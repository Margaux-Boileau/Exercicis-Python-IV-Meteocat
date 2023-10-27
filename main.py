#import csv file to list of dictionaries
import os
import csv
import numpy as np

myFile = open('2022_MeteoCat_Detall_Estacions.csv', 'r')
reader = csv.DictReader(myFile)

myList = list()
for dictionary in reader:
    myList.append(dictionary)

# ----------------1 
file= open('2022_MeteoCat_Detall_Estacions.csv')

ndarray_estacions = np.ndarray([])

dades = csv.DictReader(file)
for fila in dades:
    #print(list(fila.values()))
    # print size 
    # print(len(list(fila.values())))
    print("." ,end=" " )
    ndarray_estacions = np.append(ndarray_estacions, [list(fila.values())])
    
# remobe first element of ndarray_estacions
ndarray_estacions = np.delete(ndarray_estacions, 0)
# slipt the array between 5 columns to generate a (x, 5) array
new_arr = np.array_split(ndarray_estacions, 5)
print(ndarray_estacions.shape)
print(new_arr.shape)
print(ndarray_estacions[0:5])
print(new_arr[0])

file.close()
# ----------------2
        
# ndarray = np.ndarray(shape=(len(myList),5), dtype=object, buffer=np.array(myList))
# print(ndarray)
# np.ndarray((2,), buffer=np.array([1,2,3]), offset=np.int_().itemsize, dtype=int)


# print(myList[0])

myFile.close()
