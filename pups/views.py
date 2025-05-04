from django.shortcuts import render, redirect
from .models import Pup
from .models import AvailablePuppy
from .models import GalleryImage
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm
from django.http import Http404

# def home(request):
#     pups = Pup.objects.all()
#     available_pups = AvailablePuppy.objects.all()
#     gallery_images = GalleryImage.objects.all()
#     form=ContactForm()
#     return render(request, 'pups/home.html', {'pups': pups,'available_pups': available_pups,'gallery_images': gallery_images,'form': form})
def home(request):
    pups = Pup.objects.all()
    available_pups = AvailablePuppy.objects.all()
    gallery_images = GalleryImage.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f'New Contact Message from {name}'
            body = f"""
Name: {name}
Phone: {phone}
Email: {email}

Message:
{message}
            """

            send_mail(
                subject,
                body,
                email,
                ['timrottiez@gmail.com'],  # Your email
                fail_silently=False,
            )
            return redirect('/?submitted=true')  # Or redirect to 'home'
    else:
        form = ContactForm()
    #check if redirected after submission
    submitted = request.GET.get("submitted", False)

    return render(request, 'pups/home.html', {
        'pups': pups,
        'available_pups': available_pups,
        'gallery_images': gallery_images,
        'form': form,
        'submitted': submitted
    })

# def test_email_view(request):
#     try:
#         send_mail(
#             subject='Test Email from Timrottiez',
#             message='This is a test email sent from your Django app using python-decouple.',
#             from_email=None,
#             recipient_list=['timrottiez@gmail.com'],
#             fail_silently=False,
#         )
#         return HttpResponse("✅ Test email sent!")
#     except Exception as e:
#         return HttpResponse(f"❌ Error: {str(e)}")

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone = form.cleaned_data['phone']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#
#             subject = f'New Contact Message from {name}'
#             body = f"""
#             Name: {name}
#             Phone: {phone}
#             Email: {email}
#             Message:
#             {message}
#             """
#
#             send_mail(
#                 subject,
#                 body,
#                 email,
#                 ['timrottiez@gmail.com'],  # Your receiving address
#                 fail_silently=False,
#             )
#             return redirect('contact_success')
#     else:
#         form = ContactForm()
#     return render(request, 'pups/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'pups/contact_success.html')

def gallery_view(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'pups/gallery.html', {'gallery_images': gallery_images})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def trigger_404(request):
    raise Http404("This is a manual test of the 404 page.")