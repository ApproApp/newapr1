from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models and register that model in the admin section
'''class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.PROTECT,)
    email = models.EmailField(max_length=100, default='')
    oid = models.CharField(max_length=20, default='')
    rio = models.CharField(max_length=20, default='')
    password1 = models.CharField(max_length=20, default='')


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user = User.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)'''
