from django.apps import AppConfig


class ConfiguratorConfig(AppConfig):
    name = 'config_generator.configurator'

    def ready(self):
        super(ConfiguratorConfig, self).ready()
        import config_generator.configurator.signals