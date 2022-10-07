from django.contrib import admin
from config_generator.configurator.models import WhiteLabel, WhiteLabelConfig
from config_generator.translations.models import CustomTranslation


class CustomTranslationInline(admin.TabularInline):
    model = CustomTranslation


@admin.register(WhiteLabelConfig)
class WhiteLabelConfigAdmin(admin.ModelAdmin):
    inlines = [CustomTranslationInline]


admin.site.register(WhiteLabel)
