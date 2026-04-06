import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table'""",conn)
print(tables)

country = pd.read_sql("""SELECT * FROM Country;""",conn)
print(country)

city = pd.read_sql("""SELECT * FROM City;""",conn)
print(city)

season = pd.read_sql("""SELECT * FROM Season;""",conn)
print(season)

player = pd.read_sql("""SELECT * FROM Player;""",conn)
print(player)

team = pd.read_sql("""SELECT * FROM Team ;""",conn)
print(team)

city_join = pd.read_sql("""SELECT c.Country_Id,c.Country_Name, c1.City_Name
                        FROM Country c
                        INNER JOIN City c1
                        ON c.Country_Id == c1.Country_Id  ;""",conn)
print(city_join)

player_join = pd.read_sql("""SELECT * FROM Player
                          LEFT JOIN Season
                          ON Player.Player_id == Season.Man_of_the_Series;""",conn)
print(player_join)