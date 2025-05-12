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

#Sign Up Page with Logic
@potato.route("/signup", methods=['POST', 'GET'])
def signup():
  error= None
  if request.method == "POST":
    fName = request.form.get("firstname")
    lName = request.form.get("lastname")
    email = request.form.get("email")
    pass1= request.form.get("password")
    pass2= request.form.get("confirm_password")

    iCheck = mydb.cursor()
    iCheck.execute("select count(*) from spacepotatoesdb.loginkey where FirstName= " + "'" +fName+ "'" +" and LastName= " + "'" + lName + "'" + " and Email=  " + "'" +email+ "'" )
    SQLLoginCheck = iCheck.fetchall()
    checkint = (int(str(SQLLoginCheck[0]).replace(',', '').replace('(','').replace(')','')))
    if checkint >0:
      print(SQLLoginCheck)
      error = "User already exists. Please try another email."
    elif pass1 != pass2: 
      error = "Passwords do not match."
    else:
      #push to database
      sProc = mydb.cursor()
      sProc.execute("select count(*) from spacepotatoesdb.loginkey")
      SQLLoginCheck2= sProc.fetchall()
      checkrows2= int(str(SQLLoginCheck2).replace(',', '').replace('(','').replace(')','').replace('[','').replace(']',''))
      ID= checkrows2 +1 
      args= [ID, fName, lName, email, pass1]
      sProc.callproc('loginkey', (ID, fName, lName, email, pass1))
      mydb.commit()
      sProc.close()
      #move page to new page (to be assigned)
  return render_template("signup.html", error = error)

#Sign In Page with Logic
@potato.route("/signin", methods=['POST', 'GET'] )
def signin():
  error= None
  if request.method == "POST":
    fName = request.form.get("FirstName")
    lName = request.form.get("LastName")
    email = request.form.get("Email")
    password= request.form.get("Password")

    iCheck = mydb.cursor()
    iCheck.execute("select count(*) from spacepotatoesdb.loginkey where FirstName= " + "'" +fName+ "'" +" and LastName= " + "'" + lName + "'" + " and Email=  " + "'" +email+ "'" )
    SQLLoginCheck = iCheck.fetchall()
    checkint = (int(str(SQLLoginCheck[0]).replace(',', '').replace('(','').replace(')','')))
    if checkint ==0:
        print(SQLLoginCheck)
        error = "User does not exist."
    else: 
        iCheck.execute("select Pass from spacepotatoesdb.loginkey where FirstName= " + "'" +fName+ "'" +" and LastName= " + "'" + lName + "'" + " and Email=  " + "'" +email+ "'" )
        passCheck= iCheck.fetchall()
        passwordcheck= str(passCheck[0]).replace(',', '').replace('(','').replace(')','').replace("'","")
        if password != passwordcheck: 
          print(passwordcheck)
          error = "Password is incorrect."
        else: 
          print("Correct password")
          error = "Password is correct."
          #move page to new page (to be assigned) 
  return render_template("signin.html", error = error)


##Check if login details are already in the database
def later():

  mycursor = mydb.cursor()

  mycursor.execute("select Username, Pass, Email, FirstName, LastName from spacepotatoesdb.loginkey")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
  print(mydb)

if __name__ in "__main__":
  potato.run(debug=True)