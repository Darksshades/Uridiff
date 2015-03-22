from django.db import models
from datetime import datetime

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
    avatar_url = models.CharField(max_length=128, blank=True)
    position = models.IntegerField(default=0)

    def get_url(self):
        url = "https://www.urionlinejudge.com.br/judge/pt/profile/{}".format(self.id)
        return url

    def __unicode__(self):
      return u'%i - %s' % (self.id, self.name)


class QuestionUsers(models.Model):
    user = models.ForeignKey(UriUser, related_name='questions')
    question = models.ForeignKey(Question, related_name='users')
    submission_date = models.DateTimeField(auto_now_add=True, blank=True)
    id = models.IntegerField(primary_key=True)

    def __unicode__(self):
      return u'%i: %s - %s' % (self.id, self.user.name, self.question.name)
