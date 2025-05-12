import mysql.connector

##Connect to Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SpacePotatoes131$",
  database="spacepotatoesdb"
)

##Check if login details are already in the database
mycursor = mydb.cursor()

mycursor.execute("select Username, Pass, Email, FirstName, LastName from spacepotatoesdb.loginkey")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
##print(mydb)