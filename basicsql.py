import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

tables = pd.read_sql("""SELECT * FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables)

match = pd.read_sql("""SELECT * FROM Match;""",conn)
print(match)

team = pd.read_sql("""SELECT Match_Winner AS Team_id FROM Match 
                   WHERE Win_Margin > 50;""",conn)
print(team)

avg = pd.read_sql("""SELECT AVG(Win_Margin) FROM Match
                  WHERE Match_Winner = 2; """,conn)
print(avg)

score = pd.read_sql("""SELECT * FROM Batsman_Scored ;""",conn)
print(score)

runs = pd.read_sql("""SELECT Over_Id, AVG( Runs_Scored)
                   FROM Batsman_Scored
                   GROUP BY Over_Id;""",conn)
print(runs)

total = pd.read_sql("""SELECT Match_Id , SUM(Runs_Scored) 
                    FROM Batsman_Scored
                    GROUP BY Match_Id;""",conn)
print(total)
