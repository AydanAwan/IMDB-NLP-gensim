"""testing for all the NLP methods."""


import unittest
from DataTransforms.Tokenizing import tokenizing
from DataTransforms.Cleaning import Cleaning


class TestMethods(unittest.TestCase):
    def test_tokenize(self):
        result = tokenizing("hello my name is aydan, what is yours? you're not from around here are you, I'm form here myself; raised in london town and i work as a programmer. i like being a programmer").nltktokenize()
        self.assertEqual(result, ['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', '.', 'i', 'like', 'being', 'a', 'programmer'])

    def test_removePunc(self):
        result = Cleaning(['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', '.', 'i', 'like', 'being', 'a', 'programmer']).DelPunc()
        self.assertEqual(result, ['hello', 'my', 'name', 'is', 'aydan', 'what', 'is', 'yours', 'you', 'not', 'from', 'around', 'here', 'are', 'you', 'i', 'form', 'here', 'myself', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', 'i', 'like', 'being', 'a', 'programmer'])

    def test_removeStop(self):
        result = Cleaning(['hello', 'my', 'name', 'is', 'aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'london', 'town', 'and', 'i', 'work', 'as', 'a', 'programmer', '.', 'i', 'like', 'being', 'a', 'programmer']).DelStop()
        self.assertEqual(result, ['hello', 'name', 'aydan', ',', '?', "'re", 'around', ',', 'I', "'m", 'form', ';', 'raised', 'london', 'town', 'work', 'programmer', '.', 'like', 'programmer'])

    def test_removeNames(self):
        result = Cleaning(['hello', 'my', 'name', 'is', 'Aydan', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'London', 'town', 'and', 'I', 'work', 'as', 'a', 'programmer', '.', 'I', 'like', 'being', 'a', 'programmer']).DelNames()
        self.assertEqual(result, ['hello', 'my', 'name', 'is', ',', 'what', 'is', 'yours', '?', 'you', "'re", 'not', 'from', 'around', 'here', 'are', 'you', ',', 'I', "'m", 'form', 'here', 'myself', ';', 'raised', 'in', 'London', 'town', 'and', 'I', 'work', 'as', 'a', 'programmer', '.', 'I', 'like', 'being', 'a', 'programmer'])


if __name__ == '__main__':
    unittest.main()
