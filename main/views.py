from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.encoding import smart_str
import mimetypes
from .models import Members, Projects, Posts

from django.core.files.storage import FileSystemStorage
def drag(request):
    return render(request, 'drag.html')

def index(request):

    return render(request, 'index.html')


def detail(request, id):
    pjinfo = get_object_or_404(Projects, pk=id)
    nodes = Posts.objects.filter(projectNo = id)
    return render(request, 'detail.html', {'pjinfo':pjinfo,"nodes":nodes,})


# 혜선의 testing code
def upload(request):
    # File storage API - FileSystemStorage
    context={}
    if request.method=="POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file.content_type)
        fs = FileSystemStorage() #이미 업데이트 된 파일을 업로드하면 이름에 random string이 추가된다. 링크에 8000/media(=MEDIA_URL)/파일이름 하면 파일 열람 가능.(urls.py에 += 했던 부분의 내용이다. )
        name = fs.save(uploaded_file.name, uploaded_file) #media 폴더에 저장된다.
        # url = fs.url(name)
        # print(url)
        context['url']=fs.url(name)
    return render(request, 'upload.html', context)

