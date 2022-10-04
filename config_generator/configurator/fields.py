from django.db import models
import re


class CustomArrayField(models.TextField):

    def __init__(self,  *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(CustomArrayField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        if isinstance(value, str):
            value = [value.strip() for value in re.sub("\[|\]|\(|\)|\'|\"", "", value).split(self.token)]

        return value

    def from_db_value(self, value, *args):
        if not value:
            return []

        return value.split(',')

    def get_db_prep_value(self, value, connection, prepared=False):
        if not value:
            return
        if not prepared:
            value = self.get_prep_value(value)
        return self.token.join([str(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)