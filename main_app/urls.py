from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
# from .views import ChangePasswordView

# from users.views import ChangePasswordView

urlpatterns = [
    path('', views.front, name='front'), 
    # path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 

    ### Restaurant routes ###

    path('all_restaurants/', views.all_restaurants_index, name='all_restaurants_index'), 
    path('all_restaurants/<int:restaurant_id>/', views.all_restaurants_detail, name='all_restaurants_detail'), 
    
    path('restaurants/', views.restaurants_index, name='restaurants_index'), 
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurants_detail'), 
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'), 
    path('restaurants/<int:restaurant_id>/update/', views.restaurant_update, name='restaurants_update'), 
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'), 
    path('restaurants/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),

    ### Account routes ###
    path('accounts/signup/', views.signup, name='signup'), 

    path('accounts/profile/', views.user_profile, name='user_profile'), 
    path('accounts/update/', views.user_update, name='user_update'), 
    path('accounts/delete/', views.user_delete_confirm, name='user_delete_confirm'), 

    path('accounts/password_change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('accounts/password_change_done/', views.pwd_change_done, name='pwd_change_done'), 

    ### Testing routes ###
    path('testing/', views.testing, name='testing'), 
]