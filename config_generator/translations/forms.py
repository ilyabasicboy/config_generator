from django.core.validators import FileExtensionValidator
from django import forms
from config_generator.translations.models import ImportTranslation, Language


class ImportTranslationForm(forms.ModelForm):

    class Meta:
        model = ImportTranslation
        fields = '__all__'

    file = forms.FileField(
        label=u'Import translations file',
        validators=[FileExtensionValidator(allowed_extensions=['strings'])]
    )


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'
