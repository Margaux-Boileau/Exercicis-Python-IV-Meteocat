import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def getMatrixFromFile(fileName):
    file = open(fileName, 'r')
    reader = csv.reader(file)
    header = next(reader)  # skip the header row if it exists
    myList = [ row for row in reader]
    ndarray = np.array(list(myList))
    file.close()
    return ndarray

# EXERCICI 2
ndarray_estacions = getMatrixFromFile('2022_MeteoCat_Detall_Estacions.csv')
ndarray_dades = getMatrixFromFile('MeteoCat_Metadades.csv')
ndarray_estacions2 = getMatrixFromFile('2022_MeteoCat_Detall_Estacions2.csv')

#EXERCICI 3 PART 1
estacions = pd.read_csv('./Exercicis-Python-IV-Meteocat/2022_MeteoCat_Detall_Estacions.csv')
filtered_estacions = estacions[estacions['DATA_LECTURA'].str.startswith('2022-02-')]
filtered_estacions = filtered_estacions.loc[filtered_estacions['ACRÒNIM'] == 'TM']
filtered_estacions['DATA_LECTURA'] = filtered_estacions['DATA_LECTURA'].str[-2:]

grouped = filtered_estacions.groupby('CODI_ESTACIO')
print(grouped)
plt.figure(figsize=(10, 6))
for name, group in grouped:
    plt.plot(group['DATA_LECTURA'], group['VALOR'], label=name)

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Value vs. Date for Different Stations')
plt.legend(loc='upper right')
plt.grid(True)

plt.show()

# EXERCICI 3 PART 2 (subplots)
unique_stations = filtered_estacions['CODI_ESTACIO'].unique()
print(unique_stations)

fig, axes = plt.subplots(len(unique_stations), 1, figsize=(10, 6 * len(unique_stations)))

for i, station in enumerate(unique_stations):
    data_for_station = filtered_estacions[filtered_estacions['CODI_ESTACIO'] == station]
    axes[i].plot(data_for_station['DATA_LECTURA'], data_for_station['VALOR'])
    axes[i].set_title(f'Station {station}')
    axes[i].set_xlabel('Date')
    axes[i].set_ylabel('Value')

plt.tight_layout()
plt.show()
print(filtered_estacions)

#EXERCICI 4 PART 1 (histograma)
temperatures = filtered_estacions['VALOR']
temperature_range = (0, 25)
plt.hist(temperatures, bins=20, range=temperature_range, edgecolor='k')
plt.xlabel('Temperature (°C)')
plt.ylabel('Number of Days')
plt.title('Temperature Distribution in February 2022')
plt.grid(True)
plt.show()

#EXERCICI 4 PART 2 (predicció)
possible_temperatures = filtered_estacions['VALOR']
random_temperatures = np.random.choice(possible_temperatures, 28)

plt.plot(range(1, 29), random_temperatures, marker='o', linestyle='-', color='b')
plt.xlabel('Day of February 2023')
plt.ylabel('Temperature (°C)')
plt.xticks(range(1, 29))
plt.title('Random Temperature Values for February 2023')
plt.grid(True)
plt.show()

#EXERCICI 5