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


nboperation = 5
nbitem = 10
level = 3
nbsoustraction = 4
sorabano = Soroban()
listeoperation = []

print('Start generation')
strline = ''
# Generate title
for e in range(0, nboperation):
    strline += 'N°' + str(e + 1) + ";"
writeToCSV(strline)

# Generate operation
for i in range(0, nboperation):
    # listeoperation.append(sorabano.soustraction(nbsoustraction, nbitem, level)) #Adddition or soustraction
    listeoperation.append(sorabano.addition(nbitem, level))  # Adddition or soustraction

# generate csv file
strline = ''
for j in range(0, nbitem):
    strline = ''
    for i in range(0, len(listeoperation)):
        strline += listeoperation[i][j] + ';'
    writeToCSV(strline)
writeToCSV('\r')

print('Stop generation')
