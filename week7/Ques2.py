import psycopg2
import sys
import os
import math

database = sys.argv[1]	
user = os.environ.get('PGUSER') 
password = os.environ.get('PGPASSWORD') 
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')

parameter = open('parameter.txt', 'r')
letters = parameter.readlines()



# Connect to your postgres DB
connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)



def getScoreSum(letter):
    conn = connection.cursor()
    query = ("select sum(m.host_team_score) from matches m , teams t " 
            " where m.host_team_id = t.team_id "
            " and m.host_team_score > m.guest_team_score " 
            " and t.name like 'XXX%';" )
            
    query = query.replace("XXX", letter)
    conn.execute(query)
    result = conn.fetchall()
    conn.close()
    return result

def calculateCosine(val):
    if val is None:
        val = 0
    val = int(val)    
    return round(math.cos(val*10*(math.pi/180)),2)    
    
    
for letter in letters:
    score = getScoreSum(letter)
    score = score[0][0]
    print(calculateCosine(score))