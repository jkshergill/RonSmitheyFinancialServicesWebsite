import mysql.connector
from flask import Flask, render_template, request, redirect

##Connect to Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SpacePotatoes131$",
  database="spacepotatoesdb"
)

potato = Flask(__name__)

@potato.route("/")
def start():
  return redirect("/home")


@potato.route("/home")
def home():
  return render_template("index.html")

@potato.route("/services")
def service():
  return render_template("services.html")

@potato.route("/resources")
def resource():
  return render_template("resources.html")

@potato.route("/signup")
def signup():
  return render_template("signup.html")

@potato.route("/signin")
def signin():
  return render_template("signin.html")


##Check if login details are already in the database
def later():

  mycursor = mydb.cursor()

  mycursor.execute("select Username, Pass, Email, FirstName, LastName from spacepotatoesdb.loginkey")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
  ##print(mydb)


  """@
  convert()= html.getvalue() 
  FName= convert(FirstName)
  if sqldraw.[Firstname] = FName


  FirstName
  LastName
  Password
  Email """

if __name__ in "__main__":
  potato.run(debug=True)