from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Node
from django.http import HttpResponse
from django.utils.encoding import smart_str
import mimetypes

def drag(request):
    return render(request, 'drag.html')

def index(request):
    all = Post.objects.all()
    series = Node.objects.all()
    return render(request, 'index.html', {"all":all, "series":series})








def detail(request, id):
    row_data = get_object_or_404(Post, pk = id)
    return render(request, 'detail.html', {"row_data":row_data})


def download_file(request, pk):
    row_data = get_object_or_404(Post, pk = pk)
    fl_path = row_data.media
    file_name = row_data.media

    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(fl_path)
    return response