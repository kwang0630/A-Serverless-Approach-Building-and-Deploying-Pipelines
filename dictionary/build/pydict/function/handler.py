from PyDictionary import PyDictionary
import json

# dictionary = PyDictionary()

def find_word(input):
    i = input.find("name")
    j = input.find(" ", i) + 1
    k = input.find("}", j) - 1
    word = input[j+1:k]
    return word


def handle(word):
    #
    str_words = find_word(word)
    words = str_words.split(" ")
    word1 = words[0]
    word2 = words[1]
    dictionary = PyDictionary(word1, word2)
    # print (dictionary.translateTo("es"))
    # print(dictionary.printMeanings())
    output = dictionary.getMeanings()
    # print(str_words)
    output = json.dumps(output)
    # print(type(output))
    # print(str_words + '\n' +output)
    output = str_words + ':' + output
    print(output)
    return output
    # print(dictionary.meaning(word))
    # return dictionary.meaning(word)



#
# if __name__ == '__main__':
#      handle('[{"score": 0.872933566570282, "name": "golden retriever"},')
#      intput = '[{"score": 0.872933566570282, "name": "golden retriever"},'

#     print(word)
#     handle(word)
