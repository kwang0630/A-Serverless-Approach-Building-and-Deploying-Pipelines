from PyDictionary import PyDictionary
from googletrans import Translator

translator = Translator()
# dictionary = PyDictionary()

def find_word(input):
    i = input.find(":")
    return input[:i]

def handle(word):
    str_words = find_word(word)
    # print(str_words)
    translated_text = translator.translate(str_words, dest="ja")
    # print(translated_text.text)
    return translated_text.text
    # words = str_words.split(" ")
    # word1 = words[0]
    # print(word1)
    # print(type(word1))
    # word2 = words[1]
    # print(word2)
    # print(type(word2))
    # print('1')
    # dictionary = PyDictionary("hi", word2)
    # print(dictionary.getMeanings())
    # print('2')
    # print(dictionary.translateTo("es"))
    # print('3')
    # return dictionary.getMeanings()
    # return dictionary.translateTo("es")


#
# if __name__ == '__main__':
#     handle('golden retriever:{"golden": {"Adjective": ["having the deep slightly brownish color ')
