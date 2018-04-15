from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save

# Create your models and register that model in the admin section
class User(AbstractUser):
    email = models.EmailField(max_length=100, default='')
    oid = models.CharField(max_length=20, default='')
    rio = models.CharField(max_length=20, default='')
#
# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user = User.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile, sender=User)
    def __str__(self):
        return self.username
