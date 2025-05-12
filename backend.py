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
  #print("Sign up page")
  error= None
  if request.method == "POST":
    #print("Form Submit")
    fName = request.form.get("firstname")
    lName = request.form.get("lastname")
    email = request.form.get("email")
    pass1= request.form.get("password")
    pass2= request.form.get("confirm_password")
    #print(fName + ", " +lName + ", " + email + ", " +pass1 + ", " + pass2)

    iCheck = mydb.cursor()
    iCheck.execute("select count(*) from spacepotatoesdb.loginkey where FirstName= " + "'" +fName+ "'" +" and LastName= " + "'" + lName + "'" + " and Email=  " + "'" +email+ "'" )
    SQLLoginCheck = iCheck.fetchall()
    checkint = (int(str(SQLLoginCheck[0]).replace(',', '').replace('(','').replace(')','')))
    if checkint >0:
      print(SQLLoginCheck)
      error = "User already exists. Please try again"

    else:
      #push to data base
      sProc = mydb.cursor()
      sProc.execute("select count(*) from spacepotatoesdb.loginkey")
      SQLLoginCheck2= sProc.fetchall()
      checkrows2= int(str(SQLLoginCheck2).replace(',', '').replace('(','').replace(')','').replace('[','').replace(']',''))
      ID= checkrows2 +1 
      args= [ID, fName, lName, email, pass1]
      sProc.callproc('loginkey', (ID, fName, lName, email, pass1))
      mydb.commit()
      sProc.close()
      #print("MAYBE IT SAVED??????")
      
    '''
    if SQLoginCheck.rows() > 0:

    print(SQLFirstName)
'''
    


  return render_template("signup.html", error = error)

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