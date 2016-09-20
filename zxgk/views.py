import math

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ajxx.models import Ajxx
from dzfy.models import Wzlx
from zxgk.models import Wzxx
from utils import JsonUtil
from utils import PageUtil


def index(request):

    ajxxList = Ajxx.objects.all()[:7]
    zxdtList = Wzxx.objects.all()[:5]

    return render(request, 'zxgk/index.html', {'ajxxList': ajxxList, 'zxdtList': zxdtList})


def show(request, wid):

    wzxx = Wzxx.objects.get(wid=wid)

    return render(request, 'zxgk/show.html', {'wzxx': wzxx})

def list(request, id, page):
    if id:
        wzlx = Wzlx.objects.get(id=id)
        limit = 3
        if page != None:
            page = int(page)
            if page <= 0:
                page = 1
        else:
            page = 1

        totalCount = Wzxx.objects.filter(wzlx=wzlx).count()
        totalPage = math.ceil(totalCount * 1.0 / limit)
        if page >= totalPage:
            page = totalPage
        if totalPage <= 5:
            beginIndex = 1
            endIndex = totalPage
        else:
            beginIndex = page - 2
            endIndex = page + 2
            if beginIndex < 1:
                beginIndex = 1
                endIndex = 5
            if endIndex > totalPage:
                beginIndex = totalPage - 5 + 1;
                endIndex = totalPage

        indexList = ''
        for i in range(beginIndex, endIndex + 1):
            indexList = indexList + str(i)

        wzxxList = Wzxx.objects.filter(wzlx=wzlx)[(page-1)*limit:page*limit]

    return render(request, 'zxgk/articleList.html', {'wzxxList': wzxxList, 'wzlx': id, 'indexList': indexList, 'totalPage': totalPage, 'page': page})

def ajList(request, page):
    # limit = 3
    # if page != None:
    #     page = int(page)
    #     if page <= 0:
    #         page = 1
    # else:
    #     page = 1

    totalCount = Ajxx.objects.all().count()
    # totalPage = math.ceil(totalCount * 1.0 / limit)
    # if page >= totalPage:
    #     page = totalPage
    # if totalPage <= 5:
    #     beginIndex = 1
    #     endIndex = totalPage
    # else:
    #     beginIndex = page - 2
    #     endIndex = page + 2
    #     if beginIndex < 1:
    #         beginIndex = 1
    #         endIndex = 5
    #     if endIndex > totalPage:
    #         beginIndex = totalPage - 5 + 1;
    #         endIndex = totalPage
    #
    # indexList = ''
    # for i in range(beginIndex, endIndex + 1):
    #     indexList = indexList + str(i)
    #
    # ajlist = Ajxx.objects.all()[(page - 1) * limit:page * limit]
    # if request.method == 'POST':
    #     ajlist = JsonUtil.class_to_dict(ajlist)
    #     print(str(ajlist))
    #     return HttpResponse(str(ajlist))
    limit = 4
    pageInfor = PageUtil.getPage(page, limit, totalCount)


    ajlist = Ajxx.objects.all()[(pageInfor.get('page') - 1) * limit:pageInfor.get('page') * limit]



    return render(request, 'zxgk/executeInfo-list.html', {'ajlist': ajlist, 'pageInfor': pageInfor})
    
    

def ajShow(request, aid):
    if aid:
        ajxx = Ajxx.objects.get(aid=aid)
        return render(request, 'zxgk/executeInfo-details.html', {'ajxx': ajxx})

def sxpg(request, page):
    limit = 4
    totalCount = Ajxx.objects.all().count()
    pageInfor = PageUtil.getPage(page, limit, totalCount)
    ajlist = Ajxx.objects.all()[(pageInfor.get('page') - 1) * limit:pageInfor.get('page') * limit]
    return render(request, 'zxgk/executeInfo-list.html', {'ajlist': ajlist, 'pageInfor': pageInfor})
