from django.db import models as m

# Create your models here.
class Person(m.Model):
    full_name = m.CharField(max_length=20)
    img_url = m.CharField(max_length=3086)
    what_i_do = m.CharField(max_length=500)
    about_me = m.CharField(max_length=1000)


class Contact(m.CharField):
    phone = m.IntegerField()
    email = m.EmailField()
    github = m.CharField(max_length=1000 , blank=True, null=True)
    facebook = m.CharField(max_length=1000 , blank=True, null=True)
    youtube = m.CharField(max_length=1000 , blank=True, null=True)


class Exprience(m.Model):
    title = m.CharField(max_length=20)


class Project(m.Model):
    title = m.CharField(max_length=20)
    description = m.CharField(max_length=5000)
    image1 = m.ImageField()

