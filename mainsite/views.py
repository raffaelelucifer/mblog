from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Post

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No." +str(count)+':'+str(post)+"<br>")
        post_lists.append(str(post.body)+"<br><br>")
    return HttpResponse(post_lists)
