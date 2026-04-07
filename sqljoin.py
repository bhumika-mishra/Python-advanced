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

all = pd.read_sql("""SELECT Season_Id, Match_Id, v.Venue_Name,c.City_Name, t.Team_name AS Winner
                  FROM Match
                  INNER JOIN Venue AS v ON
                  match.Venue_Id == v.Venue_Id
                  INNER JOIN City AS c ON v.City_Id == c.city_Id
                  INNER JOIN Team AS t ON
                  match.Match_Winner == t.Team_Id;""",conn)
print(all)

match = pd.read_sql("""SELECT Match_Id, Team_2 AS Away_Team,Toss_Winner,Match_Winner
                    FROM Match
                    WHERE Team_1 = 
                    (SELECT Team_1 FROM Match
                    WHERE Team_1 == 3 AND Season_Id == 8)""",conn)
print(match)

match_run = pd.read_sql("""SELECT Match_Id,Runs_Scored AS Total_Runs,Innings_No
                        FROM Batsman_Scored
                        WHERE Total_Runs > 5 AND Match_Id IN
                        (SELECT Match_Id FROM Match WHERE Season_Id == 8)""",conn)
print(match_run)

avg = pd.read_sql("""SELECT Match_Id,Runs_Scored AS Total_Runs,Innings_No
                     FROM Batsman_Scored
                     WHERE Innings_No == 1 AND Runs_Scored > (SELECT AVG(Runs_Scored)FROM Batsman_Scored)""",conn)
print(avg)
