from django.urls import path

from . import views

urlpatterns=[
path('',views.home,name='home'),
path('pay',views.pay, name='pay'),
path('login',views.login, name='login'),
path('about',views.about, name='about'),
path('booking',views.booking, name='booking'),
path('final',views.final, name='final'),
path('regist',views.regist, name='regist'),
path('tour',views.tour, name='tour'),  
path('thank',views.thank, name='thank')
]
