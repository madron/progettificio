from django.contrib import admin


class AdminSite(admin.sites.AdminSite):
    site_header = 'Progettificio'
    site_title = 'Progettificio'
    index_title = 'Gestione'


site = AdminSite()


# association
from association import admin as association_admin
from association import models as association_models
site.register(association_models.Member, association_admin.MemberAdmin)
site.register(association_models.ProvisionalMember, association_admin.ProvisionalMemberAdmin)
