from django.db import models
from datetime import datetime

from django.urls import reverse
from realtors.models import Realtor


class Listing(models.Model):
    CHOICE_PROVINCE = [
        ("EC", "Eastern Cape"),
        ("FS", "Free State"),
        ("GP", "Gauteng"),
        ("KZN", "KwaZulu-Natal"),
        ("LP", "Limpopo"),
        ("MP", "Mpumalanga"),
        ("NC", "Northern Cape"),
        ("NW", "North West"),
        ("WC", "Western Cape")
    ]
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=200, choices=CHOICE_PROVINCE)
    postal_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to="photo/%Y/%m/%d")
    photo_one = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    photo_two = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    photo_three = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    photo_four = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    photo_five = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    photo_six = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing_detail', args=[str(self.id)])


class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
