import math
from django.shortcuts import render

# Create your views here.
from ajxx.models import Ajxx
from dzfy.models import Wzlx
from zxgk.models import Wzxx


def index(request):

    ajxxList = Ajxx.objects.all()[:7]
    zxdtList = Wzxx.objects.all()[:5]

    return render(request, 'zxgk/index.html', {'ajxxList': ajxxList, 'zxdtList': zxdtList})


def show(request, wid):

    wzxx = Wzxx.objects.get(wid=wid)

    return render(request, 'zxgk/show.html', {'wzxx': wzxx})

def list(request, id, page):
    print('11111111111111111')
    if id:
        wzlx = Wzlx.objects.get(id=id)
        print(wzlx)
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
