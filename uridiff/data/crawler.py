import urllib3
import logging
from lxml import etree
from Queue import Queue
from threading import Thread

from uridiff.data.models import Question, UriUser


logger = logging.getLogger('info')

NUM_SOCKETS = 3
NUM_WORKERS = 5

class Crawler(object):
    isFinished = False
    http = urllib3.PoolManager(maxsize=NUM_SOCKETS)

    def update_questions(self, npages=99, startPage=1, once=False):
        page = startPage
        endPage = page+npages

        while(True):

            link = "http://www.urionlinejudge.com.br/judge/en/problems/all/"\
              "sort:id/direction:desc/page:"+str(page)

            self.proc_question(link)

            if(once):
                break

            page += 1

            if(page >= endPage):
                break

    def compare_user(self, user_a, user_b):
      pass


    def proc_solved(self, url, aluno=None):
      pass


    def proc_question(self, url, aluno=False):
        if self.isFinished:
            logger.info("Unkown page processed.")
            return

        r = self.http.request('GET', url)
        html = etree.HTML(r.data)
        tr_nodes = html.xpath('//div[@id="element"]/table/tbody')

        if len(tr_nodes) <= 0:
            self.isFinished = True

        content_nodes = tr_nodes[0].xpath("tr")
        header = [i[0][0].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        name = [i[2][0].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        classe = [i[3][0].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        solved = [i[4].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        level = [i[5].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]

        for i, head in enumerate(header):
            if aluno:
              aluno.questions.add(header)
            else:
              q = Question(id=head, level=level[i], solved=solved[i].strip(),
                           category=classe[i], name=name[i])
              q.save()

        logger.info("Done: " + url)
