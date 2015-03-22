from django.core.management.base import BaseCommand

from uridiff.data.crawler import Crawler

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        pages = kwargs.get('pages') or int(args[0])
        print pages
        crawler = Crawler()
        crawler.update_questions(pages)