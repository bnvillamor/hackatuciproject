import psycopg2
import os 
import csv
#postgresql://justin:NzIK5V7dq4kvObC7IX79-Q@livid-ewe-4867.6wr.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full
os.environ["DATABASE_URL"] = "postgresql://justin:NzIK5V7dq4kvObC7IX79-Q@livid-ewe-4867.6wr.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
conn = psycopg2.connect(os.environ['DATABASE_URL'])
#establish connection to db

#forecast.csv: contains data from https://open-meteo.com/
datafile = open("forecast.csv", "r")
data = csv.reader(datafile, delimiter=",")
datafile.close()

temp = []
for row in data:
    if row != []:
        temp.append(row)
rows = []
'''parses rows into date, hour, minute, and temperature (converted to farenheuit)'''
for i in temp[4:]:
    temprow = []
    t = i[0].split("T")
    hour, minute = t[1].split(":")
    temprow.append(t[0])
    temprow.append(hour)
    temprow.append(minute)
    celsius = float(i[1])
    farenheit = round((((9/5) * celsius) + 32), 2)
    temprow.append(farenheit)
    rows.append(temprow)

'''test for verifting connection to db'''
with conn.cursor() as cur:
    cur.execute("SELECT now()")
    res = cur.fetchall()
    conn.commit()

'''creates table "temps" that stores aforementioned data'''
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS temps (date NAME, hour INTEGER, minute INTEGER, temp REAL)")
conn.commit()

#For inserting the data into the table: 
'''for data in rows[4:]:
    t = conn.cursor()
    t.execute(f"INSERT INTO temps VALUES ('{data[0]}', '{int(data[1])}', '{int(data[2])}', '{float(data[3])}')")
    print(f"Entered row {data}")
    conn.commit()
'''
cur.execute("SELECT * from temps")
t = cur.fetchall()
for i in t:
    print(i)


