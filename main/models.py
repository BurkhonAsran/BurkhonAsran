from distutils.command.upload import upload
from http import client
from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.forms import CharField, ImageField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'sotuvchi'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)
    debt = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "User"
        verbose_name_plural = "Users"

class Category(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name

class Adver(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'ads/')
    img2 = models.ImageField(upload_to = 'ads/')
    img3 = models.ImageField(upload_to = 'ads/', blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    map = models.CharField(max_length=255)
    text = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.IntegerField(choices=(
        (1, "Andijan"),
        (2, "Buxoro"),
        (3, "Jizzax"),
        (4, "Samarqand"),
        (5, "Toshkent"),
        (6, "Fargona"),
        (7, "Qashqadaryo"),
        (8, "Surxondaryo"),
        (9, "Qaralpagistan"),
        (10, "Namangan"),
        (11, "Navoiy"),
        (12, "Sirdaryo"),
        (13, "Sirdaryo"),
    ))

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Adver, on_delete=models.CASCADE)
    

class Payment(models.Model):
    money = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


