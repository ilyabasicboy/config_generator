from django.db import models
from config_generator.configurator.models import WhiteLabelConfig


class ImportTranslation(models.Model):
    class Meta:
        verbose_name = u"Import translation"
        verbose_name_plural = verbose_name

    language = models.ForeignKey(
        'Language',
        verbose_name=u'language',
        on_delete=models.CASCADE
    )


class Language(models.Model):
    class Meta:
        verbose_name = u'Language'
        verbose_name_plural = u'Languages'

    title = models.CharField(
        verbose_name=u'name of language',
        unique=True,
        max_length=255,

    )

    def __str__(self):
        return self.title


class Key(models.Model):
    class Meta:
        verbose_name = u"Translation key"
        verbose_name_plural = u'Translation keys'
        unique_together = ['language', 'title']

    language = models.ForeignKey(
        Language,
        verbose_name=u'Language',
        on_delete=models.CASCADE
    )
    title = models.TextField(
        verbose_name=u'Key'
    )

    def __str__(self):
        return self.title


class CustomTranslation(models.Model):
    class Meta:
        verbose_name = u"Custom translation"
        verbose_name_plural = u'Custom translations'
        unique_together = ['language', 'key', 'config']

    language = models.ForeignKey(
        Language,
        verbose_name=u'Language',
        on_delete=models.CASCADE
    )
    key = models.ForeignKey(
        Key,
        verbose_name=u'key',
        on_delete=models.CASCADE
    )
    value = models.CharField(
        verbose_name=u'Value',
        max_length=255
    )

    config = models.ForeignKey(
        WhiteLabelConfig,
        on_delete=models.CASCADE
    )
