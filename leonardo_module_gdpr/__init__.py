# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_module_gdpr.Config'


class Default(object):

    optgroup = 'GDPR'

    apps = [
        'leonardo_module_gdpr'
    ]

    widgets = [
        'leonardo_module_gdpr.widget.gdpr.models.GDPRWidget'
    ]

    config = {
        'GOOGLE_ANALYTICS_INFO':
        (True, u"Display google analytics info"),
    }

    public = True


class Config(AppConfig, Default):
    name = 'leonardo_module_gdpr'
    verbose_name = u"GDPR module"


default = Default()
