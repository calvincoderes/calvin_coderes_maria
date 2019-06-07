from rest_framework import serializers
from .models import HmoProvider, Plan, User, Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import logging


class HmoProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HmoProvider
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    plan_terms = PlanTermSerializer(read_only=True, many=True)

    class Meta:
        model = Plan
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'

    def validate(self, data):
        if 'plan_term' in data and 'plan' in data and PlanTerm.objects.filter(id=data['plan_term'].id,
                                                                              plan=data['plan']).exists() == False:
            raise serializers.ValidationError({'plan_term': ['Payment Term does not belong to the Plan you selected']})

        return data

    def create(self, validated_data):
        user_id = None
        request = self.context.get('request')

        if 'user' in request.data:
            user_id = request.data['user']

        user = User.objects.get(pk=user_id)

        try:
            cart = Cart.objects.get(user=user, status='not_yet_paid')
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=user, status='not_yet_paid')
            cart.save()

        validated_data['cart'] = cart

        try:
            cart_item = CartItem.objects.get(
                                    cart=validated_data.get('cart'),
                                    plan=validated_data.get('plan'),
                                    plan_term=validated_data.get('plan_term'),
                                )
            cart_item.quantity += validated_data.get('quantity')
            cart_item.save()
        except ObjectDoesNotExist:
            cart_item = CartItem.objects.create(**validated_data)

        return cart_item


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = '__all__'


