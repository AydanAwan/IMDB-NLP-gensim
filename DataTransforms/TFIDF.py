"""transforms teh corpus into their tf-idf values."""


from gensim.models import TfidfModel


class TFIDF:

    def __init__(self, corpus):
        self.corpus = corpus

    def Caltfidf(self):
        tfidfmatrix = []
        model = TfidfModel(self.corpus)
        for i in self.corpus:
            tfidfmatrix.append(model[i])
        return tfidfmatrix
