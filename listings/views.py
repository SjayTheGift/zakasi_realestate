from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import generic

from .models import Listing, Contact


class ListingView(generic.ListView):
    model = Listing
    queryset = Listing.objects.all().order_by('-list_date')
    context_object_name = "listings"
    template_name = "listings.html"
    paginate_by = 6


class ListingDetailView(generic.DetailView):
    template_name = "listing.html"
    model = Listing


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing.')
                return redirect(f'/listings/{listing_id}')

        contact_details = Contact(listing=listing,
                                  listing_id=listing_id,
                                  name=name,
                                  email=email,
                                  phone=phone,
                                  message=message,
                                  user_id=user_id
                                  )
        contact_details.save()
        # send_mail(
        #     'Property Listing Inquiry',
        #     f'There has been an inquiry for {listing}. Sign into the admin panel for more info.',
        #     'jonas.gift83@gmail.com',
        #     [realtor_email, 'jonas.esethu24@gmail.com'],
        #     fail_silently=False
        # )
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect(f'/listings/{listing_id}')

