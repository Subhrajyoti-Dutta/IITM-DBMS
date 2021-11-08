import psycopg2
import sys
import os

database = sys.argv[1]  
user = os.environ.get('PGUSER') 
password = os.environ.get('PGPASSWORD') 
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')

dates = open('date.txt', 'r')
lines = dates.readlines()


# Connect to your postgres DB
connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=host,
                                  port=port,
                                  database=database)



def getMatchNo(date):
    c2 = connection.cursor()
    query = 'select match_num from matches where match_date = %s;'
    c2.execute(query,(date,))
    result = c2.fetchall()
    c2.close()
    return result

def getRefID(matchNo):
    c3 = connection.cursor()
    query = 'select referee from match_referees where match_num = %s;'
    c3.execute(query,(matchNo,))
    result = c3.fetchall()
    c3.close()
    return result

def getRefName(refId):
    c4 = connection.cursor()
    query = 'select name from referees where referee_id = %s;'
    c4.execute(query,(refId,))
    result = c4.fetchall()
    c4.close()
    return result

dateList = []
for line in lines:
    line = str(line)
    op = getMatchNo(line)
    dateList = dateList + op
#print(dateList[0][0])

refID = []
for i in range(len(dateList)):
    matchNo = dateList[i][0]
    op = getRefID(matchNo)
    refID = refID + op
#print(refID)
nameList = []

for i in range(len(refID)):
    refId = refID[i][0]
    op = getRefName(refId)
    nameList = nameList + op

for name in nameList:
    name = list(name)
    name = name[0].split()
    
    name.reverse()
    
    if len(name) == 3:
        name[2] , name[1] = name[1] , name[2]
   
    for i in range(len(name)):
        if i == 0:
            print(name[i], end = ' ')
        elif i == (len(name) - 2) and i !=0:
            op = name[i][0] + '.'
            print(op, end = ' ')
        
        else:
            op = name[i][0] + '.'
            print(op)