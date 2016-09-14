import uuid

import math
from django.forms import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.
from cpws.Forms import CpwsForm
from cpws.models import Cpws


def index(request):

    wslist = Cpws.objects.filter(wslb=1)[:5]

    hotlist = Cpws.objects.order_by('-djl')[:7]

    return render(request, 'cpws/index.html', {'wslist': wslist, 'hostlist': hotlist})

def edit(request):

    if request.method == 'POST':
        cf = CpwsForm(request.POST)
        if cf.is_valid():
            bt = cf.cleaned_data['bt']
            fbr = cf.cleaned_data['fbr']
            fymc = cf.cleaned_data['fymc']
            wslb = cf.cleaned_data['wslb']
            nr = cf.cleaned_data['nr']
            cid = str(uuid.uuid4()).replace('-', '')
            cpws = Cpws(cid=cid, bt=bt, fymc=fymc, fbr=fbr, wslb=wslb, nr=nr)
            cpws.save()
            return HttpResponseRedirect('index.html')
    form = CpwsForm
    return render(request, 'cpws/edit.html', {'form': form})

def show(request, cid):
    if cid:
        cpws = Cpws.objects.get(cid=cid)
        c = cpws
        c.djl = cpws.djl + 1
        c.save()
        return render(request, 'cpws/details.html', {'cpws': cpws})
    pass

def list(request, wslb, page):
    if wslb:
        limit = 3
        if page:
            page = int(page)
            if page <= 0:
                page = 1
        else:
            page = 1
        
        totalCount = Cpws.objects.filter(wslb=wslb).count()
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
        for i in range(beginIndex, endIndex+1):
            indexList = indexList + str(i)

        list = Cpws.objects.filter(wslb=wslb)[(page-1)*limit:page*limit]
        return render(request, 'cpws/list.html', {'list': list, 'ajlx': wslb, 'indexList': indexList, 'totalPage': totalPage, 'page': page})
    pass

# def getpage()
