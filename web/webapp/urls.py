from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name='index'),
    path('aboutus',views.about,name='about'),
    path('product',views.product,name='works'),
    path('contact',views.contact,name='contact'),
    path('ultratech',views.ultratech1,name='ultratech'),
    path('astral',views.astr,name='astral'),
    path('berger',views.berg,name='berger'),
    path('steel',views.st,name='steel'),
    path('rmc',views.rc,name='ur'),
    path('aggregates',views.agre,name='aggregates'),
    path('cera',views.bf,name='cera'),
    path('tatawiron',views.tw,name='tatawiron'),
    path('watertank',views.wt,name='water'),
    path('constructionsloution',views.cs,name='solu'),
    path('waterproofing',views.wp,name='proof'),
    path('tileadhesive',views.ta,name='tile'),
    path('jointmortar',views.jm,name='joint'),
    path('birlawhite',views.bw,name='birla'),
    path('kdm',views.kd,name='kdm'),
    #path('info/',views.inn),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)