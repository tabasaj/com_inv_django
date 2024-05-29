from django.contrib import admin
from .models import Program, Project, MOD


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "caption", "date_time", "archive", "image_upload")


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "caption", "date_time", "archive", "image_upload")


class DonationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "donated",
        "donation_type",
        "name",
        "gcash_number",
        "paymaya_number",
        "contact_number",
        "amount",
        "address_volunteer",
        "date_sched",
        "date_time",
    )


admin.site.register(Program, ProgramAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MOD, DonationAdmin)
