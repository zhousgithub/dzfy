import random
import time

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from dzfy import models
from dzfy.models import User


def home(request):

    return render(request, "index.html")

# def login(request):
#
#     return render(request, 'login.html')
#
# def insert(request):
#
#     user = User(2, 'aa', '1111', 21)
#     user.save()
#     print('插入数据成功')
#     return HttpResponse('seccess')
#
# def select(request):
#
#     # list = User.objects.get(name__contains='s')
#     list = User.objects.all()
#     for u in list:
#         print(u.name)
#     return HttpResponse('seccess')
#
# def login(request):
#     user = models.User;
#     user.name = request.GET('name')
#     user.password = request.GET('password')
#     print(user.name)
#     print(user.password)
#     return ''
def imageUp(request):
    #    print request.FILES
    if request.method == 'POST':
        b = save_file(request.FILES['upfile'])
    return HttpResponse(b)


def save_file(file, path=''):
    filename = str(time.time()) + str(random.random()) + file._get_name()
    # print filename
    fd = open('%s/%s' % (settings.MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
    a = "{'url':'/media/" + filename + "','title':'" + filename + "','state':'SUCCESS'}"
    print(a)
    return a
from fayuan import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import os
import time
import uuid


def __myuploadfile(fileObj, source_pictitle, source_filename, fileorpic='pic'):
    """ 一个公用的上传文件的处理 """
    myresponse = ""
    if fileObj:
        filename = fileObj.name.decode('utf-8', 'ignore')
        fileExt = filename.split('.')[-1]
        file_name = str(uuid.uuid1())
        subfolder = time.strftime("%Y%m")
        if not os.path.exists(settings.MEDIA_ROOT[0] + subfolder):
            os.makedirs(settings.MEDIA_ROOT[0] + subfolder)
        path = str(subfolder + '/' + file_name + '.' + fileExt)

        if fileExt.lower() in (
        'jpg', 'jpeg', 'bmp', 'gif', 'png', "rar", "doc", "docx", "zip", "pdf", "txt", "swf", "wmv"):

            phisypath = settings.MEDIA_ROOT[0] + path
            destination = open(phisypath, 'wb+')
            for chunk in fileObj.chunks():
                destination.write(chunk)
            destination.close()

            if fileorpic == 'pic':
                if fileExt.lower() in ('jpg', 'jpeg', 'bmp', 'gif', 'png'):
                    im = open(phisypath)
                    im.thumbnail((720, 720))
                    im.save(phisypath)

            real_url = '/static/upload/' + subfolder + '/' + file_name + '.' + fileExt
            myresponse = "{'original':'%s','url':'%s','title':'%s','state':'%s'}" % (
            source_filename, real_url, source_pictitle, 'SUCCESS')
    return myresponse


@csrf_exempt
def ueditor_ImgUp(request):
    """ 上传图片 """
    fileObj = request.FILES.get('upfile', None)
    source_pictitle = request.POST.get('pictitle', '')
    source_filename = request.POST.get('fileName', '')
    response = HttpResponse()
    myresponse = __myuploadfile(fileObj, source_pictitle, source_filename, 'pic')
    response.write(myresponse)
    return response


@csrf_exempt
def ueditor_FileUp(request):
    """ 上传文件 """
    fileObj = request.FILES.get('upfile', None)
    source_pictitle = request.POST.get('pictitle', '')
    source_filename = request.POST.get('fileName', '')
    response = HttpResponse()
    myresponse = __myuploadfile(fileObj, source_pictitle, source_filename, 'file')
    response.write(myresponse)
    return response


@csrf_exempt
def ueditor_ScrawUp(request):
    """ 涂鸦文件,处理 """
    pass


@csrf_exempt
def upfile(request):
    file = request.FILES['upfile']
    with open(settings.MEDIA_ROOT + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    url = file.name
    title = file.name[:-4]
    original = file.name
    response = HttpResponse(
        "{'state': 'SUCCESS', 'url':'" + url + "','title':'" + title + "', 'original':'" + original + "'}")
    response.__setitem__("Access-Control-Allow-Origin", "*")
    return response