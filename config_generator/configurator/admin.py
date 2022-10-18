from django.contrib import admin
from config_generator.configurator.models import WhiteLabel, WhiteLabelConfig
from config_generator.translations.admin import CustomTranslationInline





@admin.register(WhiteLabelConfig)
class WhiteLabelConfigAdmin(admin.ModelAdmin):

    inlines = [CustomTranslationInline]


@admin.register(WhiteLabel)
class WhiteLabelAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}
