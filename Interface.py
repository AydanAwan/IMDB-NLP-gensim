"""an interface where we put all the methods together to make a full lsa model."""


from DataTransforms.Tokenizing import tokenizing
from DataTransforms.Cleaning import Cleaning
from DataTransforms.PullingData import PullingData
from DataTransforms.Corpus import Corpus
from DataTransforms.LSAModel import LSAModel
from DataTransforms.TFIDF import TFIDF
from DataTransforms.NumberOfTopics import NumberOfTopics
from DataTransforms.Simularities import Simularities


class Interface:

    titles, synopsRaw = PullingData(20).GetData()
    tokenedsynops = []
    for i in synopsRaw:
        tokenedsynops.append(tokenizing(i).nltktokenize())
    cleanedsyn = []
    for i in tokenedsynops:
        cleaned = Cleaning(i).DelNames()
        cleaned = Cleaning(cleaned).DelPunc()
        cleaned = Cleaning(cleaned).DelStop()
        cleanedsyn.append(cleaned)
    dictionary, corpusmatrix = Corpus(cleanedsyn).GetCorpus()
    tfidfmatrix = TFIDF(corpusmatrix).Caltfidf()
    topics = NumberOfTopics(tfidfmatrix, len(dictionary)).CalNumOTop()
    lsamodel, indexvalue = LSAModel(dictionary, tfidfmatrix, cleanedsyn, 10, 2, 1).CalCoherances()
    recomendations = Simularities(tfidfmatrix, lsamodel, indexvalue, titles).Calsim()
    print(recomendations)
