# -*- coding: utf-8 -*-
from english import ENGLISH_WORDS

def listAnagrams(letters):
    ordered = sortLetters(letters)
    
    for words in ENGLISH_WORDS:
        test = sortLetters(words)
        if test == ordered:
            print(words)
            
def sortLetters(letters):
    chs = list(letters)
    chs.sort()
    return chs 
              
                             
            
    '''
    if isEnglishWord(letters):
        anagrams.append(letters)
    for i in range(len(letters)):
        
        ch = letters[i]
        rem = letters[:i] + letters[i+1:]
        for i in range(len(rem)):
          test = rem[:i] + ch + rem[i:]
          #print(test)
          if test not in anagrams:
              if isEnglishWord(test):
                  anagrams.append(letters)
                  '''
    
   
