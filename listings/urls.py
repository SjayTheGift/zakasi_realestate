
from django.urls import path

from . import views 

urlpatterns = [
    path('listings/', views.ListingView.as_view(), name="listings"),
    path('listings/<int:pk>/', views.ListingDetailView.as_view(), name="listing_detail"),
    path('contact/', views.contact, name="contact"),
]
