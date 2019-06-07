from django.urls import path
from . import views

app_name = 'marketplace'

"""
1. View all plans                                - 'plan/'
2. Create new carts                            - 'user/<int:pk>/cart_item/' or 'user/<int:pk>/cart/'
3. Add Cart Items to Cart                         - 'user/<int:pk>/cart_item/' or 'user/<int:user_id>/cart/<int:pk>/'
4. Update the count of cart item            - 'user/<int:user_id>/cart/<int:pk>/cart_item/<int:pk>'
5. Remove a cart item                  - 'user/<int:user_id>/cart/<int:pk>/cart_item/<int:pk>'
6. See the cart item                         - 'user/<int:user_id>/cart/<int:pk>/cart_item'
7. Pay for the cart                                 - 'cart/<int:pk>/paid' or 'user/<int:user_id>/cart/<int:pk>/'
"""
urlpatterns = [
    # HMOProvider CRUD
    path('hmoprovider/', views.HmoProviderListCreate.as_view()),
    path('hmoprovider/<int:pk>/', views.ProviderRetrieveUpdateDestroy.as_view()),


    # Plan's CRUD
    path('plan/', views.PlanListCreate.as_view()),
    path('plan/<int:pk>/', views.PlanRetrieveUpdateDestroy.as_view()),


    # User's CRUD
    path('user/', views.UserListCreate.as_view()),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view()),


    # User's Cart List/Create View
    path('user/<int:pk>/cart/', views.CartListCreate.as_view()),


    # User's Cart View (specific cart)
    path('user/<int:user_id>/cart/<int:pk>/', views.CartRetrieveUpdateDestroy.as_view()),


    # User's Cart Items
    path('user/<int:user_id>/cart/<int:pk>/cart_item/', views.CartItemListCreate.as_view()),
    path('user/<int:user_id>/cart/<int:cart_id>/cart_item/<int:pk>/', views.CartItemRetrieveUpdateDestroy.as_view()),

    # 1. This 'user/<int:pk>/cart_item/' endpoint can automatically create Cart if not yet exists
    # 2. Duplicate plan/plan_term will add the value of current plus the entered quantity

    # User's Add to Cart Function
    path('user/<int:pk>/cart_item/', views.CartItemAdd.as_view()),

    # Mark Cart as Paid
    path('cart/<int:pk>/paid', views.CartPaid.as_view()),

]
