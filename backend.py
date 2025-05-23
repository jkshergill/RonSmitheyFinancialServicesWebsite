import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session

##Connect to Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SpacePotatoes131$",
  database="spacepotatoesdb"
)


global GetID
GetID= None 

potato = Flask(__name__)
potato.secret_key = 'potato'

@potato.route("/")
def start():
  session.clear()
  session["signedin"] = False
  return redirect("/home")

#Home Page
@potato.route("/home")
def home():
  return render_template("index.html")

@potato.route("/privacy")
def privacy():
  return render_template("termsandprivacy.html")

@potato.route("/eventscalender")
def events():
  print("SESSION signedin =", session.get("signedin"))
  if not session.get("signedin"):
        return redirect("/signup")
  return render_template("eventscalender.html")

@potato.route("/forums", methods=['POST', 'GET'] )
def forums():
    print("SESSION signedin =", session.get("signedin"))
    if not session.get("signedin"):
        return redirect("/signup")
    return render_template("forums.html")

@potato.route('/forumsfollow', methods=['POST'])
def forumsfollow():
    title = request.form.get('title')
    content = request.form.get('content')
    print(f"New forum post: {title} — {content}")

    return redirect(url_for('home'))

#Services Page
@potato.route("/services")
def service():
  return render_template("services.html")

@potato.route("/bookappt", methods=['POST', 'GET'])
def bookappt():
  print("SESSION signedin =", session.get("signedin"))
  if not session.get("signedin"):
        return redirect("/signup")
  if request.method =="POST":
     return redirect("/home/")
  return render_template("bookappt.html")

@potato.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    reason = request.form["reason"]

    print("Booking submitted:", name, email, phone, date, time, reason)

    return redirect(url_for("home"))

@potato.route("/EDResources")
def EDResources():
  return render_template("EDResources.html")


#Resources Page
@potato.route("/resources")
def resource():
  return render_template("resources.html")

@potato.route("/mortgagecalculator")
def mortgagecalculator():
  return render_template("mortgagecalculator.html")

@potato.route("/loancalculator")
def loancalculator():
  return render_template("loancalculator.html")

@potato.route("/savingscalculator")
def savingscalculator():
  return render_template("savingscalculator.html")

#Footer
@potato.route("/inquiryform", methods=['POST', 'GET'])
def inquiryform():
    error = None
    show_view2 = False

    if request.method == "POST":
        # Case 1: message is present → this is the final submission
        if 'message' in request.form:
            message = request.form.get("message")
            types = request.form.get("types")  

            try:
                sProc = mydb.cursor()
                sProc.callproc('inquiryform', [types, message])
                mydb.commit()
                sProc.close()
                return redirect("/home")  
            except Exception as e:
                error = f"Database error: {str(e)}"
        else:
            # Case 2: this is the first form (checkboxes)
            feedback = request.form.get("feedback")
            inquiry = request.form.get("inquiry")
            transaction = request.form.get("transaction")
            general = request.form.get("general")
            other = request.form.get("other")

            possible = ["feedback", "inquiry", "transaction", "general", "other"]
            args = [feedback, inquiry, transaction, general, other]
            savelist = [possible[i] for i in range(len(args)) if args[i] is not None]

            if not savelist:
                error = "Please select at least one option."
            else:
                show_view2 = True
                types = ", ".join(savelist)
                return render_template("inquiryform.html", show_view2=True, error=None, types=types)

    return render_template("inquiryform.html", show_view2=False, error=error)

@potato.route("/aboutus")
def aboutus():
   return render_template("aboutus.html")

#Sign Up Page with Logic
@potato.route("/signup", methods=['POST', 'GET'])
def signup():
  error= None
  if request.method == "POST":
    #print("got")
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
      #print(SQLLoginCheck)
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

      iCheck.execute("select ID from spacepotatoesdb.loginkey where FirstName= " + "'" +fName+ "'" +" and LastName= " + "'" + lName + "'" + " and Email=  " + "'" +email+ "'")
      IDcheck = iCheck.fetchall()
      checkID= str(IDcheck[0]).replace(',', '').replace('(','').replace(')','').replace("'","").replace('[','').replace(']','')
      
      session.permanent = True
      session["signedin"] = True
      session["GetID"] = IDcheck
      return redirect("/home")
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
          signedin = True
          iCheck.execute("select ID from spacepotatoesdb.loginkey where FirstName= " + "'" +fName+ "'" +" and LastName= " + "'" + lName + "'" + " and Email=  " + "'" +email+ "'")
          IDcheck = iCheck.fetchall()
          checkID= str(IDcheck[0]).replace(',', '').replace('(','').replace(')','').replace("'","").replace('[','').replace(']','')
          
          session.permanent = True
          session["signedin"] = True
          session["GetID"] = IDcheck
          return redirect("/home")

  return render_template("signin.html", error = error)

@potato.route("/budgetbuilder")
def budget():
  return render_template("budgetbuilder.html")

@potato.route("/clientportal")
def clientportal():
  print("SESSION signedin =", session.get("signedin"))
  if not session.get("signedin"):
        return redirect("/signup")
  return render_template("clientportal.html")

@potato.route("/dashboard")
def dashboard():
  return render_template("dashboard.html")

@potato.route("/downloadstatements")
def ds():
  return render_template("downloadstatements.html")

@potato.route("/investmentcalc")
def investcalc():
  return render_template("investmentcalc.html")

@potato.route("/logout")
def logout():
  return render_template("logout.html")

@potato.route("/messages")
def messages():
  return render_template("messages.html")

@potato.route("/portfolio")
def portfolio():
  return render_template("portfolio.html")

@potato.route("/retirementcalc")
def retirecalc():
  return render_template("retirementcalc.html")

@potato.route("/risktolerance")
def risktol():
  return render_template("risktolerance.html")

@potato.route("/statements")
def statements():
  return render_template("statements.html")

@potato.route("/tools")
def tools():
  return render_template("tools.html")


##Check if login details are already in the database
def later():

  mycursor = mydb.cursor()

  mycursor.execute("select Username, Pass, Email, FirstName, LastName from spacepotatoesdb.loginkey")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
  print(mydb)

if __name__ == "__main__":
  potato.run(debug=True)