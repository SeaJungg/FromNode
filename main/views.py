from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.encoding import smart_str
import mimetypes

def drag(request):
    return render(request, 'drag.html')

def index(request):
    return render(request, 'index.html')


def detail(request, id):
    return render(request, 'detail.html')

