from django.urls import path, include
from allauth.account.views import SignupView, LoginView, LogoutView
from . import views
from users import urls

app_name = 'users'
urlpatterns = [
    path('signup', SignupView.as_view(), name="account_signup"),    # account_signup
    path('login', LoginView.as_view(), name="account_login"),       #  account_login
    path('logout', LogoutView.as_view(), name="account_logout"),    # account_logout
]