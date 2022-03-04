"""method to find how many of the largest singular values we should use."""


from gensim import matutils
import numpy
import matplotlib.pyplot as plt


class NumberOfTopics:

    def __init__(self, corpus, dictsize):
        self.corpus = corpus
        self.dictsize = dictsize

    def CalNumOTop(self):
        numpy_matrix = matutils.corpus2dense(self.corpus, num_terms=self.dictsize)
        s = numpy.linalg.svd(numpy_matrix, full_matrices=False, compute_uv=False)
        plt.figure(figsize=(10, 5))
        plt.hist(s, bins=100)
        plt.xlabel('Singular values', fontsize=12)
        plt.show()
