from flask import Flask, render_template, redirect, url_for, flash, request, session
from flaskext.mysql import MySQL
import datetime



app = Flask(__name__)
mysql = MySQL()
app.secret_key = "i love you cute"
#setter db to USE
app.config['MYSQL_DATABASE_USER'] ="root"
app.config['MYSQL_DATABASE_PASSWORD'] =""
app.config['MYSQL_DATABASE_DB']="hkscholar"
app.config['MYSQL_DATABASE_HOST']="localhost"
#connection
mysql.init_app(app)
conn = mysql.connect()
qury = conn.cursor()


#dont tuch data for log in

qury.execute("SELECT `email` FROM `hk_users`")
userEmail = qury.fetchall()
usremail = []
for i in userEmail:
    usremail.append(i[0])
print(usremail)

qury.execute("SELECT `password` FROM `hk_users`")
userPassword = qury.fetchall()
usrpass = []
for i in userPassword:
    usrpass.append(i[0])
print(usrpass)

#portanti ni sa log in
credintials = []
index = 0
for i in usremail:
    credintials.append(i +" "+ usrpass[index])
    index+=1
print(credintials)


#request data
qury.execute("SELECT * FROM `request` WHERE 1")
regdata = qury.fetchall()

reqdatalist=[]
for i in regdata:
    reqdatalist.append(i)
print(reqdatalist)

chcker = "s"# sa aproval ni nga form





#render req form
@app.route("/req")
def requestForm():

    if "user" in session:

        return render_template("request.html")
    else:
        return render_template("login.html")
#render dash board form
@app.route("/dashBoard")
def dashboard():

    return render_template("dashboard.html", rec = reqdatalist)

@app.route("/")
def LogIn():

    return render_template("login.html")


#process nadi tanan sa dalom


@app.route("/logInProcess", methods=["POST"])
def logProcess():
    email = request.form['email']
    password = request.form['psw']
    logindata = email+" "+password
    session["user"]=email

    if logindata in credintials:

        # usr namea
        qury.execute("SELECT `fname` FROM `hk_users` WHERE `email` = '" + session["user"] + "' ")
        fname = qury.fetchall()[0][0]

        qury.execute("SELECT `lname` FROM `hk_users` WHERE `email` = '" + session["user"] + "' ")
        lname = qury.fetchall()[0][0]

        session["fname"] = fname
        session["lname"] = lname

        username = (fname+" "+lname)
        session['username']=username


        return redirect(url_for("requestForm"))

    else:

        flash("Wrong Email or Password", "info")
        return redirect(url_for("LogIn"))
    return redirect(url_for("requestForm"))

#log out

@app.route("/logOut", methods=['post'])
def LogOut():
    session.pop("user",None)
    flash("logout na","info")
    return redirect(url_for("LogIn"))


#req timein
@app.route("/processReqTimeIn", methods =['POST'])
def processReqInS():
    # Get the current time
    current_time = datetime.datetime.now()
    # Extract the hours and minutes
    current_hour = current_time.hour
    current_minute = current_time.minute
    # the hours and minutes
    timeIn = (f"{current_hour:}:{current_minute:02d}")
    session["timeIn"] = timeIn
    print(timeIn)

    qury.execute("INSERT INTO `request`(`email`, `timeIn`) VALUES ('"+session['user']+"','"+session["timeIn"]+"')")
    conn.commit()

    return redirect(url_for("requestForm"))

# req timeOut
@app.route("/processReqTimeOut", methods=['POST'])
def processReqOut():
    # Get the current time
    current_time = datetime.datetime.now()
    # Extract the hours and minutes
    current_hour = current_time.hour
    current_minute = current_time.minute
    # the hours and minutes
    timeOut = (f"{current_hour:}:{current_minute:02d}")
    session["timeOut"]= timeOut
    print(timeOut)

    qury.execute("UPDATE `request` SET `timeOut`='" + session["timeOut"] + "' WHERE `email` = '" + session["user"] + "' AND `timeIn` ='" + session["timeIn"] + "' ")
    conn.commit()

    #SESSION TO POP TIME IN AND OUT
    session.pop("timeOut",None)
    session.pop("timeIn", None)




    #update req table

    return redirect(url_for("requestForm"))



#aproval request

@app.route("/reqAproval", methods=['POST'])
def reqProcessAproval():



    try:
        if request.form.getlist('Approve')[0] == 'Approve':
            chcker ="Approves"
            print("Approves")
            print(chcker)


        else:
            print("error")
    except:
        if request.form.getlist('Decline')[0] == 'Decline':
            chcker = "Decline"
            print("Decline")
            print(chcker)

        else:
            print("error")




    return redirect(url_for("dashboard"))




if __name__ == "__main__":
    app.run(debug=True)