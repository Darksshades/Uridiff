import urllib3
from lxml import etree
import logging

logger = logging.getLogger('info')

from uridiff.data.models import Question

NUM_SOCKETS = 3

class Crawler(object):
    isFinished = False
    http = urllib3.PoolManager(maxsize=NUM_SOCKETS)

    def update_questions(self, npages = 99, startPage = 1, once = False):
        page = startPage
        endPage = page+npages



        link = "http://www.urionlinejudge.com.br/judge/en/problems/all/sort:"\
                "id/direction:desc/page:"+str(page)

        self.proc_question(link)

    def proc_solved(self, url, aluno=None):
      pass


    def proc_question(self, url):
        r = self.http.request('GET', url)
        html = etree.HTML(r.data)
        tr_nodes = html.xpath('//div[@id="element"]/table/tbody')

        if len(tr_nodes) <= 0:
            return

        content_nodes = tr_nodes[0].xpath("tr")
        header = [i[0][0].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        name = [i[2][0].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        classe = [i[3][0].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        solved = [i[4].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]
        level = [i[5].text for i in tr_nodes[0].xpath("tr") if len(i) > 1]

        for i, head in enumerate(header):
            q = Question(id=head, level=level[i], solved=solved[i].strip(),
                         category=classe[i], name=name[i])
            q.save()
