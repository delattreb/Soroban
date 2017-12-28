"""
soraban.py v 1.0.0
Autor: Bruno
Date : 29/08/2017
"""
import random


class Soroban:
    def addition(self, nbitem, level):
        nblist = []
        for i in range(0, nbitem):
            strnb = ''
            for i in range(0, level):
                if i == 0:
                    strnb += str(random.randrange(1, 10))
                else:
                    strnb += str(random.randrange(0, 10))
            nblist.append(strnb)
        return nblist

    def soustraction(self, nbsous, nbitem, level):
        nbsoustraction = nbsous
        nblist = []
        for i in range(0, nbitem):
            strnb = ''
            for i in range(0, level):
                if i == 0:
                    strnb += str(random.randrange(1, 10))
                else:
                    strnb += str(random.randrange(0, 10))
            nblist.append(strnb)

        for i in range(0, nbsoustraction):
            nblist[i] = '-' + nblist[i]
        random.shuffle(nblist)

        return nblist
