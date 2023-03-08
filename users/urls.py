from django.urls import path
from .views import Profile, change_password, RegisterView

urlpatterns = [
    path('accounts/profile/', Profile.as_view(), name="profile"),
    path('change-password/', change_password, name="change_password"),
    path('register/', RegisterView.as_view(), name='register'),
]
