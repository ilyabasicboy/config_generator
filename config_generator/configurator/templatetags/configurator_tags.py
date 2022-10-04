from django import template
from config_generator.configurator.forms import WhiteLabelForm, WhiteLabelConfigForm
register = template.Library()


@register.inclusion_tag('configurator/includes/create_app_form.html')
def show_create_app_form():
    return {'form': WhiteLabelForm()}\


@register.inclusion_tag('configurator/includes/create_config_form.html')
def show_create_config_form(app=None):
    return {'form': WhiteLabelConfigForm(), 'app':app}