from django.db import models

# Create your models here.
class User(models.Model):
    UserName=models.CharField(max_length=10)
    karma=models.IntegerField(default=0)
    password=models.CharField(max_length=10)
    # set_password(pass):
    #     password=pass
    # get_karma():
    #     return karma
    # set_email(mail):
    #     email=mail
    # set_username(name):
    #     username=name