from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    # path('home',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.logoutUser, name="logout"),

    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),


    #start a business urls

    path('proprietorship', views.proprietorship, name='proprietorship'),
    path('public', views.public_ltd, name='public'),
    path('private', views.private_ltd, name='private'),
    path('partnership', views.partnership, name='partnership'),
    path('one_person', views.one_person, name='one_person'),
    path('ltd_liability', views.ltd_liability, name='ltd_liability'),


    #tax_filing urls

    path('business', views.businesstax, name='business'),
    path('esi', views.ESI, name='esi'),
    path('GST_Filing', views.GST_Filing, name='GST_Filing'),
    path('incometax', views.incomeTaxFiling, name='incometax'),
    path('tds_return', views.TDS_return, name='tds_return'),



    #BLOGS pages

    path('blog1', views.blog1, name='blog1'),
    path('blog2', views.blog2, name='blog2'),
    path('blog3', views.blog3, name='blog3'),
    path('blog4', views.blog4, name='blog4'),
    path('blog5', views.blog5, name='blog5'),
    path('blog6', views.blog6, name='blog6'),



    #All services

    path('all_services', views.all_services, name='all_services'),
    path('international_Services', views.international_Services,
         name='international_Services'),
    path('Income_Tax', views.Income_Tax, name='Income_Tax'),
    path('Accounting', views.Accounting, name='Accounting'),
    path('GST', views.GST, name='GST'),
    path('Payroll', views.Payroll, name='Payroll'),
    path('Corporate_Finance', views.Corporate_Finance, name='Corporate_Finance'),
    path('Audit', views.Audit, name='Audit'),
    path('TDS', views.TDS, name='TDS'),
    path('Corporate_Services', views.Corporate_Services, name='Corporate_Services'),
    path('Outsourcing', views.Outsourcing, name='Outsourcing'),
    path('Service_Non_Resident', views.Service_Non_Resident,
         name='Service_Non_Resident'),

    # chat box urls
    path('chat', views.chat, name='chat'),


    #all_business urls
    path('all_business', views.all_business, name='all_business'),

    path('news', views.news, name='news'),
    #registration all
    path('registration', views.registration, name='registration'),
    #tax_filing
    path('tax_filing', views.tax_filing, name='tax_filing'),

    path('hide', views.hide, name='hide'),

]
