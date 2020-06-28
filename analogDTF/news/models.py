from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_length=120)
    post=models.TextField()
    date=models.DateField()
    post_rating=0
    amount_of_comments=0
    def __str__(self):
        return self.title

class comment(models.Model):
    # Owner=username
    comment_rating=0
    text=models.TextField()
    # get_rating():
    #     return comment_rating

class User(models.Model):
    username="Enter your name"
    karma=0
    password="Enter your password"
    email="Enter your email"
    # set_password(pass):
    #     password=pass
    # get_karma():
    #     return karma
    # set_email(mail):
    #     email=mail
    # set_username(name):
    #     username=name