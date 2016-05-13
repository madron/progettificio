from django.views.generic import DetailView
from . import models


class MembershipRequestModule(DetailView):
    model = models.Member
    template_name = 'association/membership_request_module.html'
