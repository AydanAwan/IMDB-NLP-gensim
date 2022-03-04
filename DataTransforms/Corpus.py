"""method for creating the corpus."""

from gensim import corpora


class Corpus:

    def __init__(self, cleanData):
        self.cleandata = cleanData

    def GetCorpus(self):
        dictionary = corpora.Dictionary(self.cleandata)
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in self.cleandata]
        return dictionary, doc_term_matrix
