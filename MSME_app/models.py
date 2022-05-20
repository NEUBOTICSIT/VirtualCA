from django.db import models
# from phone_field import PhoneField
# # Create your models here.
#
#       # step1
#
# class msme_registration(models.Model):
#         NameofEntrepreneur=models.CharField(max_length=200)
#         mobile = PhoneField(blank=True, help_text='Contact phone number')
#         email = models.EmailField(max_length=100)
#
#
#       #radio button
#
#         SocialCategory = (
#             ('General', 'General'),
#             ('SC', 'SC'),
#             ('ST', 'ST'),
#             ('OBC', 'OBC'),
#         )
#         social_cat = models.CharField(max_length=7, choices=SocialCategory)
#
#
#         Gender = (
#             ('M', 'Male'),
#             ('F', 'Female'),
#         )
#
#         gender_option = models.CharField(max_length=1, choices=Gender)
#
#         SpeciallyAbled = (
#             ('Y', 'Yes'),
#             ('N', 'No'),
#         )
#         SpeciallyAbled_option = models.CharField(max_length=1, choices=SpeciallyAbled)
#
#         def __str__(self):
#             return self.NameofEntrepreneur
#
#
#
#     # step2
#
#         NameofEnterprise = models.CharField(max_length=100)
#         Plant_UnitName=models.CharField(max_length=100)
#
#         Location_of_Plant = (
#             ('one', 'one'),
#             ('two', 'two')
#         )
#         Location_of_Plant_option = models.CharField(max_length=3, choices=Location_of_Plant)
#
#         Flat=models.IntegerField()
#         Building = models.CharField(max_length=100)
#         Village = models.CharField(max_length=200)
#         Block = models.CharField(max_length=200)
#         Street = models.CharField(max_length=200)
#         City = models.CharField(max_length=100)
#         Pin = models.CharField(("zip code"), max_length=6, default="437012")
#
#
#
#         State = models.CharField(max_length=50,blank=True, null=True)
#
#         District = models.CharField(max_length=50)
#
#
#
#
#
#     # step3
#
#         Previous_EMII = (
#             ('N/A', 'N/A'),
#             ('EM-II', 'EM-II'),
#             ('Previous UAM', 'Previous UAM'),
#         )
#         Previous_EMII_option = models.CharField(max_length=13, choices=Previous_EMII)
#
#         Date_of_Incorporation = models.DateTimeField(blank=True, null=True)
#         Whether_production = models.CharField(max_length=100)
#
#         Major_Activity_of_Unit = (
#             ('Manufacturing', 'Manufacturing'),
#             ('Services', 'Services'),
#         )
#         Major_Activity_of_Unit_option = models.CharField(max_length=13, choices=Major_Activity_of_Unit)
#
#
#
#
#
#
#     # step4
#
#
#         Search_NIC_Code=models.CharField(max_length=30)
#
#         activities = (
#             ('Manufacturing', 'Manufacturing'),
#             ('NIC 4 Digit Code', 'NIC 4 Digit Code'),
#             ('NIC 5 Digit Code', 'NIC 5 Digit Code'),
#         )
#         activities_option = models.CharField(max_length=16, choices=activities)
#
#         NIC2_DigitCode = (
#             ('option1', 'option1'),
#             ('option2', 'option2'),
#         )
#         NIC2_DigitCode_option = models.CharField(max_length=7, choices=NIC2_DigitCode)
#
#
#
#         NIC4_DigitCode = (
#             ('option1', 'option1'),
#             ('option2', 'option2'),
#
#         )
#         NIC4_DigitCode_option = models.CharField(max_length=7, choices=NIC4_DigitCode)
#
#
#
#         NIC5_DigitCode = (
#             ('option1', 'option1'),
#             ('option2', 'option2'),
#
#         )
#         NIC5_DigitCode_option = models.CharField(max_length=7, choices=NIC5_DigitCode)
#
#         Numberof_persons_employed_Male=models.IntegerField(blank=True, null=True)
#         Numberof_persons_employed_Female = models.IntegerField(blank=True, null=True)
#         Numberof_persons_employed_District= models.IntegerField(blank=True, null=True)
#         Numberof_persons_employed_Total= models.IntegerField(blank=True, null=True)
#
#
#         Written_Down_Value=models.IntegerField()
#         Exclusion_of_cost=models.IntegerField()
#         Net_Investment_Plant=models.IntegerField()
#
#         Total_Turnover_A=models.IntegerField()
#         Export_Turnover_B=models.IntegerField()
#         Net_Turnover_AB=models.IntegerField()
#
#
#         Government_e_Market= (
#             ('Yes', 'Yes'),
#             ('No', 'No'),
#
#         )
#         Government_e_Market_option = models.CharField(max_length=3, choices=Government_e_Market)
#
#
#
#         TReDS_Portals = (
#             ('Yes', 'Yes'),
#             ('No', 'No'),
#
#         )
#         TReDS_Portals_option = models.CharField(max_length=3, choices=TReDS_Portals)
#
#
#
#         District_Industries= (
#             ('Yes', 'Yes'),
#             ('No', 'No'),
#         )
#         District_Industries_option = models.CharField(max_length=3, choices=District_Industries)


# Table for NIC code


# Table for NIC code################################################################################################
# Table for Manufacturing NIC code################################################################################################

class Manufacturing_2DG(models.Model):
    m2_code = models.IntegerField(primary_key=True, unique=True)

    m2_name = models.CharField(max_length=500)

    def __str__(self):
        return self.m2_name


class Manufacturing_4DG(models.Model):
    m4_code = models.IntegerField(primary_key=True, unique=True)

    m4_name = models.CharField(max_length=600)
    m2_code = models.ForeignKey(
        Manufacturing_2DG, to_field='m2_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.m4_name


class Manufacturing_5DG(models.Model):
    m5_code = models.IntegerField(primary_key=True, unique=True)

    m5_name = models.CharField(max_length=600)
    m2_code = models.ForeignKey(
        Manufacturing_2DG, to_field='m2_code', on_delete=models.CASCADE)
    m4_code = models.ForeignKey(
        Manufacturing_4DG, to_field='m4_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.m5_name

    # Table for Services NIC code################################################################################################


class services_2DG(models.Model):

    s2_code = models.IntegerField(primary_key=True, unique=True)

    s2_name = models.CharField(max_length=500)

    def __str__(self):
        return self.s2_name


class services_4DG(models.Model):
    s4_code = models.IntegerField(primary_key=True, unique=True)

    s4_name = models.CharField(max_length=600)
    s2_code = models.ForeignKey(
        services_2DG, to_field='s2_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.s4_name


class services_5DG(models.Model):
    s5_code = models.IntegerField(primary_key=True, unique=True)

    s5_name = models.CharField(max_length=600)
    s2_code = models.ForeignKey(
        services_2DG, to_field='s2_code', on_delete=models.CASCADE)
    s4_code = models.ForeignKey(
        services_4DG, to_field='s4_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.s5_name

    # Table for Trading NIC code################################################################################################


class Trading_2DG(models.Model):

    t2_code = models.IntegerField(primary_key=True, unique=True)

    t2_name = models.CharField(max_length=500)

    def __str__(self):
        return self.t2_name


class Trading_4DG(models.Model):
    t4_code = models.IntegerField(primary_key=True, unique=True)

    t4_name = models.CharField(max_length=600)
    t2_code = models.ForeignKey(
        Trading_2DG, to_field='t2_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.t4_name


class Trading_5DG(models.Model):
    t5_code = models.IntegerField(primary_key=True, unique=True)

    t5_name = models.CharField(max_length=600)
    t2_code = models.ForeignKey(
        Trading_2DG, to_field='t2_code', on_delete=models.CASCADE)
    t4_code = models.ForeignKey(
        Trading_4DG, to_field='t4_code', on_delete=models.CASCADE)

    def __str__(self):
        return self.t5_name
