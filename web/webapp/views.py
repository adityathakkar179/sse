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

   
def bff(request):
    return render(request,'bf.html')

def caa(request):
    data21=ca.objects.all()
    return render(request,'ca1.html',{'data21':data21})

def hff(request):
    data22=halfturn.objects.all()
    return render(request,'hft.html',{'data22':data22})

def haf(request):
    data23=healthFaucets.objects.all()
    return render(request,'hef.html',{'data23':data23})

def kitchen(request):
    data24=kitchenFaucets.objects.all()
    return render(request,'kif.html',{'data24':data24})

def ali(request):
    data25=alied.objects.all()
    return render(request,'oa.html',{'data25':data25})

def qut(request):
    data26=quarterturn.objects.all()
    return render(request,'qt.html',{'data26':data26})

def sens(request):
    data27=touch.objects.all()
    return render(request,'sensor.html',{'data27':data27})


def sww(request):
    data28=shower.objects.all()
    return render(request,'sw.html',{'data28':data28})

def sl(request):
    data29=singleLever.objects.all()
    return render(request,'slf.html',{'data29':data29})


def snpp(request):
    data30=snp.objects.all()
    return render(request,'sp.html',{'data30':data30})

def kits(request):
    data31=kitchensink.objects.all()
    return render(request,'ks.html',{'data31':data31})

def bas(request):
    data32=bathac.objects.all()
    return render(request,'bathacss.html',{'data32':data32})

def cit(request):
    data33=cistern.objects.all()
    return render(request,'cist.html',{'data33':data33})

def ew(request):
    data34=ecws.objects.all()
    return render(request,'ea.html',{'data34':data34})

def flu(request):
    data35=electronicflushing.objects.all()
    return render(request,'fl.html',{'data35':data35})

def kr(request):
    data36=kidsrange.objects.all()
    return render(request,'kds.html',{'data36':data36})

def stt(request):
    data37=seatcover.objects.all()
    return render(request,'seat.html',{'data37':data37})

def sp(request):
    data38=specialneedrange.objects.all()
    return render(request,'special.html',{'data38':data38})

def urr(request):
    data39=urinals.objects.all()
    return render(request,'uri.html',{'data39':data39})

def bs(request):
    data40=washbasins.objects.all()
    return render(request,'wb.html',{'data40':data40})

def sw(request):
    data41=watersaving.objects.all()
    return render(request,'ws.html',{'data41':data41})

def btu(request):
    data42=bathtubs.objects.all()
    return render(request,'btub.html',{'data42':data42})

def btuw(request):
    data43=bathtubswirlpool.objects.all()
    return render(request,'btubwirl.html',{'data43':data43})

def cp(request):
    data44=customizeshowerpartition.objects.all()
    return render(request,'csp.html',{'data44':data44})

def ppp(request):
    data45=pressurpump.objects.all()
    return render(request,'pp.html',{'data45':data45})

def swcc(request):
    data46=showercubicles.objects.all()
    return render(request,'swc.html',{'data46':data46})

def swpp(request):
    data47=showerpanels.objects.all()
    return render(request,'swp.html',{'data47':data47})

def shpp(request):
    data48=showerpartition.objects.all()
    return render(request,'shp.html',{'data48':data48})

def stm(request):
    data49=steamshowerroom.objects.all()
    return render(request,'steam.html',{'data49':data49})


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


def upvccc(request):
    data51=upvc1.objects.all()
    return render(request,'upvcc.html',{'data51':data51})

def cpvccc(request):
    data52=cpvc.objects.all()
    return render(request,'cpv.html',{'data52':data52})
    
def dm(request):
    data53=drainmaster.objects.all()
    return render(request,'drain.html',{'data53':data53})

def allastr(request):
    return render(request,'aupc.html')

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
