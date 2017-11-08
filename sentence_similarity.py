# coding:utf-8
from gensim.models.doc2vec import LabeledSentence
sentence = LabeledSentence(words=[u'some', u'words', u'here'], tags=[u'SENT_1'])


class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self,filename):
        for uid, line in enumerate(open(filename)):
            yield LabeledSentence(words=line.split(), labels=['SENT_%s' % uid])

from gensim.models import Doc2Vec
model = Doc2Vec(dm=1, size=100, window=5, negative=5, hs=0, min_count=2, workers=4)
