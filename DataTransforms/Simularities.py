"""method for calculating the simularity abetween synopses."""


import numpy


class Simularities:

    def __init__(self, tfidfvalues, lsamodel, index, titles):
        self.corpus_tfidf = tfidfvalues
        self.lsi = lsamodel
        self.index = index
        self.movie = titles

    def Calsim(self):
        total_sims = []  # storage of all similarity vectors to analysis
        thershold = 0.4
        recomendations = []
        for i, doc in enumerate(self.corpus_tfidf):
            vec_lsi = self.lsi[doc]  # convert the vector to LSI space
            sims = self.index[vec_lsi]  # perform a similarity vector against the corpus
            total_sims = numpy.concatenate([total_sims, sims])
            similarity = []  # Create a list with movie_id and similarity value
            for j, x in enumerate(enumerate(self.movie)):
                if sims[j] > thershold:
                    similarity.append((x, sims[j]))
            similarity = sorted(similarity, key=lambda item: -item[1])
            recomendations.append([self.movie[i], similarity])
        return recomendations
