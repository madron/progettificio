from django.contrib import admin
from . import models


class MemberAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')
    fieldsets = (
        (None, {'fields': ('surname', 'name')}),
    )
    search_fields = ('surname', 'name')


admin.site.register(models.Member, MemberAdmin)
