from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[MinLengthValidator(3)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Plan(models.Model):
    hmo_provider = models.ForeignKey('marketplace.HmoProvider', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], unique=True)
    description = models.CharField(max_length=500, validators=[MinLengthValidator(3)])
    monthly_term = models.BooleanField(default=True)
    quarterly_term = models.BooleanField(default=True)
    annual_term = models.BooleanField(default=True)
    annual_price = models.FloatField(default=0)
    quarterly_price = models.FloatField(default=0)
    monthly_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def plan_terms(self):
    #     return self.planterm_set.all()


class HmoProvider(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    cart = models.ForeignKey('marketplace.Cart', on_delete=models.CASCADE, blank=True)
    plan = models.ForeignKey('marketplace.Plan', on_delete=models.CASCADE)
    payment_term = models.CharField(max_length=50, default=)
    quantity = models.IntegerField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Cart(models.Model):
    STATUS_OPEN = 'open'
    STATUS_PAID = 'paid'
    STATUSES = (
        (STATUS_OPEN, 'open'),
        (STATUS_PAID, 'Paid')
    )
    user = models.ForeignKey('marketplace.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=12, default=STATUS_OPEN, choices=STATUSES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Cart ID# ' + str(self.pk) + ' (' + self.status + ')'

    def cart_items(self):
        return self.cartitem_set.all()
