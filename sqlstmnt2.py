import pandas as pd
import sqlite3

database = "database.sqlite"
conn = sqlite3.connect(database)
print("Opened databse successfully")

table1 = pd.read_sql("""SELECT * FROM sqlite_master 
                     WHERE type = 'table';""",conn)
print(table1)

match1 = pd.read_sql("""SELECT * FROM Match ;""",conn)
print(match1)

#avg win margin for winning team in season 9 
win = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner FROM Match
                  WHERE Season_Id = 9
                  GROUP BY  Match_Winner
                  ORDER BY AVG(Win_Margin) DESC;""",conn)
print(win)

#player id & the no.of times they have been declared man_of the match in season 9
win2 = pd.read_sql("""SELECT DISTINCT Man_of_the_Match,COUNT(Man_of_the_Match) FROM Match
                   WHERE Season_Id = 9 
                   GROUP BY Man_of_the_Match;""",conn)
print(win2)

#count of venues per season
venue = pd.read_sql("""SELECT Season_Id,COUNT(Venue_Id) FROM Match
                    GROUP BY Season_Id;""",conn)
print(venue)

