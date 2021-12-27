# -*- coding: utf-8 -*-
import random
SENTENCES = ["le chat mange le poisson", "le chien mange dans la cuisine", 
             "le chien mange le chat", "le chat est dans le chien", 
             "la cuisne est dans la maison", "le chat mange dans la maison"]

TRANSLATIONS = {"le" : {"the"}, 
                "chat" : {"cat"}, 
                "mange" : {"eats", "consumes"}, 
                "la": {"the"},
                "chien" : {"dog", "hound"},
                "dans" : {"in", "inside"},
                "est" : {"is"}, 
                "poisson" : {"fish"},
                "maison": {"house"}
                }

def reverse_tanslations(dictionary):
    result = dict()
    for key in dictionary:
        for value in dictionary[key]:
            if value not in result:
                result[value] = {key}
            else:
                result[value].add(key)
    return result

def back_translate(sent, dictionary):
    translate(sent, reverse_tanslations(dictionary))

"""
def back_translate(sent, dictionary):
    words = []
    for word in sent.split():
        for key in dictionary:
            if word in dictionary[key]:
                words.append(key)
    return " ".join(words)
    """
        

def translate(sent, dictionary):
    result = []
    for word in sent.split():
        if word in dictionary:
            possibles = dictionary[word]
            newword = random.choice(list(possibles))
        else:
            newword = word
        result.append(newword)
    return " ".join(result)

def get_words(sents):
    words = set()
    for sent in sents:
        for word in sent.split():
                words.append(word)
    return sorted(list(words))      
            

"""
def get_words(sents):
    words = []
    for sent in sents:
        for word in sent.split():
            if word not in words:
                words.append(word)
    return sorted(words) 
    """