from django.shortcuts import render,redirect,HttpResponseRedirect
from django.conf import settings
from .models import *
from .forms import fm

# Create your views here.

def index(request):
    data14=offer.objects.all()
    return render(request,'index.html',{'data14':data14})

def about(request):
    if request.method == 'POST':
        form = fm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = fm()
    return render(request,'about.html',{'form':form})

    return render(request,'about.html')
    
    
def product(request):
    return render(request,'works.html')


def contact(request):
    if request.method == 'POST':
        form = fm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = fm()
    return render(request,'contact.html',{'form':form})

    return render(request,'contact.html')
    

def ultratech1(request):
    data=ultratech.objects.all()
    return render(request,'ultratech.html',{'data':data})

def astr(request):
    data1=astral.objects.all()
    return render(request,'astral.html',{'data1':data1})

def berg(request):
    data2=berger.objects.all()
    return render(request,'berger.html',{'data2':data2})

def st(request):
    data3=steel.objects.all()
    return render(request,'steel.html',{'data3':data3})

def rc(request):
    data4=rmc.objects.all()
    return render(request,'ur.html',{'data4':data4})

def agre(request):
    data5=aggregates.objects.all()
    return render(request,'aggregates.html',{'data5':data5})

def bf(request):
    data6=BathroomFittings.objects.all()
    return render(request,'cera.html',{'data6':data6})

def tw(request):
    data7=tatawiron.objects.all()
    return render(request,'tatawiron.html',{'data7':data7})

def wt(request):
    data8=waterTank.objects.all()
    return render(request,'water.html',{'data8':data8})

def cs(request):
    data9=constructionSolution.objects.all()
    return render(request,'solu.html',{'data9':data9})

def wp(request):
    data10=waterproofing.objects.all()
    return render(request,'proof.html',{'data10':data10})

def ta(request):
    data11=tileadhesive.objects.all()
    return render(request,'tile.html',{'data11':data11})

def jm(request):
    data12=jointmortar.objects.all()
    return render(request,'joint.html',{'data12':data12})

def bw(request):
    data13=birlawhite.objects.all()
    return render(request,'birla.html',{'data13':data13})

def kd(request):
    data15=kdm.objects.all()
    return render(request,'kdm.html',{'data15':data15})

#def inn(request):
#   udata=form.objects.all()

#    return render(request,'info.html',{'udata':udata})
