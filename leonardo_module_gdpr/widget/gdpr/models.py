# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo.utils import get_htmltext_widget


class GDPRWidget(Widget):

    domain_name = models.CharField("Domain name")
    company_name = models.CharField("Company name")
    email_address = models.CharField("Webmaster e-mail")
    resources = models.TextField(
        _('Resources for obtaining personal information '), blank=True, default="<p>%s</p>" % ('Empty element'))
    made_by = models.CharField("Made by with prefix")

    widgets = {
        'resources': get_htmltext_widget
    }

    class Meta:
        abstract = True
        verbose_name = 'GDPR'
        verbose_name_plural = 'GDPRs'
