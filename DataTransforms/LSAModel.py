"""method for turning our dictionary and the valuematrix into an lsa model using different amounts of topics and calculating their coherence."""


from gensim.models import LsiModel
from gensim import similarities


class LSAModel:

    def __init__(self, dictionary, valuematrix, cleaneddoc, stop, start, step):
        self.dictionary = dictionary
        self.valuematrix = valuematrix
        self.cleaneddata = cleaneddoc
        self.stop = stop
        self.start = start
        self.step = step

    def CalCoherances(self):

        model = LsiModel(self.valuematrix, id2word=self.dictionary, num_topics=10)
        index = similarities.MatrixSimilarity(model[self.valuematrix])
        return model, index
