from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path('', views.home, name='home'),

    # AUTHENTICATION
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # CATEGORY PAGES
    path('cakes/', views.cakes, name='cakes'),
    path('cupcakes/', views.cupcakes, name='cupcakes'),
    path('bouquets/', views.bouquets, name='bouquets'),
    path('brownies/', views.brownies, name='brownies'),
    path('pastries/', views.pastries, name='pastries'),
    path('cookies/', views.cookies, name='cookies'),
    path('savouries/', views.savouries, name='savouries'),

    # CART + ANALYTICS
    path('cart/', views.cart, name='cart'),
    path('analytics/', views.analytics, name='analytics'),

    # CART ACTIONS
    path('add-to-cart/<str:name>/<int:price>/', views.add_to_cart, name='add_to_cart'),

    path('increase/<str:name>/', views.increase_quantity, name='increase'),

    path('decrease/<str:name>/', views.decrease_quantity, name='decrease'),

    path('remove/<str:name>/', views.remove_item, name='remove_item'),
]
