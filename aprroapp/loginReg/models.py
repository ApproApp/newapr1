from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models and register that model in the admin section
class User(models.Model):
    username = models.OneToOneField(User, on_delete=models.PROTECT,)
    email = models.EmailField(max_length=100, default='')
    oid = models.CharField(max_length=20, default='')
    rio = models.CharField(max_length=20, default='')
    password1 = models.CharField(max_length=20, default='')


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user = User.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

<<<<<<< HEAD
=======
# Create your models here.
class Users(models.Model):
	userId = models.CharField(max_length = 100 , default = '' , blank = False)
	pwd = models.CharField(max_length = 10 ,blank = False)
	email = models.CharField(max_length = 200 , blank=False)
	org = models.CharField(max_length = 200,blank = False)
	role = models.CharField(max_length = 50 , blank = False)
	reg_date = models.DateTimeField('date registered')
>>>>>>> 635a9962e677b79a910a5c8fa0a95a736160a0d9

