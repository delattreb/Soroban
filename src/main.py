"""
main.py v 1.0.0
Autor: Bruno
Date : 29/08/2017
"""

from soroban import Soroban


def writeToCSV(line):
    file = open('D:\\SOROBAN Exercice.csv', 'a+')
    file.write(line)
    file.write('\r')
    file.close()


nboperation = 10
nbitem = 15
nbsize = 3
soraban = Soroban(nbsize)
listeoperation = []

print('Start generation')
strline = ''
for e in range(0, nboperation):
    strline += 'N°' + str(e + 1) + ";"
writeToCSV(strline)

for i in range(0, nboperation):
    listeoperation.append(soraban.addition())

strline = ''
for j in range(0, 15):
    strline = ''
    for i in range(0, len(listeoperation)):
        #print(listeoperation[i][j] + ';', end = '', flush = True)
        strline += listeoperation[i][j] + ';'
    writeToCSV(strline)
writeToCSV ('\r')

print('Stop generation')
