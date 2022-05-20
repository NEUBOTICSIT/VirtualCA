from django.shortcuts import render,redirect
# from MSME_app.models import msme_registration

# Create your views here.



def msme_about(request):
    return render(request,'MSME_app/msme_about.html')

#
# def msme_home(request):
#     return render(request,'MSME_app/msme_home.html')

def msme_reg(request):
    # if  request.method=="POST":
    #     NameofEntrepreneur=request.POST.get('NameofEntrepreneur')
    #     mobile = request.POST.get('mobile')
    #     email = request.POST.get('email')
    #     social_cat=request.POST.get('social_cat')
    #     gender_option=request.POST.get('gender_option')
    #     SpeciallyAbled_option = request.POST.get('SpeciallyAbled_option')
    #
    #     NameofEnterprise = request.POST.get('NameofEnterprise')
    #     Plant_UnitName = request.POST.get('Plant_UnitName')
    #     Location_of_Plant_option = request.POST.get('Location_of_Plant_option')
    #     Flat = request.POST.get('Flat')
    #     Building = request.POST.get('Building')
    #     Village = request.POST.get('Village')
    #     Block = request.POST.get('Block')
    #     Street = request.POST.get('Street')
    #     City = request.POST.get('City')
    #     Pin = request.POST.get('Pin')
    #
    #     State = request.POST.get('State')
    #     District = request.POST.get('District')
    #     Previous_EMII_option = request.POST.get('Previous_EMII_option')
    #     Date_of_Incorporation = request.POST.get('Date_of_Incorporation')
    #     Whether_production = request.POST.get('Whether_production')
    #     Major_Activity_of_Unit_option = request.POST.get('Major_Activity_of_Unit_option')
    #
    #     Search_NIC_Code = request.POST.get('Search_NIC_Code')
    #     activities_option=request.POST.get('activities_option')
    #     NIC2_DigitCode_option = request.POST.get('NIC2_DigitCode_option')
    #     NIC4_DigitCode_option = request.POST.get('NIC4_DigitCode_option')
    #     NIC5_DigitCode_option = request.POST.get('NIC5_DigitCode_option')
    #
    #     Numberof_persons_employed_Male = request.POST.get('Numberof_persons_employed_Male')
    #     Numberof_persons_employed_Female = request.POST.get('Numberof_persons_employed_Female')
    #     Numberof_persons_employed_District = request.POST.get('Numberof_persons_employed_District')
    #     Numberof_persons_employed_Total = request.POST.get('Numberof_persons_employed_Total')
    #
    #     Written_Down_Value = request.POST.get('Written_Down_Value')
    #     Exclusion_of_cost = request.POST.get('Exclusion_of_cost')
    #     Net_Investment_Plant = request.POST.get('Net_Investment_Plant')
    #     Total_Turnover_A = request.POST.get('Total_Turnover_A')
    #
    #     Export_Turnover_B = request.POST.get('Export_Turnover_B')
    #     Net_Turnover_AB = request.POST.get('Net_Turnover_AB')
    #
    #     Government_e_Market_option = request.POST.get('Government_e_Market_option')
    #     TReDS_Portals_option = request.POST.get('TReDS_Portals_option')
    #     District_Industries_option = request.POST.get('District_Industries_option')
    #
    #
    #     msme_registration(NameofEntrepreneur=NameofEntrepreneur,mobile=mobile,social_cat=social_cat,gender_option=gender_option
    #     ,SpeciallyAbled_option=SpeciallyAbled_option,NameofEnterprise=NameofEnterprise,Plant_UnitName=Plant_UnitName,
    #      Location_of_Plant_option=Location_of_Plant_option,Flat=Flat,Building=Building, Village = Village,Block =Block,
    #      Street = Street, City = City,Pin = Pin,State = State,District = District,
    #     Previous_EMII_option = Previous_EMII_option, Date_of_Incorporation = Date_of_Incorporation,Major_Activity_of_Unit_option=Major_Activity_of_Unit_option,
    #     Whether_production =Whether_production,Search_NIC_Code = Search_NIC_Code, NIC2_DigitCode_option = NIC2_DigitCode_option,
    #     NIC4_DigitCode_option = NIC4_DigitCode_option,
    #     NIC5_DigitCode_option = NIC5_DigitCode_option,
    #     Numberof_persons_employed_Male = Numberof_persons_employed_Male,
    #     Numberof_persons_employed_Female =Numberof_persons_employed_Female,
    #     Numberof_persons_employed_District = Numberof_persons_employed_District,
    #     Numberof_persons_employed_Total = Numberof_persons_employed_Total,
    #
    #     Written_Down_Value = Written_Down_Value,
    #     Exclusion_of_cost = Exclusion_of_cost,
    #     Net_Investment_Plant = Net_Investment_Plant,
    #     Total_Turnover_A = Total_Turnover_A,
    #     Export_Turnover_B = Export_Turnover_B,
    #     Net_Turnover_AB = Net_Turnover_AB,
    #     Government_e_Market_option = Government_e_Market_option,
    #     TReDS_Portals_option = TReDS_Portals_option,
    #     District_Industries_option = District_Industries_option).save()
    #     return redirect('/msme_about')
    # else:
        return render(request,'MSME_app/msme_reg_stepper.html')



def aadhaar(request):
    return render(request,'MSME_app/Aadhaar.html')

def msme_demo(request):
    return render(request,'MSME_app/BASECODE/msme_demo.html')



    #MSME_reg_process_views

def reg1(request):
    return render(request, 'MSME_app/MSME_reg_process/reg1.html')


def reg2(request):
    return render(request,'MSME_app/MSME_reg_process/reg2.html')


def reg3(request):
    return render(request,'MSME_app/MSME_reg_process/reg3.html')


def reg4(request):
    return render(request,'MSME_app/MSME_reg_process/reg4.html')


def msme_FAQ(request):
    return render(request,'MSME_app/FAQ.html')

 # stepperTab views

def msme_tab(request):


    return render(request,'MSME_app/MSME_StepperTab/msme_stepper.html')


#modalbox views

def modal(request):
    return render(request,'MSME_app/MSME_modalbox/msme_modalbox.html')



#payment views

def pay(request):
    return render(request,'MSME_app/payments/payment.html')


def tab_demo(request):
    return render(request,'MSME_app/MSME_StepperTab/stepperdemo.html')


def vca_contact(request):
    return render(request,'MSME_app/vca_contact.html')


def stepper(request):
   
    return render(request,'MSME_app/stepper.html')