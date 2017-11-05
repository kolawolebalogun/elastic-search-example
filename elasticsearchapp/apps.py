from django.apps import AppConfig


class ElasticsearchappConfig(AppConfig):
    name = 'elasticsearchapp'

    def ready(self):
        from elasticsearchapp.util.util import run
        run()
