from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from GST_app.models import Member


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("firstname", "lastname", "email", "birth_date")
    pass



