from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mainsite.models import Post
from datetime import datetime

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    #post_lists = list()
    #for count, post in enumerate(posts):
    #    post_lists.append("No." +str(count)+':'+str(post)+"<br>")
    #    post_lists.append(str(post.body)+"<br><br>")
    #return HttpResponse(post_lists)
    return HttpResponse(html)
