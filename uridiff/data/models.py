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

    def __unicode__(self):
      return u'%i - %s' % (self.id, self.name)


class UriUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    questions = models.ManyToManyField(Question)
    avatar_url = models.CharField(max_length=128, blank=True)
    position = models.IntegerField(default=0)

    def get_url(self):
        url = "https://www.urionlinejudge.com.br/judge/pt/profile/{}".format(self.id)
        return url

    def __unicode__(self):
      return u'%i - %s' % (self.id, self.name)
