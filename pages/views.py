from django.shortcuts import render
from django.views import generic
from listings.models import Listing
from realtors.models import  Realtor
from listings.choices import bedroom_choices, price_choices, province_choices

class HomeView(generic.ListView):
    model = Listing
    queryset = Listing.objects.all().order_by("-list_date")[:3]
    template_name = "index.html"
    context_object_name = "listings"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices
        context['province_choices'] = province_choices
        return context


def about(request):
    realtors = Realtor.objects.all()
    context = {
        "realtors": realtors
    }
    return render(request, template_name="about.html", context=context)


def search(request):
    queryset_listing = Listing.objects.all().order_by("-list_date")

    #keywords

    if "keywords" in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_listing = queryset_listing.filter(description__icontains=keywords)

    #city

    if "city" in request.GET:
        city = request.GET['city']
        if city:
            queryset_listing = queryset_listing.filter(city__iexact=city)

    #Province

    if "province" in request.GET:
        province = request.GET['province']
        if province:
            queryset_listing = queryset_listing.filter(province__iexact=province)

    # Bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_listing = queryset_listing.filter(bedrooms__lte=bedrooms)

    # Price
    if "price" in request.GET:
        price = request.GET['price']
        if price:
            queryset_listing = queryset_listing.filter(price__lte=price)

    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "province_choices": province_choices,
        "listings": queryset_listing,
        "values": request.GET
    }
    return render(request, template_name="search.html", context=context)
