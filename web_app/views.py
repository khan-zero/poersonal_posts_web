
from django.shortcuts import render
from .models import *

def index(request):

    everything_p = Post.objects.all()
    category = Category.objects.all()
    single_post = Blog_area_single_post.objects.all()
    list_post = Blog_area_list_post.objects.all()
    user_info = User.objects.all()
    return render(request, "index.html", {'posts': everything_p,
        'hidden': False,
        'categories': category,
        'single_post': single_post,
        'list_post': list_post,
        'user_info': user_info,
        })

def register(request):
    return render(request, "register.html")

def log_in(request):
    return render(request, "index.html", {'hidden': True})
    
def archive(request):
    everything_l = Links.objects.all()
    return render(request, "archive.html", {'links': everything_l, 'hidden': True})
    
def contact(request):
    return render(request, "contact.html")
