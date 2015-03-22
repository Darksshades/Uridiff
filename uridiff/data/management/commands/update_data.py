from django.core.management.base import BaseCommand

from uridiff.data.crawler import Crawler

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        crawler = Crawler()
        crawler.update_questions(1)