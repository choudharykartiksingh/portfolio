from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Review, Quote
from .models import Greeting
from django.core.mail import send_mail,send_mass_mail
from gettingstarted.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage

# Create your views here.


def index(request):
    if request.method == "POST":
        c = Contact()
        c.Name = request.POST.get("Name")
        c.Email = request.POST.get("Email")
        c.Subject = request.POST.get("Subject")
        c.msg = request.POST.get("msg")
        c.attachment = request.POST.get("attachment")
        # send_mail(c.Subject, c.Name+" - "+c.Email+" - "+c.msg, EMAIL_HOST_USER, [
        #           "kartik123choudhary@gmail.com"], fail_silently=False)
        # send_mail("Thanks for Contacting Me", "Hey Dear "+c.Name+", Thanks for contact,I will shortly reply to your message\n-Kartik", EMAIL_HOST_USER, [
        #           c.Email], fail_silently=False)
        c.save()
        # feedback ={"err":"Your text has been send Successfully"}
        return HttpResponseRedirect('thank_you')
    quotes = Quote.objects.all().order_by("id")
    reviews = Review.objects.filter(status=True).order_by("id")
    return render(request, "index.html", {"reviews": reviews, "quotes": quotes})


def review_submit(request):
    if request.method == "POST":
        r = Review()
        r.Name = request.POST.get("Name")
        r.Email = request.POST.get("Email")
        r.Review = request.POST.get("Review")
        
        try:
            image = request.FILES['attachment']
            print(image)
            r.photo = image
            r.save()
            try:
                message1 = ("New Review by "+r.Name, r.Name+" - "+r.Review+" email-id: "+r.Email,EMAIL_HOST_USER, ["kartik123choudhary@gmail.com"])
                f= f'Hey Dear {r.Name},\nThanks for your review on my website. I will publish it soon.\nHave a good day:)'
                message2 = ("Thanks for Review", f,EMAIL_HOST_USER, [r.Email])
                send_mass_mail((message1, message2), fail_silently=False)
            except Exception as e:
                print('Email sending error: ',e)  
            try:
                msg = EmailMessage(
                    'New review image',
                    'this is the image',
                    'EMAIL_HOST_USER',
                    ['kartik123choudhary@gmail.com'],
                    headers={'Message-ID': 'foo'},
                )
                msg.content_subtype = "html"
                if image:
                    print('extension',str(r.photo.name).split(".")[-1])
                    mime_image = MIMEImage(r.photo.read(),_subtype=str(r.photo.name).split(".")[-1])
                    mime_image.add_header('Content-ID', '<image>')
                    msg.attach(mime_image)
                    print('mime image',mime_image)
                msg.send()
            except:
                pass
        except Exception as e:
            print('image is not given',e)
            r.save()
            try:
                message1 = ("New Review by "+r.Name, r.Name+" - "+r.Review+" email-id: "+r.Email,EMAIL_HOST_USER, ["kartik123choudhary@gmail.com"])
                f= f'Hey Dear {r.Name},\nThanks for your review on my website. I will publish it soon.\nYou can send your image to show on website on this email: kartik123choudhary@gmail.com\nHave a good day:)'
                message2 = ("Thanks for Review", f,EMAIL_HOST_USER, [r.Email])
                send_mass_mail((message1, message2), fail_silently=False)
            except Exception as e:
                print('Email sending error: ',e)    
            
        return redirect('/')
    else:
        return redirect('/')


def thank_you(request):
    return redirect(index)


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
