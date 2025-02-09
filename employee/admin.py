from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import EmployProfile

# Employ Profile Admin
@admin.register(EmployProfile)
class EmployProfileAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "email",
        "phone_number",
        "total_experience",
    )
    search_fields = ("name", "email", "phone_number")
    list_filter = ("total_experience",)
    readonly_fields = ("slug",)