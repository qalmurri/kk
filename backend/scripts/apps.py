from django.apps import AppConfig

class ScriptsConfig(AppConfig):
    name = 'scripts'

    def ready(self):
        import scripts.signals.log
        import scripts.signals.migrate