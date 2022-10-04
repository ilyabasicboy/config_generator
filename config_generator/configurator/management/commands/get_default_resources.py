# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
import shutil
from git import Repo
import os


class Command(BaseCommand):

    help = 'get or update default resources'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            type=str,
        )
        parser.add_argument(
            '--folder',
            type=str,
            help='download in specified folder'
        )

    def handle(self, *args, **options):
        if options['url']:
            url = options['url']
        else:
            raise Exception('missed required argument --url')

        path = settings.DEFAULT_RESOURCES_DIRECTORY

        if options['folder']:
            path += options['folder']
        else:
            raise Exception('missed required argument --folder')

        if os.path.exists(path):
            shutil.rmtree(path)

        Repo.clone_from(url, path)