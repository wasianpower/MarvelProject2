import mysql.connector

HOST = "localhost"
USER = "liu4"
DB = "Team4"
PASS="S218288"
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASS,
    database=DB
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM ART1")

myresult = mycursor.fetchall()

for x in myresult:
      print(x)
    
