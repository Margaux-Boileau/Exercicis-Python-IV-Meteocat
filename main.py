import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

def getMatrixFromFile(fileName):
    file = open(fileName, "r")
    reader = csv.reader(file)
    header = next(reader)  # skip the header row if it exists
    myList = [row for row in reader]
    ndarray = np.array(list(myList))
    file.close()
    return ndarray


# EXERCICI 2
ndarray_estacions = getMatrixFromFile("2022_MeteoCat_Detall_Estacions.csv")
ndarray_dades = getMatrixFromFile("MeteoCat_Metadades.csv")
ndarray_estacions2 = getMatrixFromFile("2022_MeteoCat_Detall_Estacions2.csv")

# EXERCICI 3 PART 1
estacions = pd.read_csv("2022_MeteoCat_Detall_Estacions.csv")
tm_february = estacions[estacions["DATA_LECTURA"].str.startswith("2022-02-")]
tm_february = tm_february.loc[tm_february["ACRÒNIM"] == "TM"]
tm_february["DATA_LECTURA"] = tm_february["DATA_LECTURA"].str[-2:]

grouped = tm_february.groupby("CODI_ESTACIO")
print(grouped)
plt.figure(figsize=(10, 6))
for name, group in grouped:
    plt.plot(group["DATA_LECTURA"], group["VALOR"], label=name)

plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature vs. Date for Different Stations")
plt.legend(loc="upper right")
plt.grid(True)

plt.show()

# EXERCICI 3 PART 2 (subplots)
unique_stations = tm_february["CODI_ESTACIO"].unique()

fig, axes = plt.subplots(len(unique_stations), 1, figsize=(10, 6 * len(unique_stations)))

for i, station in enumerate(unique_stations):
    data_for_station = tm_february[tm_february["CODI_ESTACIO"] == station]
    axes[i].plot(data_for_station["DATA_LECTURA"], data_for_station["VALOR"])
    axes[i].set_title(f"Station {station}")
    axes[i].set_xlabel("Date")
    axes[i].set_ylabel("Temperature")

plt.tight_layout()
plt.show()

# EXERCICI 4 PART 1 (histograma)
temperatures = tm_february["VALOR"]
temperature_range = (-10, 25)
plt.hist(temperatures, bins=20, range=temperature_range, edgecolor="k")
plt.xlabel("Temperature (°C)")
plt.ylabel("Number of Days")
plt.title("Temperature Distribution in February 2022")
plt.grid(True)
plt.show()

# EXERCICI 4 PART 2 (predicció)
possible_temperatures = tm_february["VALOR"]
random_temperatures = np.random.choice(possible_temperatures, 28)

plt.plot(range(1, 29), random_temperatures, marker="o", linestyle="-", color="b")
plt.xlabel("Day of February 2023")
plt.ylabel("Temperature (°C)")
plt.xticks(range(1, 29))
plt.title("Temperature Prediction for February 2023")
plt.grid(True)
plt.show()

# EXERCICI 5 (mitjana 2022)
estacions = pd.read_csv("2022_MeteoCat_Detall_Estacions.csv")
rain_february = estacions[estacions["DATA_LECTURA"].str.startswith("2022-02-")]
rain_february["DATA_LECTURA"] = rain_february["DATA_LECTURA"].str[-2:]
rain_february = rain_february.loc[rain_february["ACRÒNIM"] == "PPT"]
rain_february = rain_february.drop_duplicates(subset=["DATA_LECTURA"], keep="first")

rain_false = rain_february.loc[rain_february["VALOR"] == 0.0].count()[0] / 28
rain_true = rain_february.loc[rain_february["VALOR"] != 0.0].count()[0] / 28

values = [rain_false, rain_true]
labels = ["No rain", "Rain"]

# Diagrama sectors
plt.figure(figsize=(8, 5))
plt.title("Rain Prediction for February 2023")
plt.pie(values, labels=labels, autopct="%.2f %%")
plt.show()

# Diagrama barres
plt.figure(figsize=(5, 3))
plt.title("Rain Prediction for February 2023")
plt.bar(labels, values)
plt.show()
