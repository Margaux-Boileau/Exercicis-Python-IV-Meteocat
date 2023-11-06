#import csv file to list of dictionaries
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pprint
import random
import numpy

pprint = pprint.PrettyPrinter(indent=2)

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

list_temps_mitjans = {}
for dada in list_dades_febrer:
    data = dada[0].split("-")[2]
    # remove the first 0 from data
    if data.startswith("0"):
        data = data[1:]
    # print(dada)
    
    if (dada[3] == "TM"):
        if dada[2] not in list_temps_mitjans:
            list_temps_mitjans[data] = {}
            list_temps_mitjans[data]["count"] = 1
            list_temps_mitjans[data]["sum"] = float(dada[4])
        list_temps_mitjans[data]["count"] += 1
        list_temps_mitjans[data]["sum"] += float(dada[4])

for i in list_temps_mitjans:
    # list_temps_mitjans[i]["mean"] = list_temps_mitjans[i]["sum"] / list_temps_mitjans[i]["count"]
    list_temps_mitjans[i]["mean"] = list_temps_mitjans[i]["sum"] / list_temps_mitjans[i]["count"]

# create a list of dates and a list of average temperatures

dates = []
avg_temps = []
for day in list_temps_mitjans:
    # if hour != "count" and hour != "sum":
    dates.append(day)
    avg_temps.append(list_temps_mitjans[day]["mean"])


# plot the graph

def aa1():
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
# plt.bar(dates, avg_temps, color=colors[:len(dates)])
# select 8 random colors from the list
    list1 = []
    for i in range(len(dates)):
        # get random elemnt from colors

        list1.append(random.choice(colors))
    
    list2 = []
    for i in range(len(dates)):
    # get random elemnt from colors
    
        list2.append(random.choice(colors))


    fig, axs = plt.subplots(2)
    axs[0].bar(dates, avg_temps, color=list1)
    axs[1].bar(dates, avg_temps, color=list2)
    plt.show()

# aa1();

# Usant les dades de la temperatura mitjana d’entre totes les estacions, l’objectiu és
# calcular i graficar una predicció de la temperatura mitjana estàndard del mes de
# febrer de 2023.
# Sabent les dades de temperatura mitjana per dia del mes de Febrer de 2022 per totes
# les estacions, , dibuixa un histograma per a conèixer quina distribució de valors
# temperatura hi ha i en quina freqüència apareixen. És a dir, a les d’abscisses (x) hi
# posarem els graus de temperatura (per exemple de -10 a +25) i a l’eix de les y hi
# posarem la quantitat de dies que cauen en cada rang.
# Sabent aquesta informació, usa les funcionalitats de random() i choice() de NumPy
# per tal de calcular un array de valors de temperatura mitjana per a cada dia del mes
# de febrer de 2023.
# pas 1
# reset plt
# plt.clf()
# # from list of float to list of int
# list_avg_temps = [int(data) for data in avg_temps]
# print(list_avg_temps)
# plt.hist([int(temp) for temp in avg_temps], bins=10)
# plt.show()

# pprint.pprint(list_temps_mitjans)



def predict_temp_mitjana_febrer_2023(estacions: numpy.ndarray, detall_estacions: numpy.ndarray, metadades: numpy.ndarray):
    mitjanes = temp_mitjana_febrer(estacions, detall_estacions, metadades)
# Supongamos que tienes una lista de temperaturas medias diarias para febrero de 2022
    temperaturas_febrero_2022 = numpy.array(mitjanes)[:,1]
    # Crear un histograma para visualizar la distribución de las temperaturas de febrero de 2022
    plt.hist(temperaturas_febrero_2022, bins=range(-10, 26), edgecolor='black')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas en febrero de 2022')
    plt.show()

    # Calcular la media y la desviación estándar de las temperaturas de febrero de 2022
    media = numpy.mean(temperaturas_febrero_2022)
    desviacion_estandar = numpy.std(temperaturas_febrero_2022)

    # Generar valores aleatorios para febrero de 2023 basados en la distribución de 2022
    temperaturas_febrero_2023 = numpy.random.normal(media, desviacion_estandar, 28)  # Suponiendo 28 días en febrero

    # Graficar la distribución de las temperaturas de febrero de 2023
    plt.hist(temperaturas_febrero_2023, bins=range(-10, 26), edgecolor='black')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas en febrero de 2023')
    plt.show()

# print(predict_temp_mitjana_febrer_2023(estacions, detall_estacions, metadades))

# 4- Predicció temperatura mes de Febrer
avg_temps_array = np.array(avg_temps)

print(avg_temps_array)

def predict_temp_mitjana_febrer_2023(listFeb: numpy.ndarray):
    # plt.hist(listFeb, bins=range(-10, 26), edgecolor='black')
    # plt.xlabel('Temperatura (°C)')
    # plt.ylabel('Frecuencia')
    # plt.title('Distribución de temperaturas en febrero de 2022')
    # plt.show()
    
    
    fig, axs = plt.subplots(2)
    axs[0].hist(listFeb, bins=range(-10, 26), edgecolor='black')
    axs[0].xlabel('Temperatura (°C)')
    axs[0].ylabel('Frecuencia')
    axs[0].title('Distribución de temperaturas en febrero de 2022')
    axs[1].bar(dates, avg_temps)
    
    # Calcular la media y la desviación estándar de las temperaturas de febrero de 2022
    media = numpy.mean(temperaturas_febrero_2022)
    desviacion_estandar = numpy.std(temperaturas_febrero_2022)

    # Generar valores aleatorios para febrero de 2023 basados en la distribución de 2022
    temperaturas_febrero_2023 = numpy.random.normal(media, desviacion_estandar, 28)  # Suponiendo 28 días en febrero

    # Graficar la distribución de las temperaturas de febrero de 2023
    plt.hist(temperaturas_febrero_2023, bins=range(-10, 26), edgecolor='black')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Frecuencia')
    plt.title('Distribución de temperaturas en febrero de 2023')
    plt.show()
    
    
    plt.show()
    
    
    
predict_temp_mitjana_febrer_2023(avg_temps_array)
