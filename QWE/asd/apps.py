from django.apps import AppConfig


class AsdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'asd'

    def ready(self) -> None:
        from asd import signals
