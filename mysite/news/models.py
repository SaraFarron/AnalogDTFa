from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_length=120)
    post=models.TextField()
    date=models.DateField()
    post_rating=models.IntegerField(default=10)
    amount_of_comments=models.IntegerField(default=1)
    def __str__(self):
        return self.title
    # @classmethod
    def upvote(self):
        Articles.post_rating+=1
        Articles.save()
    def downvote(self):
        Articles.post_rating-=1
        Articles.save()

class comment(models.Model):
    # Owner=username
    comment_rating=0
    text=models.TextField()
    # get_rating():
    #     return comment_rating

