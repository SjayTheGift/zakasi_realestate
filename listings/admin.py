from django.contrib import admin
from .models import Listing, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listings')
    list_per_page = 25
    list_filter = ('name', 'email')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'realtor', 'price', 'province', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('list_date', 'is_published', 'price', 'province')
    list_editable = ('is_published', )
    search_fields = ('title', 'city', 'province', 'price')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(Listing, ListingAdmin)
