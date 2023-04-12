from PyDictionary import PyDictionary

# dictionary = PyDictionary()

def handle(word):
    words = word.split(" ")
    word1 = words[0]
    word2 = words[1]
    dictionary = PyDictionary(word1, word2)
    return dictionary.translateTo("es")


#
# if __name__ == '__main__':
#     handle("gold retriever")
