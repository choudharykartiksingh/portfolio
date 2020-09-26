from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Contact(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Subject = models.CharField(max_length=400, default="")
    msg = models.CharField(max_length=3000)
    attachment = models.FileField(upload_to='files', default='')


class Review(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Review = models.CharField(max_length=6000)
    status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="review_photo",
                              default="review_photo/default.png")


class Quote(models.Model):
    title = models.CharField(max_length=5000, default="")
    image = models.ImageField(upload_to="quotes", default="")
