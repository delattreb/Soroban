"""
soraban.py v 1.0.0
Autor: Bruno
Date : 29/08/2017
"""
import random


class Soroban:
    def __init__(self):
        pass
    
    def addition(self):
        taillenb = 3
        strnb = ''
        nblist = []
        for i in range(0, 10):
            strnb = ''
            for i in range(0, taillenb):
                if i == 0:
                   strnb += str(random.randrange(1, 10))
                else:
                    strnb += str(random.randrange(0, 10))
            nblist.append(strnb)
        
        taillenb = 2
        for i in range(0, 5):
            strnb = ''
            for i in range(0, taillenb):
                if i == 0:
                    strnb += str(random.randrange(1, 10))
                else:
                   strnb += str(random.randrange(0, 10))
            nblist.append(strnb)
        
        random.shuffle(nblist)
        
        return nblist
