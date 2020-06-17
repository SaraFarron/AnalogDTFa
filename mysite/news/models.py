from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_length=120)
    post=models.TextField()
    date=models.DateField()
    post_rating=0
    amount_of_comments=0
    # slug = models.SlugField(max_length=100, db_index=True)
    def __str__(self):
        return self.title

def upvote():
    post_rating=+1

def downvote():
    post_rating=-1

def add_comment():
    comments_number=+1

class comment(models.Model):
    # Owner=username
    comment_rating=0
    text=models.TextField()

class User(models.Model):
    Username="Enter your name"
    Karma=0
    password="Enter your password"
    email="Enter your email"
