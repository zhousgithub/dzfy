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
