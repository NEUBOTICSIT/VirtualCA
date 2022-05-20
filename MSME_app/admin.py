

from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

from MSME_app.models import Manufacturing_2DG, Manufacturing_4DG, Manufacturing_5DG, services_2DG, services_4DG, services_5DG, Trading_2DG, Trading_4DG, Trading_5DG

# Register your models here.
admin.site.register(Manufacturing_2DG)
admin.site.register(Manufacturing_4DG)
admin.site.register(Manufacturing_5DG)

admin.site.register(services_2DG)
admin.site.register(services_4DG)
admin.site.register(services_5DG)


admin.site.register(Trading_2DG)
admin.site.register(Trading_4DG)
admin.site.register(Trading_5DG)


# class udataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     ...
    
# admin.site.register(udataAdmin)
