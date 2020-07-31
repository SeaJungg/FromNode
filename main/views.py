from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.encoding import smart_str
import mimetypes
from .models import Members, Projects, Posts
import users

def drag(request):
    return render(request, 'drag.html')

def index(request):
    return render(request, 'index.html')


def detail(request, id):
    pjinfo = get_object_or_404(Projects, pk=id)
    nodes = Posts.objects.filter(projectNo = id)
    return render(request, 'detail.html', {'pjinfo':pjinfo,"nodes":nodes})

def login(request):
    return render(request, 'account/login.html')
