from django.core.management.base import BaseCommand

import uridiff.data.crawler as crawler

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        crawler.parse_exs(1)