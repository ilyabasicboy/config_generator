from config_generator.translations.views import import_translation
from config_generator.translations.models import ImportTranslation, Key, CustomTranslation, Language
from config_generator.translations.forms import LanguageAdminForm
from django.contrib import admin


@admin.register(ImportTranslation)
class ImportAdmin(admin.ModelAdmin):
    changelist_view = import_translation

    def has_add_permission(self, request):
        return False


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):

    list_display = ['title', 'language']
    list_filter = ['language']
