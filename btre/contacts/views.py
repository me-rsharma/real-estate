from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        email = request.POST['email']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made inquiry for this property")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        # Send mail
        send_mail(
            'Property Listing Inquiry ',
            'There has been inquiry for '+ listing + '. Sign in into the admin panel for more info',
            'sharma.rajeshwar6@gmail.com',
            ['sharma.rajeshwar9@gmail.com', realtor_email],
            fail_silently = False
        )
        messages.success(request, "Your request has been submitted, a realtor will get back to you soon")
        return redirect("/listings/"+listing_id)
