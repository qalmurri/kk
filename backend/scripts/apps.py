from django.apps import AppConfig


class ScriptsConfig(AppConfig):
    name = 'scripts'

    def ready(self):
        import scripts.migrate
        import scripts.signals