from django.apps import AppConfig


class AHputAppConfig(AppConfig):
    name = 'ahput'
    verbose_name = 'AHput'

    def ready(self):
        import ahput.signals #noqa: F401
