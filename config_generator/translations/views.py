from config_generator.translations.forms import ImportTranslationForm
from config_generator.translations.models import Language, Key
from config_generator.configurator.models import WhiteLabel
from django.shortcuts import render
from config_generator.translations.utils import get_keys_from_translation
from django.db.utils import IntegrityError
from django.http import Http404, JsonResponse


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


def get_translations(request, lang):
    if 'app' in request.GET:
        try:
            object = WhiteLabel.objects.get(slug=request.GET.get('app'))
        except WhiteLabel.DoesNotExist:
            raise Http404("WhiteLabel does not exist")
        try:
            language = Language.objects.get(title=lang)
        except Language.DoesNotExist:
            raise Http404("Language does not exist")

        if object.config:
            result = {}
            translations = object.config.customtranslation_set.filter(language=language)
            for trans in translations:
                result[trans.key.title] = trans.value
            return JsonResponse(result)
        else:
            raise Exception('WhiteLabel %s has no configuration' % object.title)
    else:
        raise Http404
