import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables)

player = pd.read_sql("""SELECT * FROM Player;""",conn)
print(player)

season = pd.read_sql("""SELECT * FROM Season;""",conn)
print(season)