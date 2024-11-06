from django.apps import AppConfig

class UserTasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usertasks'

    def ready(self):
        import usertasks.signals  # Імпортує файл signals, щоб сигнал спрацював
