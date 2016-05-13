from django.conf.urls import url
from django.contrib import admin
from . import models
from . import views


class MemberAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name')
    fieldsets = (
        (None, {'fields': ('surname', 'name')}),
    )
    search_fields = ('surname', 'name')

    def get_urls(self):
        info = dict(app_label=self.model._meta.app_label, model_name=self.model._meta.model_name)
        request_name = '{app_label}_{model_name}_request'.format(**info)
        urls = [
            url(
                r'^(?P<pk>[0-9]+)/request/$',
                self.admin_site.admin_view(views.MembershipRequestModule.as_view()),
                name=request_name
            ),
        ]
        return urls + super(MemberAdmin, self).get_urls()


admin.site.register(models.Member, MemberAdmin)
