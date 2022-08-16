import sqlite3

conn = sqlite3.connect('solarPower.db')
c = conn.cursor()

check_exists_plantData = """DROP TABLE IF EXISTS plantData"""
c.execute(check_exists_plantData)
check_exists_weatherSensorData = """DROP TABLE IF EXISTS weatherSensorData"""
c.execute(check_exists_weatherSensorData)

create_plantData = """CREATE TABLE plantData (
                                DATE_TIME integer,
                                PLANT_ID integer,
                                SOURCE_KEY text,
                                DC_POWER real,
                                AC_POWER real,
                                DAILY_YIELD real,
                                TOTAL_YIELD real
                                )"""
c.execute(create_plantData)

create_weatherData = """CREATE TABLE weatherSensorData (
                                DATE_TIME integer,
                                PLANT_ID integer,
                                SOURCE_KEY text,
                                AMBIENT_TEMPERATURE real,
                                MODULE_TEMPERATURE real,
                                IRRADIATION real
                                )"""
c.execute(create_weatherData)

print("plantData table has been created successfully")
conn.commit()
conn.close()
