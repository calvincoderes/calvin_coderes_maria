from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Models and Serializers
from .models import HmoProvider, Plan, User, Cart, CartItem
from .serializers import HmoProviderSerializer, PlanSerializer, UserSerializer, CartSerializer, CartItemSerializer


# Provider
class HmoProviderListCreate(generics.ListCreateAPIView):
    queryset = HmoProvider.objects.all()
    serializer_class = HmoProviderSerializer


class ProviderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HmoProvider.objects.all()
    serializer_class = HmoProviderSerializer


class PaymentTermRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# Plan
class PlanListCreate(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# Plan Price
class PlanTermListCreate(generics.ListCreateAPIView):
    queryset = PlanTerm.objects.all()
    serializer_class = PlanTermSerializer


class PlanTermRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlanTerm.objects.all()
    serializer_class = PlanTermSerializer


# User
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Cart
class CartListCreate(generics.ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = Cart.objects.all()

        pk = self.kwargs['pk']

        if pk is not None:
            queryset = queryset.filter(user=pk)

        return queryset


class CartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        queryset = Cart.objects.all()

        user_id = self.kwargs['user_id']
        cart_id = self.kwargs['pk']

        if user_id is not None:
            queryset = queryset.filter(user=user_id)

        if cart_id is not None:
            queryset = queryset.filter(id=cart_id)

        return queryset


class CartPaid(APIView):
    def patch(self, request, pk):
        model = get_object_or_404(Cart, pk=pk)
        data = {'status': 'paid'}
        serializer = CartSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart Item
class CartItemListCreate(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['user'] = self.kwargs['user_id']
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = CartItem.objects.all()

        cart_id = self.kwargs['pk']
        if cart_id is not None:
            queryset = queryset.filter(id=cart_id)

        return queryset


class CartItemAdd(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['user'] = self.kwargs['pk']
        return self.create(request, *args, **kwargs)


class CartItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
