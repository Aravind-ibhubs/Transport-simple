from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.registration, name="signup" ),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="User Logout"),
]

