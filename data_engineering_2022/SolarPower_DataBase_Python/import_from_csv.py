import sqlite3
from tqdm import tqdm

connection = sqlite3.connect("solarPower.db")
cursor = connection.cursor()

# Import Plant_1_Generation_Data
with open('solar data project/Plant_1_Generation_Data.csv', 'r') as file:
    no_records = 0
    for row in tqdm(file):
        cursor.execute("INSERT INTO plantData VALUES (?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1

print('\n{} Plant_1_Generation_Data Records transferred'.format(no_records))


# Import Plant_2_Generation_Data
with open('solar data project/Plant_2_Generation_Data.csv', 'r') as file:
    no_records = 0
    for row in tqdm(file):
        cursor.execute("INSERT INTO plantData VALUES (?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1

print('\n{} Plant_2_Generation_Data Records transferred'.format(no_records))


# Import Plant_1_Weather_Sensor_Data
with open('solar data project/Plant_1_Weather_Sensor_Data.csv', 'r') as file:
    no_records = 0
    for row in tqdm(file):
        cursor.execute("INSERT INTO weatherSensorData VALUES (?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1

print('\n{} Plant_1_Weather_Sensor_Data Records transferred'.format(no_records))


# Import Plant_2_Weather_Sensor_Data
with open('solar data project/Plant_2_Weather_Sensor_Data.csv', 'r') as file:
    no_records = 0
    for row in tqdm(file):
        cursor.execute("INSERT INTO weatherSensorData VALUES (?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print('\n{} Plant_2_Weather_Sensor_Data Records transferred'.format(no_records))
