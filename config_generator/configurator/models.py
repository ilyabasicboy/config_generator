import shutil
import uuid
from django.db import models
from config_generator.configurator.fields import CustomArrayField
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import os
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class WhiteLabel(models.Model):

    class Meta:
        verbose_name = u"whitelabel"
        verbose_name_plural = u"whitelabels"

    title = models.CharField(
        verbose_name=u'название приложения',
        max_length=255,
        unique=True
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=255,
        unique=True,
    )

    icons = models.FileField(
        verbose_name=u'Распаковать архив с иконками',
        upload_to='upload/files',
        null=True,
        blank=True
    )

    masks = models.FileField(
        verbose_name=u'Распаковать архив с масками',
        upload_to='upload/files',
        null=True,
        blank=True
    )

    config = models.ForeignKey(
        'WhiteLabelConfig',
        verbose_name=u'Конфигурация',
        related_name='whitelabel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        User,
        verbose_name=u'Пользователь',
        on_delete=models.CASCADE,
    )

    api_key = models.UUIDField(
        verbose_name=u'Ключ авторизации',
        default=uuid.uuid4,
        editable=False,
    )

    def __str__(self):
        return self.title

    def reset_api_key(self):
        self.api_key = uuid.uuid4()
        self.save()

    def get_config(self):
        return JsonResponse(model_to_dict(self.config)) if self.config else HttpResponse("Whitelabel %s has no configuration" % (self.title))

    def get_resources(self):
        zip_filename = "%s_media" % self.title
        app_res_path = settings.MEDIA_ROOT + '/upload/whitelabels/%s' % (self.title)
        path = shutil.make_archive('media/upload/files/%s' % zip_filename, 'zip', app_res_path)


        # Grab ZIP file from in-memory, make response with correct content type
        resp = HttpResponse(open(path, 'rb').read(), content_type="application/x-zip-compressed")
        resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename +'.zip'

        os.remove(path)

        return resp


class WhiteLabelConfig(models.Model):

    class Meta:
        verbose_name = u"Whitelabel config"
        verbose_name_plural = u"Whitelabel configs"

    bundle_id = models.CharField(
        verbose_name=u'id приложения в appstore',
        max_length=255,
        blank=True,
        null=True
    )

    push_bundle_id = models.CharField(
        verbose_name=u'id пуш экстеншена в appstore',
        max_length=255,
        blank=True,
        null=True
    )

    onboarding_subtitle_text = models.CharField(
        verbose_name=u'текст на стартовом экране онбординга под логотипом и названием клиента',
        max_length=255,
        blank=True,
        null=True,
    )

    app_name = models.CharField(
        verbose_name=u'название приложения',
        max_length=255,
    )

    version = models.CharField(
        verbose_name=u'версия',
        max_length=255,
    )

    domain = models.CharField(
        verbose_name=u'основной домен приложения',
        help_text='не xmpp хост, может не сопадать',
        max_length=255,
        blank=True,
        null=True,
    )

    allow_registration = models.BooleanField(
        verbose_name=u'разрешать регистрацию',
        default=False,
    )

    locked_host = models.CharField(
        verbose_name=u'xmpp хост, который нельзя изменить,'
                     u'на котором происходит регистрация'
                     u'и авторизация пользователя',
        help_text='если пустой -  доступны все из allowed_hosts',
        max_length=255,
        blank=True,
        null=True,
    )

    allowed_hosts = CustomArrayField(
        verbose_name=u'доступные для регистрации и авторизации xmpp хосты',
        help_text='Если пустой - доступны любые хосты. Значения разделить запятой.',
        blank=True,
        null=True,
    )

    supports_mulriaccounts = models.BooleanField(
        verbose_name=u'разрешать добавлять несколько аккаунтов',
        default=False,
    )

    required_touch_id_or_password = models.BooleanField(
        verbose_name=u'включить дополнительную защиту приложения пинкодом или отпечатком/лицом',
        default=False,
    )

    locked_conversation_type = models.CharField(
        verbose_name=u'принимать только чаты определенного типа',
        max_length=255,
        blank=True,
        null=True,
    )

    avatar_masks = CustomArrayField(
        verbose_name=u'маски для аватаров',
        help_text='Значения разделить запятой.',
        max_length=255,
        blank=True,
        null=True,
    )

    locked_avatar_mask = models.CharField(
        verbose_name=u'закрепленная маска для аватара',
        max_length=255,
        blank=True,
        null=True,
    )

    support_calls = models.BooleanField(
        verbose_name=u'поддержка звонков',
        default=False,
    )

    support_groupchats = models.BooleanField(
        verbose_name=u'поддержка групповых чатов',
        default=False,
    )

    allow_conversations_from_all_hosts = models.BooleanField(
        verbose_name=u'разрешать диалоги с любыми хостами',
        default=False,
    )

    application_color = models.CharField(
        verbose_name=u'основной цвет приложения',
        help_text='в hexadecimal формате, #ffffff',
        max_length=255,
        blank=True,
        null=True,
    )

    launch_screen_color = models.CharField(
        verbose_name=u'цвет стартового экрана',
        help_text='в hexadecimal формате, #ffffff',
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.app_name
