from django.db import models

# Create your models here.
class Users(models.Model):
	userId = models.CharField(max_length = 100 , default = '' , blank = False)
	pwd = models.CharField(max_length = 10 ,blank = False)
	email = models.CharField(max_length = 200 , blank=False)
	org = models.CharField(max_length = 200,blank = False)
	role = models.CharField(max_length = 50 , blank = False)
	reg_date = models.DateTimeField('date registered')

