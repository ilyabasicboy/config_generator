from django.contrib import admin

from config_generator.configurator.models import WhiteLabel, WhiteLabelConfig


admin.site.register(WhiteLabel)
admin.site.register(WhiteLabelConfig)