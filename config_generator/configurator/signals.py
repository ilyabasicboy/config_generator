# -*- encoding: utf-8 -*-
import os

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from config_generator.configurator.models import WhiteLabel
from django.conf import settings
import shutil
import zipfile
import tarfile


@receiver(post_save, sender=WhiteLabel)
def create_resources_directory(sender, instance, **kwargs):
    """ post save whitelabel resources logic """

    app_res_path = settings.MEDIA_ROOT + '/upload/whitelabels/%s/' % (instance.title)
    icons_path = app_res_path + 'icons'
    masks_path = app_res_path + 'masks'


    # Creating default resources folders

    if not os.path.exists(icons_path):
        shutil.copytree(settings.DEFAULT_ICONS_DIRECTORY, icons_path)

    if not os.path.exists(masks_path):
        shutil.copytree(settings.DEFAULT_MASKS_DIRECTORY, masks_path)

    if not os.path.exists(app_res_path + 'assets'):
        os.mkdir(app_res_path + 'assets')


    # Unpack custom resources

    if instance.icons:
        if (zipfile.is_zipfile(instance.icons) or tarfile.is_tarfile(instance.icons)):
            shutil.unpack_archive(instance.icons.path, icons_path)

        # Clear FileFields after unpacking
        instance.icons.storage.delete(instance.icons.name)
        instance.icons.delete()

    if instance.masks:
        if (zipfile.is_zipfile(instance.masks) or tarfile.is_tarfile(instance.masks)):
            shutil.unpack_archive(instance.masks.path, masks_path)

        instance.masks.storage.delete(instance.masks.name)
        instance.masks.delete()


@receiver(post_delete, sender=WhiteLabel)
def delete_resources(sender, instance, **kwargs):
    app_res_path = settings.MEDIA_ROOT + '/upload/whitelabels/%s/' % (instance.title)
    if os.path.exists(app_res_path):
        shutil.rmtree(app_res_path)
