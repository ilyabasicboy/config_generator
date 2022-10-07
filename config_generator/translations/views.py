from config_generator.translations.forms import ImportTranslationForm
from config_generator.translations.models import Language, Key
from django.shortcuts import render
from config_generator.translations.utils import get_keys_from_translation
from django.db.utils import IntegrityError
import re


def import_translation(self, request):

    success = False
    logs = []

    if request.method == 'POST':
        form = ImportTranslationForm(request.POST,  request.FILES)
        if form.is_valid():
            language_id = request.POST.get('language', None)
            language = Language.objects.filter(id=language_id).first()
            file = request.FILES.get('file')
            if file:
                keys = get_keys_from_translation(file)
            else:
                keys = []

            if keys:
                for key in keys:
                    try:
                        Key.objects.create(
                            language=language,
                            title=key
                        )
                    except IntegrityError:
                        logs += ['key "%s" already exists.' % key]
                success = True
        else:
            logs += [form.errors]
    else:
        form = ImportTranslationForm()

    context = {
        'form': form,
        'success': success,
        'logs': logs
    }
    return render(request, 'admin/translations/importtranslation/change_list.html', context)
