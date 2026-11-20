import sqlite3
import csv

con = sqlite3.connect("ttc_delays.db")

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS subway_delays")
cur.execute("""CREATE TABLE subway_delays (
    id INTEGER PRIMARY KEY,
    delay_date TEXT,
    delay_time text,
      day text,
      station text,
      code text,
      delay_minutes integer,
      delay_gap_minutes integer,
      bound text,
    line text,
    vehicle integer
)""")

cur.execute( "DROP TABLE IF EXISTS delay_codes")
cur.execute( """CREATE TABLE delay_codes (
    id INTEGER,
    code TEXT PRIMARY KEY,
    description TEXT
)""")

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

f = open("TTC Subway Delay Data since 2025.csv", "r")
line = f.readline()
line = f.readline()
delay_data = []

while line:
    row_list = line.split(",")
    row_list[6] = int(row_list[6])
    row_list[7] = int(row_list[7])
    row_list[10] = int(row_list[10])

    row = tuple(row_list)
    #cur.execute("""
     #   INSERT INTO subway_delays VALUES
      #      (row[1], row[2], row[3], row[4], row[5], int(row[6]), int(row[7]), row[8], row[9], int(row[10]))
       #         """)
    delay_data.append(row)
    line = f.readline()

f.close()

f = open("Code Descriptions.csv")
line = f.readline()
line = f.readline()
code_data = []

while line:
    row_list = line.split(",")
    row_list[0] = int(row_list[0])

    row = tuple(row_list)
    code_data.append(row)
    line = f.readline()

f.close()

cur.executemany( """INSERT INTO subway_delays(
                id,
                delay_date,
                delay_time,
                day,
                station,
                code,
                delay_minutes,
                delay_gap_minutes,
                bound,
                line,
                vehicle) VALUES(
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                ) """, delay_data)

cur.executemany( """INSERT INTO delay_codes( 
                id, code, description) VALUES(
                ?, ?, ?)""", code_data)


con.commit()