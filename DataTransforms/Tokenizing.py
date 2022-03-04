"""methods for tokenizing the data."""


import nltk.tokenize


class tokenizing:
    def __init__(self, rawdata):
        self.rawdata = rawdata

    def nltktokenize(self):
        return nltk.word_tokenize(self.rawdata)
