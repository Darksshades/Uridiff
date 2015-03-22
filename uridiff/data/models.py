from django.db import models

class Question(models.Model):

    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    solved = models.CharField(max_length=10, blank=True)
    level = models.IntegerField(default=1)

    def get_url(self):
        url = "https://www.urionlinejudge.com.br/judge/pt/problems/view/{}".format(self.id)
        return url


class UriUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
