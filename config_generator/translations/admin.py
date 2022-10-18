from config_generator.translations.views import import_translation
from config_generator.translations.models import ImportTranslation, Key, CustomTranslation, Language
from config_generator.translations.forms import LanguageAdminForm
from django.contrib import admin


class CustomTranslationInline(admin.TabularInline):
    model = CustomTranslation

    def get_formset(self, request, obj=None, **kwargs):
     formset = super().get_formset(request, obj, **kwargs)
     field = formset.form.base_fields["key"]
     field.widget.can_add_related = False
     field.widget.can_change_related = False
     field.widget.can_delete_related = False
     return formset


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
