from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from .models import Contact,Headline

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .forms import CreateUserForm
# Create your views here.
# def home(request):
#     return render(request,'CA_app/home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'CA_app/SIGNUP_LOGIN/signup.html', context)


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'CA_app/SIGNUP_LOGIN/login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('login')




def about(request):
    return render(request,'CA_app/about.html')


def blog(request):
    return render(request,'CA_app/BLOGS/All_Blog/blog.html')




def contact(request):
    if  request.method=="POST":
        Your_Name=request.POST.get('Your_Name')
        Your_Email=request.POST.get('Your_Email')
        Your_Subject=request.POST.get('Your_Subject')
        Your_Message=request.POST.get('Your_Message')
        Contact(Your_Name=Your_Name,Your_Email=Your_Email,Your_Subject=Your_Subject,Your_Message=Your_Message).save()

        return render(request, 'CA_app/index.html')
    else:
        return render(request, 'CA_app/contact.html')

#
# start a business

def proprietorship(request):
    return render(request,'CA_app/START_A_BUSINESS/proprietorship.html')


def partnership(request):
    return render(request,'CA_app/START_A_BUSINESS/partnership.html')


def public_ltd(request):
    return render(request,'CA_app/START_A_BUSINESS/public_ltd_company.html')


def private_ltd(request):
    return render(request,'CA_app/START_A_BUSINESS/private_ltd_company.html')

def one_person(request):
    return render(request,'CA_app/START_A_BUSINESS/one_person_company.html')

def ltd_liability(request):
    return render(request,'CA_app/START_A_BUSINESS/ltd_liability_partnership.html')



#tax-filing

def businesstax(request):
    return render(request,'CA_app/TAX_FILING/businessTaxFiling.html')


def ESI(request):
    return render(request,'CA_app/TAX_FILING/ESI_Return.html')



def GST_Filing(request):
    return render(request,'CA_app/TAX_FILING/GST_Filing.html')


def incomeTaxFiling(request):
    return render(request,'CA_app/TAX_FILING/incomeTaxFiling.html')


def TDS_return(request):
    return render(request,'CA_app/TAX_FILING/TDS_Return.html')



#BLOGS pages views

def blog1(request):
    return render(request,'CA_app/BLOGS/blog1.html')

def blog2(request):
    return render(request,'CA_app/BLOGS/blog2.html')

def blog3(request):
    return render(request,'CA_app/BLOGS/blog3.html')

def blog4(request):
    return render(request,'CA_app/BLOGS/blog4.html')

def blog5(request):
    return render(request,'CA_app/BLOGS/blog5.html')

def blog6(request):
    return render(request,'CA_app/BLOGS/blog6.html')




def index(request):
    all_news = Headline.objects.all()

    return render(request, 'CA_app/index.html', context = {'index': all_news})



#all services

def all_services(request):
    return render(request,'CA_app/SERVICES/All_Services/all_services.html')

def international_Services(request):
    return render(request,'CA_app/SERVICES/international_Services.html')

def Accounting(request):
    return render(request,'CA_app/SERVICES/Accounting.html')
def Income_Tax(request):
    return render(request,'CA_app/SERVICES/Income_Tax.html')
def GST(request):
    return render(request,'CA_app/SERVICES/GST.html')
def Payroll(request):
    return render(request,'CA_app/SERVICES/Payroll.html')
def Corporate_Finance(request):
    return render(request,'CA_app/SERVICES/Corporate_Finance.html')
def Audit(request):
    return render(request,'CA_app/SERVICES/Audit.html')
def TDS(request):
    return render(request,'CA_app/SERVICES/TDS.html')
def Corporate_Services(request):
    return render(request,'CA_app/SERVICES/Corporate_Services.html')
def Outsourcing(request):
    return render(request,'CA_app/SERVICES/Outsourcing.html')
def Service_Non_Resident(request):
    return render(request,'CA_app/SERVICES/Service_Non_Resident.html')


def chat(request):
    return render(request,'CA_app/CHAT_BOX/chat.html')


def all_business(request):
    return render(request,'CA_app/START_A_BUSINESS/all_businesses/all_busness.html')


# dynamic news views

# def news(request):
#   title = 'Is GST number mandatory for MSME registration?'
#     discription='Having PAN & GST number is mandatory from 01.04. 2021. Those who have EM-II or UAM registration or any other registration ...'
#
#     context={
#
#             'title':title,
#             'discription':discription
#     }
#
#     return render(request,'CA_app/index.html',context)



def news(request):
    all_news=Headline.objects.all()
    return render(request,'CA_app/news.html',context={'news':all_news})


# def news(request):
#     if  request.method=="POST":
#         title=request.POST.get('title')
#         images=request.POST.get('image')
#         url=request.POST.get('url')
#
#         Headline(title=title,images=images,url=url).save()
#
#         return render(request, 'CA_app/index.html')
#     else:
#         return render(request, 'CA_app/news.html)


#registration views
def registration(request):
    return render(request,'CA_app/REGISTRATIONS/All_registration.html')


#tax_filing
def tax_filing(request):
    return render(request,'CA_app/TAX_FILING/Tax_filing_home/Tax_filing.html')


def hide(request):
    return render(request,'CA_app/hide.html')


def Request_form(request):


    return render(request,'CA_app/index.html')