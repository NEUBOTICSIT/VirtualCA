from django.urls import path
from .import views

urlpatterns = [
    path('', views.msme_about, name='msme_about'),

    # path('home',views.msme_home,name='msme_home'),
    path('msme_reg', views.msme_reg, name='msme_reg'),

    path('aadhaar', views.aadhaar, name='aadhaar'),
    path('demo', views.msme_demo, name='demo'),
    path('FAQ', views.msme_FAQ, name='msme_FAQ'),

    #MSME_reg_process_urls

    path('reg1', views.reg1, name='reg1'),
    path('reg2', views.reg2, name='reg2'),
    path('reg3', views.reg3, name='reg3'),
    path('reg4', views.reg4, name='reg4'),


    # stepperTab urls
    path('tab', views.msme_tab, name='msme_tab'),


    # stepperdemo
    path('tab_demo', views.tab_demo, name='tab_demo'),

    #modalbox urls
    path('modal', views.modal, name='modal'),


    #payment urls

    path('pay', views.pay, name='pay'),

    path('stepper', views.stepper, name='stepper'),

]
