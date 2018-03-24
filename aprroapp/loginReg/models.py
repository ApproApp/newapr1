from django.db import models

# Create your models here.
class Users(models.Model):
	userId = models.CharField(max_length = 100)
	pwd = models.CharField(max_length = 10)
	org = models.CharField(max_length = 200)
	role = models.CharField(max_length = 50)
	reg_date = models.DateTimeField('date registered')

