import sqlite3
import csv

conn = sqlite3.connect('solarPower.db')
c = conn.cursor()

c.execute("""CREATE TABLE plantData (
            DATE_TIME integer,
            PLANT_ID integer,
            SOURCE_KEY text,
            DC_POWER real,
            AC_POWER real,
            DAILY_YIELD real,
            TOTAL_YIELD real
            )""")

with open('solar data project/Plant_1_Generation_Data.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['DATE_TIME'], i['PLANT_ID'], i['SOURCE_KEY'], i['DC_POWER'], i['AC_POWER'], i['DAILY_YIELD'], i['TOTAL_YIELD']) for i in dr]

conn.commit()
conn.close()
