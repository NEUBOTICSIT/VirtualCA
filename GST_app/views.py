from django.shortcuts import render

# Create your views here.

def gst_home(request):
    return render(request,'GST_app/gst_about.html')

def gst_change(request):
    return render(request,'GST_app/gst_change.html')

def gst_cancel(request):
    return render(request,'GST_app/gst_cancel.html')

def reg(request):
    return render(request,'GST_app/gst_registration.html')







def accounting(request):
    return render(request,'GST_app/SERVICES/Accounting.html')


def Audit(request):
    return render(request,'CA_app/SERVICES/Audit.html')


def C_finance(request):
    return render(request,'GST_app/SERVICES/Corporate_Finance.html')


def C_service(request):
    return render(request,'GST_app/SERVICES/Corporate_Services.html')


def GST(request):
    return render(request,'CA_app/SERVICES/GST.html')


def income(request):
    return render(request,'GST_app/SERVICES/Income_Tax.html')


def international(request):
    return render(request,'GST_app/SERVICES/international_Services.html')


def outsourcing(request):
    return render(request,'GST_app/SERVICES/Outsourcing.html')


def payroll(request):
    return render(request,'GST_app/SERVICES/payroll.html')


def resident(request):
    return render(request,'GST_app/SERVICES/Service_Non_Resident.html')


def tds(request):
    return render(request,'GST_app/SERVICES/TDS.html')



def demo2(request):
    return render(request,'GST_app/demo2.html')