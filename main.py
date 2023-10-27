#import csv file to list of dictionaries
import os
import csv
import numpy as np
import matplotlib as plt
import pprint

print = pprint.PrettyPrinter(indent=2)

def getMatrixFromFile(fileName):
    file = open(fileName, 'r')
    reader = csv.reader(file)
    header = next(reader)  # skip the header row if it exists
    myList = [ row for row in reader]
    ndarray = np.array(list(myList))
    file.close()
    return ndarray

# 2- Carregar dades
ndarray_estacions = getMatrixFromFile('2022_MeteoCat_Detall_Estacions.csv')
# print(ndarray_estacions)

ndarray_dades = getMatrixFromFile('MeteoCat_Metadades.csv')
# print(ndarray_dades)

ndarray_estacions2 = getMatrixFromFile('2022_MeteoCat_Detall_Estacions2.csv')
#  print(ndarray_estacions2)

# 3- Visualitza temperatura mitjana del mes de Febrer
# list dades febrer using ndarray_estacions[x][0]
# example of data : 2022-01-02,"21:18:00","D5","TN",9.4
list_dades_febrer = []
for i in range(len(ndarray_estacions)):
    if ndarray_estacions[i][0].startswith('2022-02'):
        list_dades_febrer.append(ndarray_estacions[i])

temps_mitjans = {}
for dada in list_dades_febrer:
    data = dada[0]
    estacio = dada[1]
    temperatura = float(dada[3])
    if data not in temps_mitjans:
        temps_mitjans[data] = {}
    temps_mitjans[data][estacio] = temperatura

print.pprint(list_dades_febrer)


# # BEGIN: 8f7d6e5a1b2c
# list_dades_febrer = []
# for i in range(len(ndarray_estacions)):
#     if ndarray_estacions[i][0].startswith('2022-02'):
#         list_dades_febrer.append(ndarray_estacions[i])

# temps_mitjans = {}
# for dada in list_dades_febrer:
#     estacio = dada[1]
#     temperatura = float(dada[3])
#     if estacio not in temps_mitjans:
#         temps_mitjans[estacio] = []
#     temps_mitjans[estacio].append(temperatura)

# print(temps_mitjans)
# # END: 8f7d6e5a1b2c