import uuid

from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from ajxx.models import Ajlx
from cpws.Forms import CpwsForm
from cpws.models import Cpws
from utils import PageUtil


def index(request):

    ajlxlist = Ajlx.objects.all()

    # request.session['ajlxlist'] = JsonUtil.class_to_dict(ajlxlist)

    # print(request.session.get("ajlxlist"))

    wslist = Cpws.objects.filter(ajxx__ajlx=ajlxlist[0])[:5]

    hotlist = Cpws.objects.order_by('-djl')[:7]

    return render(request, 'cpws/index.html', {'wslist': wslist, 'hostlist': hotlist, 'ajlxlist': ajlxlist, 'i': 0})

def edit(request):

    if request.method == 'POST':
        cf = CpwsForm(request.POST)
        if cf.is_valid():
            bt = cf.cleaned_data['bt']
            fbr = cf.cleaned_data['fbr']
            fymc = cf.cleaned_data['fymc']
            lx = cf.cleaned_data['lx']
            nr = cf.cleaned_data['nr']
            cid = str(uuid.uuid4()).replace('-', '')
            cpws = Cpws(cid=cid, bt=bt, fymc=fymc, fbr=fbr, lx=lx, nr=nr)
            cpws.save()
            return HttpResponseRedirect('index.html')
    form = CpwsForm
    return render(request, 'cpws/edit.html', {'form': form})

def show(request, lx, cid):
    if cid:
        ajlxlist = Ajlx.objects.all()
        ajlx = get_object_or_404(Ajlx, id=lx)
        cpws = get_object_or_404(Cpws, cid=cid)
        c = cpws
        c.djl = cpws.djl + 1
        c.save()
        return render(request, 'cpws/details.html', {'cpws': cpws, 'ajlxlist': ajlxlist, 'ajlx': ajlx})

def list(request, lx, page):
    ajlxlist = Ajlx.objects.all()
    if lx:
        limit = 3
        ajlx = get_object_or_404(Ajlx, id=lx)
        totalCount = Cpws.objects.filter(ajxx__ajlx=lx).count()
        pageInfo = PageUtil.getPage(page, limit, totalCount)

        list = Cpws.objects.filter(ajxx__ajlx=lx)[(pageInfo.get('page')-1)*pageInfo.get('limit'):pageInfo.get('page')*pageInfo.get('limit')]
        return render(request, 'cpws/list.html', {'list': list, 'pageInfo': pageInfo, 'ajlxlist': ajlxlist, 'ajlx': ajlx})
    pass

def byAjlx(request, lx):
    if lx:
        wslist = Cpws.objects.filter(ajxx__ajlx=lx)[:5]
        wslist = serializers.serialize('json', wslist)
        print(wslist)
        return HttpResponse(wslist, content_type="application/json")
