from django.shortcuts import render

# Create your views here.
def upvote():
    articles.post_rating+=1

def downvote():
    articles.post_rating-=1

#def add_comment():
    #comments_number+=1
