import os

import bcrypt
import pandas as pd
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, send_file, jsonify
from flaskext.mysql import MySQL
import cryptography.fernet
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
# Generate a key
key = cryptography.fernet.Fernet.generate_key()
# Create a Fernet symmetric key
cipher_suite = cryptography.fernet.Fernet(key)


app = Flask(__name__)
app.secret_key = "i love you cute"
mysql = MySQL()

#dir whare photo are stored
#dir whare photo are stored
app.config['UPLOAD_DIR']="static/profilePics/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#setter kung ano nga db gamiton
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]=""
app.config["MYSQL_DATABASE_DB"]="hkscholar"
app.config["MYSQLI_DATABASE_HOST"]="localhost"


#connection mo ni sa db kag sa python aka conn
mysql.init_app(app)
conn = mysql.connect()
qury = conn.cursor()

#--------------------------log in data dont tandog--------------------------------

qury.execute("SELECT `email` FROM `hk_users`")
userEmail = qury.fetchall()
usremail = []
for i in userEmail:
    usremail.append(i[0])


qury.execute("SELECT `password` FROM `hk_users`")
userPassword = qury.fetchall()
usrpass = []
for i in userPassword:
    usrpass.append(i[0])


#portanti ni sa log in
credintials = []
index = 0
for i in usremail:
    credintials.append(i +" "+ usrpass[index])
    index+=1


#----student id numbers---
qury.execute("SELECT `idnum` FROM `hk_users`")
idnumberStdnt = qury.fetchall()
stdntIdNumberAvilable =[]
for k in idnumberStdnt:
    stdntIdNumberAvilable.append(k[0])






adminls = []
#------------admin data---------------------


qury.execute("SELECT `adminIdNumber` FROM `admin` ")
adminUsername = qury.fetchall()

adminusernamels=[]
for k in adminUsername:
    adminusernamels.append(k[0])


qury.execute("SELECT `passWord` FROM `admin` ")
adminpass = qury.fetchall()

adminuserpassWord=[]
for k in adminpass:
    adminuserpassWord.append(k[0])


admin_cridentials = []
indexadmin = 0
for i in adminusernamels:
    admin_cridentials.append(i +" "+ adminuserpassWord[indexadmin])
    indexadmin+=1



#-----------------operations Datas-------------------------------------------

qury.execute("SELECT `Faculty_Id_Number` FROM `operations_data`")
Faculty_Id_Number = qury.fetchall()

faculty_id = []
for k in Faculty_Id_Number:
    faculty_id.append(k[0])


qury.execute("SELECT `Faculty_Password`FROM `operations_data`")
Faculty_PassWord = qury.fetchall()

faculty_psw = []
for k in Faculty_PassWord:
    faculty_psw.append(k[0])


#faculty credintials
faculty_credintials =[]
faculty_counter = 0


for k in faculty_id:
    compress = (k+" "+faculty_psw[faculty_counter])
    faculty_credintials.append(compress)
    faculty_counter+=1








#------------------------data table for Duty_assignment------------------------
qury.execute("SELECT * FROM `operation_request`")
operation_request_DB = qury.fetchall()
operation_request = []
for k in operation_request_DB:
    operation_request.append(k)


table_Assigment_Page_Admin =[]
for k in range(len(operation_request)):
    process = {"DESIGNATION": operation_request[k][0],"REQ": operation_request[k][1],"REPORT DAY/S": operation_request[k][2], "SUPERVISOR":str(operation_request[k][5]),	"DEPT":operation_request[k][4], "REQST":operation_request[k][3],"REQ ID":operation_request[k][6]}
    table_Assigment_Page_Admin.append(process)

#checker if ang student naka sign in or wala pa
list_of_sign_in = []
#stroage for time in Time to use in formulation
timeInList =[]
# stroage for time in Time to use in formulation




#----------------------main code------------------------------



#logout for admin
@app.route("/LogoutAdmin", methods=['POST'])
def logOutAmin():
    session.pop("adminUser",None)
    session.pop("Duty_record_table", None)
    session.pop("student_Id_num", None)
    session.pop("userIdAdmin", None)

    return '<script>;window.location="/"</script>'




#------------------------------------log out----------------------------------------------

@app.route("/Logout", methods=['POST'])
def logOut():
    qury.execute("UPDATE `operations_data` SET `status_ol`='INACTIVE' WHERE `Faculty_Id_Number` = '" + session[
        'opration_Id'] + "'")
    conn.commit()
    qury.execute("UPDATE `operations_data` SET `color_status`='danger' WHERE `Faculty_Id_Number` = '"+session[
        'opration_Id']+"'")

    # ---------- this is for recording all activities of the user-----------------

    x = datetime.datetime.now()

    qury.execute(
        "SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '" +
        session['opration_Id'] + "'")
    operation_data = qury.fetchall()

    fullname = str(operation_data[0][0]) + " " + str(operation_data[0][1])

    qury.execute("INSERT INTO `active_logs`(`date_time`, `user_id`, `uname`, `dept`, `act_perm`)"
                 " VALUES ('" + str(x).split(".")[0] + "','" + str(operation_data[0][2]) + "','" + str(
        fullname) + "','" + str(operation_data[0][3]) + "','Just log out to the system')")
    conn.commit()




    conn.commit()
    session.pop("user",None)
    session.pop("username",None)
    session.pop("lname",None)
    session.pop("fname", None)
    session.pop("assigmentstdList", None)
    session.pop("opration_Id", None)


    



    return '<script>;window.location="/"</script>'


#-----------------------landing page----------------------------------------------

@app.route("/")
def landing_page():

    return render_template("ScholarTracker/unaindex.php")

@app.route("/sts_Page")
def sts_Page():

    return render_template("ScholarTracker/index1caps.php")





#--------------------------------------register------------------------------------------------

@app.route("/register")
def reg_render():

    return render_template('register.html')
@app.route("/reg", methods=["POST"])
def indexprocess():
    # try:

    gmail = request.form["email"]
    password = request.form["psw"]
    repPaswrd = request.form['reppsw']
    idnum = request.form['idnum']
    fname = request.form['fname']
    lname = request.form['lname']
    mname = request.form['Mname']
    phone = request.form['phone']
    Position = request.form['Position']
    dept = request.form.get('dept')



    if password == repPaswrd:

        encrypted_pass =  bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())




        qury.execute("INSERT INTO `opertaion_req_acc`(`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`) VALUES ('"+str(lname)+"','"+str(fname)+"','"+str(encrypted_pass.decode())+"','"+str(idnum)+"','"+str(dept)+"','"+str(mname)+"','"+str(phone)+"','"+str(Position)+"','"+str(gmail)+"')")
        conn.commit()


        return '<script>alert("Registered Complete");window.location="/register"</script>'
    else:
        return '<script>alert("Password not match");window.location="/register"</script>'
    #
    # except:
    #
    #     return '<script>alert("ID number already used");window.location="/register"</script>'
    #

#---------------------------------/Sign in-----------------------------------------------------


@app.route("/Sign in")
def signInPAge():

    return render_template("SignIn.html")


@app.route("/signed in", methods= ["POST"])
def signInprocess():
    try:

        idNum = request.form['email']
        password = request.form['psw']

        session["user"]=idNum
        qury.execute("SELECT `Faculty_Password` FROM `operations_data` WHERE  `Faculty_Id_Number` = '"+idNum+"'")
        from_db_pass = qury.fetchall()


        if bcrypt.checkpw(password.encode(), from_db_pass[0][0].encode()):
            password = str(from_db_pass[0][0])
            logindata = idNum + " " + password



            if logindata in faculty_credintials:



                # faculty usr namea
                qury.execute("SELECT `Faculty_Fname` FROM `operations_data` WHERE `Faculty_Id_Number` = '"+idNum+"'")
                fname = qury.fetchall()[0][0]

                qury.execute("SELECT `Faculty_Lname` FROM `operations_data` WHERE `Faculty_Id_Number` = '"+idNum+"'")
                lname = qury.fetchall()[0][0]

                qury.execute("SELECT `Faculty_Id_Number` FROM `operations_data` WHERE `Faculty_Id_Number`= '"+idNum+"'")
                opration_Id = qury.fetchall()[0][0]


                session["fname"] = fname
                session["lname"] = lname

                username = (fname+" "+lname).upper()
                session['username']=username
                session["opration_Id"] = opration_Id
                qury.execute("UPDATE `operations_data` SET `status_ol`='ACTIVE' WHERE `Faculty_Id_Number` = '" + session[
                    'opration_Id'] + "'")
                conn.commit()
                qury.execute("UPDATE `operations_data` SET `color_status`='success' WHERE `Faculty_Id_Number` = '" + session[
                    'opration_Id'] + "'")
                conn.commit()
        #---------- this is for recording all activities of the user-----------------

                x = datetime.datetime.now()

                qury.execute("SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '"+ session['opration_Id']+"'")
                operation_data = qury.fetchall()

                fullname = str(operation_data[0][0])+" "+str(operation_data[0][1])

                qury.execute("INSERT INTO `active_logs`(`date_time`, `user_id`, `uname`, `dept`, `act_perm`)"
                             " VALUES ('"+str(x).split(".")[0]+"','"+str(operation_data[0][2])+"','"+str(fullname)+"','"+str(operation_data[0][3])+"','Just log in to the system')")
                conn.commit()

                return '<script>;window.location="/Dash board"</script>'

            else:

                return '<script>alert("Wrong password or Email");window.location="/Sign in"</script>'
        else:
            return '<script>alert("Wrong password or Email");window.location="/Sign in"</script>'
    except Exception:
        return '<script>alert("Wrong password or Email");window.location="/Sign in"</script>'


#-------------------------------dash board-----------------------------------------
@app.route("/Dash board")
def Dashboard():


    if "username" in session:

        # to get data reports from db to display
        qury.execute("SELECT `content`, `date`, `time`, `adminName`, `id` FROM `reports/announcement`")
        db_announc_data = qury.fetchall()

        announcment_List = []
        dateTimeLista_announcment = []
        reversed_dare_announcment = []

        for k in db_announc_data:
            announcment_List.append(k)

            #       to display date and time


            for k in range(len(announcment_List)):
                content = str(announcment_List[k][1]) + " " + str(announcment_List[k][2]) + ">20%" + str(announcment_List[k][3]) + ">20%" + str(announcment_List[k][0])
                dateTimeLista_announcment.append(content.split(">20%"))

            # to display the latest announcement

            for k in dateTimeLista_announcment[::-1]:
                reversed_dare_announcment.append(k)
            #      end  to display date and time



        # select profile pic
        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '" + session["user"] + "'")
        profilepicDb = qury.fetchall()[0][0]


        # to display how many hk student there are
        qury.execute("SELECT `hk_ID` FROM `hk_assignd_teaecher` WHERE  `operatikon_ID` = '"+session["lname"]+" "+session["fname"]+"'")
        number_of_stndt = qury.fetchall()


        std_under_me = []
        for k in number_of_stndt:
            for m in k:

                qury.execute("SELECT `statsForRenewal` FROM `hk_users` WHERE `idnum`='"+str(m)+"'")
                dataz = qury.fetchall()[0][0]
                std_under_me.append(dataz)

        pending = []
        complete =[]

        for k in std_under_me:
            if str(k) == "Complete":
                complete.append(k)
            else:
                pending.append(k)




        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
        stduentNotAv = qury.fetchall()

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='av' ")
        studentAv = qury.fetchall()

        # comliance rate data
        if len(complete) == 0 and len(pending) == 0:
            complirate = 0
        else:
            complirate = ((len(complete)/len(pending))*100).__round__()

        return render_template("dashboard operations/OpartionsDashBoard.html",
                               logUser = session['username'],
                               dateTimeLista_announcment=reversed_dare_announcment,
                               profilepicDb=profilepicDb,complirate=str(complirate)+"%",
                               number_of_stndt=len(number_of_stndt))

    else:
        return redirect(url_for("signInPAge"))
#-----------------------------------------request-----------------------------------------------------

@app.route("/Request and Scholar Management")
def request_Scholar():
    listahan = []
    try:



        qury.execute("SELECT `hk_ID`FROM `hk_assignd_teaecher` WHERE `operatikon_ID` = '"+str(session["lname"])+" "+str(session["fname"])+"'")
        mYStudent_Db_Id = qury.fetchall()




        for k in mYStudent_Db_Id:

            qury.execute("SELECT `idnum`,`lname`, `fname`, `id_totalHours`,  `remaningDuty`, `remDutyMins`,`statsForRenewal`, `status_color` , `department` FROM `hk_users` WHERE `idnum`= '"+k[0]+"'")
            listahan.append(qury.fetchall()[0])


        student_underMe=[]
        for k in range(len(listahan)):
            tables = {"STUDENT ID":listahan[k][0],"SCHOLAR NAME":listahan[k][1]+" "+listahan[k][2],
                      "COMPLETED HOURS":str(listahan[k][3])+"m","REMAINING HOURS":listahan[k][4]+"h "+str(float(listahan[k][5]).__round__()).split(".")[0]+"m",
                      "STATUS":listahan[k][6],"color":listahan[k][7], "Department":listahan[k][8]}
            student_underMe.append(tables)


        #select profile pic
        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '" + session["user"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        for k in range (len(student_underMe)):
            # status update function
            qury.execute("SELECT  `hk_ID` FROM `hk_assignd_teaecher` WHERE `hk_ID`='"+student_underMe[k]['STUDENT ID']+"' ")
            std_id_under_me = qury.fetchall()[0][0]

            qury.execute("SELECT `remaningDuty`, `remDutyMins` FROM `hk_users` WHERE `idnum`='"+std_id_under_me+"'")
            std_remning = qury.fetchall()[0]

            hours = int(std_remning[0])
            mins = float(std_remning[1]).__round__()

            if hours <=0 and mins <=0.0 :

                qury.execute("UPDATE `hk_users` SET `status_color`='success',`statsForRenewal`='Complete' WHERE `idnum`='"+std_id_under_me+"'")
                conn.commit()

            else:

                qury.execute("UPDATE `hk_users` SET `status_color`='warning',`statsForRenewal`='pending' WHERE `idnum`='" + std_id_under_me + "'")
                conn.commit()





        return render_template("dashboard operations/requestmanage.html",logUser = session['username'], student_underMe =student_underMe,profilepicDb=profilepicDb)

    except Exception:
        return redirect(url_for("signInPAge"))


@app.route("/print_cert", methods =['POST'])
def print_cert():

    button = request.form['select']

    if str(button.split(" ")[0]) == "print":

        qury.execute("SELECT * FROM `hk_users` WHERE `idnum` = '" +button.split(" ")[1]+ "'")
        hkdetails = qury.fetchall()

        Lname = hkdetails[0][2]  # Lname
        Fname = hkdetails[0][3]  # Fname
        DUTY_SUPERVISOR = hkdetails[0][11]  # DUTY_SUPERVISOR
        department = hkdetails[0][7]  # department
        scholarship = hkdetails[0][9]  # scholarship
        DUTY_DESIGNATION = hkdetails[0][10]  # DUTY_DESIGNATION
        reqiredDuty = hkdetails[0][12]  # reqiredDuty


        return render_template("dashboard operations/print_cert.html",Fullname =Fname+" "+Lname, DUTY_SUPERVISOR=DUTY_SUPERVISOR,department=department,scholarship=scholarship,DUTY_DESIGNATION=DUTY_DESIGNATION,reqiredDuty=reqiredDuty)

    else:

        qury.execute("SELECT * FROM `hk_users` WHERE `idnum` = '" + button + "'")
        hkdetails = qury.fetchall()  # len of 17
        # details to show in profile of the student searched
        idnum = hkdetails[0][0]  # idnum
        Lname = hkdetails[0][2]  # Lname
        Fname = hkdetails[0][3]  # Fname
        totalDuty = hkdetails[0][5]  # totalDuty
        course_Program = hkdetails[0][6]  # course_Program
        department = hkdetails[0][7]  # department
        yearLvl = hkdetails[0][8]  # yearLvl
        scholarship = hkdetails[0][9]  # scholarship
        DUTY_DESIGNATION = hkdetails[0][10]  # DUTY_DESIGNATION
        DUTY_SUPERVISOR = hkdetails[0][11]  # DUTY_SUPERVISOR
        reqiredDuty = hkdetails[0][12]  # reqiredDuty
        remaningDuty = hkdetails[0][13]  # remaningDuty
        remDutyMin = str(float(hkdetails[0][14])).split(".")  # remDutyMin
        statsuForRenewal = hkdetails[0][15]  # statsuForRenewal
        Schoolyr = hkdetails[0][16]  # Schoolyr
        semister = hkdetails[0][17]  # semister



        return render_template("dashboard operations/details.html",idnum=idnum, Lname=Lname, Fname=Fname, totalDuty=totalDuty,
                               course_Program=course_Program, department=department, yearLvl=yearLvl,
                               scholarship=scholarship,
                               DUTY_DESIGNATION=DUTY_DESIGNATION, DUTY_SUPERVISOR=DUTY_SUPERVISOR,
                               reqiredDuty=reqiredDuty,
                               remaningDuty=remaningDuty, statsuForRenewal=statsuForRenewal, Schoolyr=Schoolyr,
                               semister=semister, remDutyMin=remDutyMin[0])






    #this is for requesting a hk studen
@app.route("/Modal_request_process", methods=['POST'])
def Modal_request_process():

    Designation = request.form['Designation']
    Requirements = request.form['Requirements']

    sched_list =[]
    Report_Days_mon = request.form.get("monday")
    if str(Report_Days_mon) == "None":
        pass
    else:
        sched_list.append(str(Report_Days_mon))
    Report_Days_tues = request.form.get("tuesday")
    if str(Report_Days_tues) == "None":
        pass
    else:
        sched_list.append(str(Report_Days_tues))
    Report_Days_wed = request.form.get("wednesday")
    if str(Report_Days_wed) == "None":
        pass
    else:
        sched_list.append(str(Report_Days_wed))
    Report_Days_thurs = request.form.get("thursday")
    if str(Report_Days_thurs) == "None":
        pass
    else:
        sched_list.append(str(Report_Days_thurs))
    Report_Days_fri = request.form.get("friday")
    if str(Report_Days_fri) == "None":
        pass
    else:
        sched_list.append(str(Report_Days_fri))
    Report_Days_sat = request.form.get("saturday")
    if str(Report_Days_sat) == "None":
        pass
    else:
        sched_list.append(str(Report_Days_sat))

    sched = str(sched_list).replace("['","").replace("']","").replace("', '","-")



    dept = request.form["dept"]

    Request = request.form['Request']





    qury.execute("INSERT INTO `operation_request`(`Designation`, `Requirements`, `Report Day/s`, `Request`, `DEPT`, `SUPERVISOR`) VALUES ('"+Designation+"','"+Requirements+"','"+sched+"','"+Request+"', '"+dept
                 +"', '"+str(session['lname'])+" "+str(session['fname'])+"') ")
    conn.commit()

    process = {"DESIGNATION": Designation, "REQ": Requirements,
               "REPORT DAY/S": str(sched_list), "SUPERVISOR": str(session["lname"])+" "+str(session["fname"]),
               "DEPT":dept[0][0] , "REQST":Request }
    table_Assigment_Page_Admin.append(process)

    # ---------- this is for recording all activities of the user-----------------

    x = datetime.datetime.now()

    qury.execute(
        "SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '" +
        session['opration_Id'] + "'")
    operation_data = qury.fetchall()

    fullname = str(operation_data[0][0]) + " " + str(operation_data[0][1])

    qury.execute("INSERT INTO `active_logs`(`date_time`, `user_id`, `uname`, `dept`, `act_perm`)"
                 " VALUES ('" + str(x).split(".")[0] + "','" + str(operation_data[0][2]) + "','" + str(
        fullname) + "','" + str(operation_data[0][3]) + "','Requested an HK scholar')")
    conn.commit()

    return '<script>alert("Request Sent!!");window.location="/Request and Scholar Management"</script>'


#-----------------------------end of operations requesr--------------------------------------------------


#------------------feed back form----------------------

@app.route("/feedback")
def feedback():

    try:
        # select profile pic
        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '" + session["user"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        qury.execute("SELECT  `hk_ID` FROM `hk_assignd_teaecher` WHERE `operatikon_ID` ='"+str(session["lname"])+" "+str(session["fname"])+"'")
        student_underme_Id = qury.fetchall()

        activitys_all_hk_under_me = []
        for k in student_underme_Id:
            print(k[0])
            qury.execute("SELECT * FROM `hk_user_activelogs` WHERE `hk_id` = '"+k[0]+"'")
            activitys = qury.fetchall()
            activitys_all_hk_under_me.append(activitys)

        activitys_all_hk_under_me_toshow = []
        counter = 0
        #`date_time`, `hk_id`, `hk_name`, `dept`, `act_perm`
        print(activitys_all_hk_under_me)
        for k in activitys_all_hk_under_me:
            for m in k:
                table = {"Date and Time":m[1],"ID":m[2],"USER":m[3],"DEPT":m[4],"ACT PERM":m[5]}
                activitys_all_hk_under_me_toshow.append(table)

        return render_template("dashboard operations/feedback.html", logUser=session['username'],profilepicDb=profilepicDb,activitys_all_hk_under_me_toshow=activitys_all_hk_under_me_toshow)
    except Exception:
        return redirect(url_for("signInPAge"))

@app.route("/feed_back", methods = ['POST'])
def feed_back():
    try:
        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '" + session["user"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        datez = str(datetime.datetime.now()).split(":")[0]+":"+str(datetime.datetime.now()).split(":")[1]
        feedbackMess = request.form['feedbackMess']
        feedbacker_Name = session['username']

        qury.execute("INSERT INTO `operation_feedback`(`feedMess`, `feed_name`, `feed_date`, `feed_pic`) VALUES ('"+feedbackMess+"','"+feedbacker_Name+"','"+datez+"','"+profilepicDb+"') ")
        conn.commit()

        return redirect(url_for('feedback'))
    except Exception:
        return '<script>alert("Dont use apostrophe");window.location="/feedback"</script>'


#------------------end of feddback --------------------





#-------------------------------------profile------------------------------------------
@app.route("/Profile")
def Profile_Operations():
    if "username" in session:

        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '"+session["user"]+"'")
        profilepicDb = qury.fetchall()[0][0]
        #fetch all data need to show in edit profile
        qury.execute("SELECT `Faculty_Lname`, `Faculty_Fname`,"
                     " `Operation_phone_Number`, `Operations_Email`,  "
                     "`operations_about`, `twitter`, `facebook`, `instagram`, "
                     "`linkedin`,`Address` FROM `operations_data`  WHERE `Faculty_Id_Number` = "
                     "'"+session["opration_Id"]+"'")
        operation_Db_datas = qury.fetchall()
        operation_data_list = []
        for k in operation_Db_datas[0]:
            operation_data_list.append(k)


        qury.execute("SELECT `Operation_Designation-Position`FROM `operations_data` WHERE `Faculty_Id_Number` = '"+session["opration_Id"]+"'")
        Job = str(qury.fetchall()[0][0]).upper()



        return render_template("dashboard operations/profile.html",
                               logUser = session['username'],
                               profilepicDb=profilepicDb,
                               lname=session["lname"],
                               fname=session["fname"],
                               phone=operation_data_list[2],
                               emailacc=operation_data_list[3],
                               about=operation_data_list[4],
                               twitter=operation_data_list[5],
                               facebook=operation_data_list[6],
                               instagram=operation_data_list[7],
                               linkedin=operation_data_list[8],
                               Address=str(operation_data_list[9]).upper(),
                               Job=Job)

    else:
        return redirect(url_for("signInPAge"))

@app.route("/uplaodProfile", methods=['POST']) #to upate profile picture of operations
def uplaodProfile():


    try:
        profilePic = request.files['file']
        if str(profilePic) != "<FileStorage: '' ('application/octet-stream')>":
            try:
                profilePic.save(os.path.join(app.config['UPLOAD_DIR']+secure_filename(profilePic.filename)))
                qury.execute("UPDATE `operations_data` SET `profilePics`='"+str(secure_filename(profilePic.filename))+"' WHERE  `Faculty_Id_Number` = '"+session["opration_Id"]+"' ")
                conn.commit()

                firstName = request.form['firstName']
                lasttName = request.form['lasttName']
                about = request.form['about']
                phone = request.form['phone']
                email = request.form['email']
                twitter = request.form['twitter']
                facebook = request.form['facebook']
                instagram = request.form['instagram']
                linkedin = request.form['linkedin']
                Address = request.form['Address']

                qury.execute("UPDATE `operations_data` SET `Faculty_Lname`='"+str(lasttName)+"',`Faculty_Fname`='"+str(firstName)+"',`Operation_phone_Number`='"+str(phone)+"',`Operations_Email`='"+str(email)+"',`twitter`='"+str(twitter)+"',`facebook`='"+str(facebook)+"',`instagram`='"+str(instagram)+"',`linkedin`='"+str(linkedin)+"',`Address`='"+str(Address)+"' WHERE `Faculty_Id_Number` =  '" + str(session["opration_Id"]) + "' ")
                conn.commit()

                qury.execute("UPDATE `operations_data` SET `operations_about`='" + about + "' WHERE  `Faculty_Id_Number` =  '" + str(session["opration_Id"]) + "' ")
                conn.commit()

                # ---------- this is for recording all activities of the user-----------------

                x = datetime.datetime.now()

                qury.execute(
                    "SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '" +
                    session['opration_Id'] + "'")
                operation_data = qury.fetchall()

                fullname = str(operation_data[0][0]) + " " + str(operation_data[0][1])

                qury.execute("INSERT INTO `active_logs`(`date_time`, `user_id`, `uname`, `dept`, `act_perm`)"
                             " VALUES ('" + str(x).split(".")[0] + "','" + str(operation_data[0][2]) + "','" + str(
                    fullname) + "','" + str(operation_data[0][3]) + "','Update profile')")
                conn.commit()

            except Exception:
                return '<script>alert("Dont use apostrophe");window.location="/Profile"</script>'



        else:
            try:
                firstName = request.form['firstName']
                lasttName = request.form['lasttName']
                about = request.form['about']
                phone = request.form['phone']
                email = request.form['email']
                twitter = request.form['twitter']
                facebook = request.form['facebook']
                instagram = request.form['instagram']
                linkedin = request.form['linkedin']
                Address = request.form['Address']

                qury.execute("UPDATE `operations_data` SET `Faculty_Lname`='"+str(lasttName)+"',`Faculty_Fname`='"+str(firstName)+"',`Operation_phone_Number`='"+str(phone)+"',`Operations_Email`='"+str(email)+"',`twitter`='"+str(twitter)+"',`facebook`='"+str(facebook)+"',`instagram`='"+str(instagram)+"',`linkedin`='"+str(linkedin)+"',`Address`='"+str(Address)+"' WHERE `Faculty_Id_Number` =  '" + str(session["opration_Id"]) + "' ")
                conn.commit()

                print(type(about))
                qury.execute("UPDATE `operations_data` SET `operations_about`='"+about+"' WHERE  `Faculty_Id_Number` =  '" + str(session["opration_Id"]) + "' ")
                conn.commit()

                # ---------- this is for recording all activities of the user-----------------

                x = datetime.datetime.now()

                qury.execute(
                    "SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '" +
                    session['opration_Id'] + "'")
                operation_data = qury.fetchall()

                fullname = str(operation_data[0][0]) + " " + str(operation_data[0][1])

                qury.execute("INSERT INTO `active_logs`(`date_time`, `user_id`, `uname`, `dept`, `act_perm`)"
                             " VALUES ('" + str(x).split(".")[0] + "','" + str(operation_data[0][2]) + "','" + str(
                    fullname) + "','" + str(operation_data[0][3]) + "','Update profile')")
                conn.commit()
            except Exception:
                return '<script>alert("Dont use apostrophe");window.location="/Profile"</script>'




    except RequestEntityTooLarge:
        return '<script>alert("file to large");window.location="/Profile"</script>'



    return redirect(url_for("Profile_Operations"))


@app.route("/change_password_operations", methods=['POST'])
def change_password_operations():

    old_password = request.form['password']
    new_password = request.form['newpassword']
    re_enter_password = request.form['renewpassword']


    qury.execute("SELECT `Faculty_Password` FROM `operations_data` WHERE `Faculty_Id_Number` = '"+session["opration_Id"]+"'")
    old_password_db = qury.fetchall()[0][0]

    if bcrypt.checkpw(old_password.encode(), str(old_password_db).encode()):
        if str(new_password) == str(re_enter_password):
            hashed_password_new = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
            qury.execute("UPDATE `operations_data` SET `Faculty_Password`='"+str(hashed_password_new.decode())+"' WHERE `Faculty_Id_Number` = '"+session["opration_Id"]+"' ")
            conn.commit()

            # -----------------operations Datas-------------------------------------------

            faculty_credintials.insert(faculty_credintials.index(str(session["opration_Id"])+" "+old_password_db) ,session["opration_Id"]+" "+hashed_password_new.decode())
            faculty_credintials.remove(str(session["opration_Id"]+" "+old_password_db))

            # ---------- this is for recording all activities of the user-----------------

            x = datetime.datetime.now()

            qury.execute(
                "SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '" +
                session['opration_Id'] + "'")
            operation_data = qury.fetchall()

            fullname = str(operation_data[0][0]) + " " + str(operation_data[0][1])

            qury.execute("INSERT INTO `active_logs`(`date_time`, `user_id`, `uname`, `dept`, `act_perm`)"
                         " VALUES ('" + str(x).split(".")[0] + "','" + str(operation_data[0][2]) + "','" + str(
                fullname) + "','" + str(operation_data[0][3]) + "','Change credentials')")
            conn.commit()

            return '<script>alert("Password had been updated");window.location="/Profile"</script>'
        else:
            return '<script>alert("New password did not match");window.location="/Profile"</script>'
    else:
        return '<script>alert("Old password did not match");window.location="/Profile"</script>'

    return redirect(url_for("Profile_Operations"))


#------------ end of operation profile--------------------



#-------------------------------------show total duty hours-----------------------------------------------
@app.route("/showDutyProcess", methods=['POST'])
def showDutyHours():
#for formulation data time
    qury.execute("SELECT `totaldutyHours` FROM `dutyhourformulationdata` WHERE `email`='"+session["user"]+"' ")
    dtymData = qury.fetchall()
    totalDutyHours= (dtymData[0][0])
    convertToHours = int(totalDutyHours) / 60
    splitedHM = str(convertToHours).split(".")
    hour = splitedHM[0]
    session["hours"] = hour
    minutes = float("0."+splitedHM[1])*60
    session["minutes"] = minutes
    timeToDisplay = ("Total Working Hours: '"+str(hour)+"' Hours and '"+str(int(minutes))+"' Minutes")

    session["duty"]=timeToDisplay

#this is for remaining duty hours
    target = 10800
    H = int(session["hours"]) * 60
    remM = target - H
    dataTime = str(remM / 60).split(".")
    Hour = dataTime[0]
    Minutes = str(int((float("0." + dataTime[1]) * 60)))
    reamining = str(Hour) + ":" + Minutes
    session["reamining"] =reamining

#this is for records time date display
    qury.execute("SELECT * FROM `timeintimeout` WHERE `TinToutgmail` = '" + session["user"] + "'")
    userTimeRecords = qury.fetchall()


    return render_template("dashboard operations/OpartionsDashBoard.html", logUser=session['username'],duty = session["duty"], remduty = session["reamining"], rec = userTimeRecords)



#-------------------------------------request end-------------------------------------



#------------------------------------scholar info searching--------------------------------------------------
@app.route("/search_PAge")
def searchPage():
    return render_template("scholar.html")


@app.route("/scholars",methods=['POST'])
def scholarSearch():

    searchInputIdNum = request.form['search']
    if searchInputIdNum in stdntIdNumberAvilable:
        qury.execute("SELECT * FROM `hk_users` WHERE `idnum` = '"+searchInputIdNum+"'")
        hkdetails = qury.fetchall()#len of 17
        #details to show in profile of the student searched
        idnum=hkdetails[0][0]#idnum
        Lname=hkdetails[0][2]#Lname
        Fname=hkdetails[0][3]#Fname
        totalDuty=hkdetails[0][5]#totalDuty
        course_Program=hkdetails[0][6]#course_Program
        department=hkdetails[0][7]#department
        yearLvl=hkdetails[0][8]#yearLvl
        scholarship=hkdetails[0][9]#scholarship
        DUTY_DESIGNATION=hkdetails[0][10]#DUTY_DESIGNATION
        DUTY_SUPERVISOR=hkdetails[0][11]#DUTY_SUPERVISOR
        reqiredDuty=hkdetails[0][12]#reqiredDuty
        remaningDuty=hkdetails[0][13]#remaningDuty
        remDutyMin = str(float(hkdetails[0][14])).split(".")  # remDutyMin
        statsuForRenewal=hkdetails[0][15]#statsuForRenewal
        Schoolyr=hkdetails[0][16]#Schoolyr
        semister=hkdetails[0][17]#semister

        return render_template("details.html",idnum=idnum,Lname=Lname,Fname=Fname,totalDuty=totalDuty,
        course_Program=course_Program,department=department,yearLvl=yearLvl,scholarship=scholarship,
        DUTY_DESIGNATION=DUTY_DESIGNATION,DUTY_SUPERVISOR=DUTY_SUPERVISOR,reqiredDuty=reqiredDuty,
        remaningDuty=remaningDuty,statsuForRenewal=statsuForRenewal,Schoolyr=Schoolyr,semister=semister, remDutyMin=remDutyMin[0])

    else:
        return render_template("norecords.html")


#---------- end of scholar info page -------------------









#------------------admin side------------------------------
@app.route("/adminLanding")
def admin():

    return render_template("admin.html")

@app.route("/adminLog", methods=['POST'])
def adminLog():

    try:
        useraAdmin = request.form['email']
        pswAdmin = request.form['pass']

        qury.execute("SELECT `userName` FROM `admin` WHERE `adminIdNumber` = '"+useraAdmin+"'")
        adminfullname = qury.fetchall()
        session["userIdAdmin"] =useraAdmin
        session["adminUser"] = adminfullname[0][0]


        check = useraAdmin+" "+pswAdmin
        if check in admin_cridentials:
            return '<script>window.location="admindashBoard"</script>'
        else:
            return  '<script>alert("Wrong Credentials!");window.location="/adminLanding"</script>'

    except Exception:
            return '<script>alert("Wrong Credentials!");window.location="/adminLanding"</script>'


@app.route("/admindashBoard")
def admindashBoard():

#to check if the user is still log in
    if "adminUser" in session:

        #to get data reports from db to display
        qury.execute("SELECT `content`, `date`, `time`, `adminName`, `id` FROM `reports/announcement`")
        db_announc_data = qury.fetchall()
        announcment_List = []

        for k in db_announc_data:
            announcment_List.append(k)

#       to display date and time


        dateTimeLista_announcment = []
        for k in range(len(announcment_List)):
            content = str(announcment_List[k][1]) + " " + str(announcment_List[k][2]) + ">20%" + str(
                announcment_List[k][3]) + ">20%" + str(announcment_List[k][0])

            dateTimeLista_announcment.append(content.split(">20%"))
        reversed_dare_announcment = []
       # to display the latest announcement
        for k in dateTimeLista_announcment[::-1]:
            reversed_dare_announcment.append(k)
        #      end  to display date and time



        # to display how many hk student there are
        qury.execute("SELECT * FROM `hk_users`")
        number_of_stndt = qury.fetchall()

        #to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
        stduentNotAv = qury.fetchall()


        qury.execute("SELECT * FROM `hk_users` WHERE `statsForRenewal` = 'Complete'")
        std_complied = qury.fetchall()

        qury.execute("SELECT * FROM `hk_users` WHERE `statsForRenewal` = 'pending'")
        std_Notcomplied = qury.fetchall()
        print(len(std_complied))

        #comliance rate data
        complirate = (len(std_complied)/len(number_of_stndt))*100

        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        return render_template('dashboard admin/dashboardAdminFinal.html',
                               logUser=session["adminUser"],
                               dateTimeLista_announcment=reversed_dare_announcment,
                               number_of_stndt=len(number_of_stndt),
                               stduentNotAv=len(std_complied),
                               studentAv=len(std_Notcomplied),complirate=str(complirate.__round__())+"%",
                               profilepicDb=profilepicDb)
    else:
        return redirect(url_for("admin"))

# to log out the admin log and clear all session

   #-----------------------end of admin dash board----------------------

#----------------------------ADMIN SIDE BARS----------------------------

@app.route("/compliance")
def compliance():
    # to check if the user is still log in
    if "adminUser" in session:

        # -------------student informations---------------------
        qury.execute("SELECT * FROM `hk_users` WHERE 1")
        student_Info_FromDb = qury.fetchall()

        student_info = []
        for k in student_Info_FromDb:
            student_info.append(k)


        table_OfStudent_Info = []
        counter_Table1 = 0
        # details to show in profile of the student searched #
        for k in reversed(student_info):
            std_fullNmae = str(student_info[counter_Table1][3]) + " " + str(student_info[counter_Table1][2])
            dataProcess = {"STUDENT ID": student_info[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                           "COMPLETED HOURS": student_info[counter_Table1][5] + "m",
                           "REMAINING HOURS": student_info[counter_Table1][13] + "h " +str(float(student_info[counter_Table1][14]).__round__()).split(".")[0] + "m",
                           "STATUS": student_info[counter_Table1][15],"color":student_info[counter_Table1][19],"DEPARTENT":student_info[counter_Table1][7]}
            table_OfStudent_Info.append(dataProcess)
            counter_Table1 += 1






        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]


         #status update function
        qury.execute("SELECT `idnum`,`remaningDuty`, `remDutyMins` FROM `hk_users` ")
        std_data_rem_time = qury.fetchall()

        for k in std_data_rem_time:
            hours = int(k[1])
            mins = float(k[2]).__round__()

            if hours <= 0 and mins <= 0.0:

                qury.execute("UPDATE `hk_users` SET `statsForRenewal`='Complete',`status_color`='success' WHERE `idnum`= '"+str(k[0])+"'")
                conn.commit()
            else:

                qury.execute("UPDATE `hk_users` SET `statsForRenewal`='pending', `status_color`='warning' WHERE `idnum`= '" + str(k[0]) + "'")
                conn.commit()




        return render_template("dashboard admin/compliance.html", logUser=session["adminUser"],
                               table_OfStudent_Info=table_OfStudent_Info,profilepicDb=profilepicDb)

    else:
        return redirect(url_for("admin"))


@app.route('/export_excel')
def export_excel():
    # -------------student informations---------------------
    qury.execute("SELECT * FROM `hk_users` WHERE 1")
    student_Info_FromDb = qury.fetchall()

    student_info = []
    for k in student_Info_FromDb:
        student_info.append(k)


    table_OfStudent_Info = []
    counter_Table1 = 0
    # details to show in profile of the student searched #
    for k in student_info:
        std_fullNmae = str(student_info[counter_Table1][3]) + " " + str(student_info[counter_Table1][2])
        dataProcess = {"STUDENT ID": student_info[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                       "COMPLETED HOURS": student_info[counter_Table1][5] + "m",
                       "REMAINING HOURS": student_info[counter_Table1][13] + "h " +
                                          str(float(student_info[counter_Table1][14]).__round__()).split(".")[0] + "m",
                       "STATUS": student_info[counter_Table1][15],"DEPARTENT":student_info[counter_Table1][7]}
        table_OfStudent_Info.append(dataProcess)
        counter_Table1 += 1
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(table_OfStudent_Info)

    # Save the DataFrame to an Excel file
    excel_file_path = 'HK_Dataz.xlsx'
    df.to_excel(excel_file_path, index=True)

    # Send the Excel file as a response
    return send_file(excel_file_path, as_attachment=True)

#----------------------Hk 25, 50, 75, 100-----------------------------
@app.route("/compliance_hk_25")
def compliance_Hk_25():

    try:
        #Qeury Student with 25% hk

        qury.execute("SELECT * FROM `hk_users` WHERE `scholarship` = 'HK25' " )
        student_Info_FromDb_25 = qury.fetchall()

        student_info_25 = []
        for k in student_Info_FromDb_25:
            student_info_25.append(k)

        table_OfStudent_Info_25 = []
        counter_Table1 = 0
        # details to show in profile of the student searched #
        for k in student_info_25:
            std_fullNmae = str(student_info_25[counter_Table1][3]) + " " + str(student_info_25[counter_Table1][2])
            dataProcess = {"STUDENT ID": student_info_25[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                           "COMPLETED HOURS": student_info_25[counter_Table1][5] + "m",
                           "REMAINING HOURS": student_info_25[counter_Table1][13] + "h " +
                                              str(float(student_info_25[counter_Table1][14]).__round__()).split(".")[
                                                  0] + "m",
                           "STATUS": student_info_25[counter_Table1][15], "color": student_info_25[counter_Table1][19],"DEPARTENT":student_info_25[counter_Table1][7]}
            table_OfStudent_Info_25.append(dataProcess)
            counter_Table1 += 1


        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]


        return render_template("dashboard admin/compliance_Hk_25.html",profilepicDb=profilepicDb,logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_25)
    except Exception:
        return redirect(url_for("admin"))
@app.route("/compliance_hk_50")
def compliance_Hk_50():

    try:

        # Qeury Student with 50% hk

        qury.execute("SELECT * FROM `hk_users` WHERE `scholarship` = 'HK50' ")
        student_Info_FromDb_50 = qury.fetchall()

        student_info_50 = []
        for k in student_Info_FromDb_50:
            student_info_50.append(k)

        table_OfStudent_Info_50 = []
        counter_Table1 = 0
        # details to show in profile of the student searched #
        for k in student_info_50:
            std_fullNmae = str(student_info_50[counter_Table1][3]) + " " + str(student_info_50[counter_Table1][2])
            dataProcess = {"STUDENT ID": student_info_50[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                           "COMPLETED HOURS": student_info_50[counter_Table1][5] + "m",
                           "REMAINING HOURS": student_info_50[counter_Table1][13] + "h " +
                                              str(float(student_info_50[counter_Table1][14]).__round__()).split(".")[
                                                  0] + "m",
                           "STATUS": student_info_50[counter_Table1][15], "color": student_info_50[counter_Table1][19],"DEPARTENT":student_info_50[counter_Table1][7]}
            table_OfStudent_Info_50.append(dataProcess)
            counter_Table1 += 1


        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        return render_template("dashboard admin/compliance_Hk_50.html",profilepicDb=profilepicDb,logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_50)
    except Exception:
        return  redirect(url_for("admin"))
@app.route("/compliance_hk_75")
def compliance_Hk_75():

    try:

        # Qeury Student with 75% hk

        qury.execute("SELECT * FROM `hk_users` WHERE `scholarship` = 'HK75' ")
        student_Info_FromDb_75 = qury.fetchall()

        student_info_75 = []
        for k in student_Info_FromDb_75:
            student_info_75.append(k)

        table_OfStudent_Info_75 = []
        counter_Table1 = 0
        # details to show in profile of the student searched #
        for k in student_info_75:
            std_fullNmae = str(student_info_75[counter_Table1][3]) + " " + str(student_info_75[counter_Table1][2])
            dataProcess = {"STUDENT ID": student_info_75[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                           "COMPLETED HOURS": student_info_75[counter_Table1][5] + "m",
                           "REMAINING HOURS": student_info_75[counter_Table1][13] + "h " +
                                              str(float(student_info_75[counter_Table1][14]).__round__()).split(".")[
                                                  0] + "m",
                           "STATUS": student_info_75[counter_Table1][15], "color": student_info_75[counter_Table1][19],"DEPARTENT":student_info_75[counter_Table1][7]}
            table_OfStudent_Info_75.append(dataProcess)
            counter_Table1 += 1


        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]


        return render_template("dashboard admin/compliance_Hk_75.html",profilepicDb=profilepicDb,logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_75)
    except Exception:
        return redirect(url_for("admin"))
@app.route("/compliance_hk_100")
def compliance_Hk_100():
    try:

        # Qeury Student with 100% hk

        qury.execute("SELECT * FROM `hk_users` WHERE `scholarship` = 'HK100' ")
        student_Info_FromDb_100 = qury.fetchall()

        student_info_100 = []
        for k in student_Info_FromDb_100:
            student_info_100.append(k)

        table_OfStudent_Info_100 = []
        counter_Table1 = 0
        # details to show in profile of the student searched #
        for k in student_info_100:
            std_fullNmae = str(student_info_100[counter_Table1][3]) + " " + str(student_info_100[counter_Table1][2])
            dataProcess = {"STUDENT ID": student_info_100[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                           "COMPLETED HOURS": student_info_100[counter_Table1][5] + "m",
                           "REMAINING HOURS": student_info_100[counter_Table1][13] + "h " +
                                              str(float(student_info_100[counter_Table1][14]).__round__()).split(".")[
                                                  0] + "m",
                           "STATUS": student_info_100[counter_Table1][15], "color": student_info_100[counter_Table1][19],"DEPARTENT":student_info_100[counter_Table1][7]}
            table_OfStudent_Info_100.append(dataProcess)
            counter_Table1 += 1


        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        return render_template("dashboard admin/compliance_Hk_100.html",profilepicDb=profilepicDb,logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_100)
    except Exception:
        return redirect(url_for("admin"))

@app.route("/Duty Assignment And Management")
def DutyAssig():

    try:
        # ------------------------data table for Duty_assignment------------------------
        qury.execute("SELECT * FROM `operation_request`")
        operation_request_DB = qury.fetchall()
        operation_request = []
        for k in operation_request_DB:
            operation_request.append(k)

        table_Assigment_Page_Admin1 = []
        session["assigmentstdList"] =table_Assigment_Page_Admin1
        for k in range(len(operation_request)):
            process = {"DESIGNATION": operation_request[k][0], "REQ": operation_request[k][1],
                       "REPORT DAY/S": operation_request[k][2], "SUPERVISOR": operation_request[k][5],
                       "DEPT": operation_request[k][4], "REQST": operation_request[k][3], "REQ ID": operation_request[k][6]}
            table_Assigment_Page_Admin1.append(process)


        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
        stduentNotAv = qury.fetchall()

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='av' ")
        studentAv = qury.fetchall()


# this is for puting value to the pai charts
        qury.execute("SELECT `department` FROM `hk_users`")
        department_data_db= qury.fetchall()


        coa = []
        coed = []
        cite = []
        com = []
        ccje = []
        coe = []
        cahs = []
        come = []
        for k in department_data_db:

            if str(k[0]).upper() == "COA":
                coa.append(str(k[0]).upper())
            elif str(k[0]).upper() =="COED":
                coed.append(str(k[0]).upper())
            elif str(k[0]).upper() =="CITE":
                cite.append(str(k[0]).upper())
            elif str(k[0]).upper() =="COM":
                com.append(str(k[0]).upper())
            elif str(k[0]).upper() =="CCJE":
                ccje.append(str(k[0]).upper())
            elif str(k[0]).upper() =="COE":
                coe.append(str(k[0]).upper())
            elif str(k[0]).upper() =="CAHS":
                cahs.append(str(k[0]).upper())
            elif str(k[0]).upper() =="COME":
                come.append(str(k[0]).upper())

        # to display how many hk student there are
        qury.execute("SELECT * FROM `hk_users`")
        number_of_stndt = qury.fetchall()

        complirate = (len(stduentNotAv) / len(number_of_stndt)) * 100



        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        return render_template("dashboard admin/assignment.html",
                               profilepicDb=profilepicDb,
                               logUser=session["adminUser"],
                               table_Assigment_Page_Admin = table_Assigment_Page_Admin1
                               ,stduentNotAv=len(studentAv),studentAv=len(stduentNotAv)
                               ,coa = len(coa), coed = len(coed),cite = len(cite),
                               com = len(com),ccje = len(ccje),coe = len(coe),
                               cahs = len(cahs),come = len(come) ,complirate=str(complirate.__round__())+"%",
                               number_of_stndt=len(number_of_stndt))
    except Exception:

        return redirect(url_for("admin"))
#---------------for announcment methodss
@app.route("/Announcement", methods=['POST'])
def Announcement():


    try:

        # Get current date
        tday = datetime.date.today()
        # Get the current time
        current_time = datetime.datetime.now()
        curtime =str(current_time.hour)+":"+str(current_time.minute)

        announcemnet = request.form.get('comment')


        #INSERT ANNOUNCMENT TO DB
        qury.execute("INSERT INTO `reports/announcement`(`content`, `date`, `time`, `adminName`)"
                    " VALUES ('"+announcemnet+"','"+str(tday)+"','"+str(curtime)+"','"+session["adminUser"]+"')")
        conn.commit()

        #======================================
        qury.execute("SELECT * FROM `operation_request`")
        operation_request_DB = qury.fetchall()
        operation_request = []
        for k in operation_request_DB:
            operation_request.append(k)

        table_Assigment_Page_Admin1 = []
        session["assigmentstdList"] = table_Assigment_Page_Admin1
        for k in range(len(operation_request)):
            process = {"DESIGNATION": operation_request[k][0], "REQ": operation_request[k][1],
                       "REPORT DAY/S": operation_request[k][2], "SUPERVISOR": operation_request[k][5],
                       "DEPT": operation_request[k][4], "REQST": operation_request[k][3], "REQ ID": operation_request[k][6]}
            table_Assigment_Page_Admin1.append(process)

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
        stduentNotAv = qury.fetchall()

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='av' ")
        studentAv = qury.fetchall()

        # this is for puting value to the pai charts
        qury.execute("SELECT `department` FROM `hk_users`")
        department_data_db = qury.fetchall()

        coa = []
        coed = []
        cite = []
        com = []
        ccje = []
        coe = []
        cahs = []
        come = []
        for k in department_data_db:

            if str(k[0]).upper() == "COA":
                coa.append(str(k[0]).upper())
            elif str(k[0]).upper() == "COED":
                coed.append(str(k[0]).upper())
            elif str(k[0]).upper() == "CITE":
                cite.append(str(k[0]).upper())
            elif str(k[0]).upper() == "COM":
                com.append(str(k[0]).upper())
            elif str(k[0]).upper() == "CCJE":
                ccje.append(str(k[0]).upper())
            elif str(k[0]).upper() == "COE":
                coe.append(str(k[0]).upper())
            elif str(k[0]).upper() == "CAHS":
                cahs.append(str(k[0]).upper())
            elif str(k[0]).upper() == "COME":
                come.append(str(k[0]).upper())

        # to display how many hk student there are
        qury.execute("SELECT * FROM `hk_users`")
        number_of_stndt = qury.fetchall()

        complirate = (len(stduentNotAv) / len(number_of_stndt)) * 100

        #======================================





        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        return render_template("dashboard admin/assignment.html",
                               logUser=session["adminUser"],
                               table_Assigment_Page_Admin = session["assigmentstdList"],
                               profilepicDb=profilepicDb, stduentNotAv=len(studentAv), studentAv=len(stduentNotAv)
                               , coa=len(coa), coed=len(coed), cite=len(cite),
                               com=len(com), ccje=len(ccje), coe=len(coe),
                               cahs=len(cahs), come=len(come), complirate=str(complirate.__round__()) + "%",
                               number_of_stndt=len(number_of_stndt)
                               )
    except Exception:
        return '<script>alert("Dont use apostrophe");window.location="/Duty Assignment And Management"</script>'

 # to assign a studen to a faculty
techer = []


@app.route("/Duty Assignment", methods=['POST'])
def DutyAssig_process():
    # messages = request.args['h'] mag pass value halin sa url_for


    hkDESIGNATION = request.form['hkDESIGNATION']
    supervi = request.form['operations_Id_Selected']
    reqid = request.form['operationId']

    session["supervi"] = supervi
    session['reqid'] = reqid




    session['hkDESIGNATION'] = hkDESIGNATION
    techer.append(supervi)
    #   to filter out the student by the request requirements
    std_dept = request.form['std_dept']
    std_yr_lvl = request.form['std_yr_lvl']

    qury.execute("SELECT `idnum`, `lname`, `fname`,`program_course`, `department`, `yrLvL` FROM `hk_users` WHERE `Status_avail` = 'av' AND `yrLvL`= '"+std_yr_lvl+"' AND `department` = '"+std_dept+"' ")
    student_db_data = qury.fetchall()
    avil_std_list = []
    for k in student_db_data:
        avil_std_list.append(k)




    table_avil_std =[]
    for k in range (len(avil_std_list)):#table of request of the teacher from operations
        table = {"STUDENT ID":avil_std_list[k][0],"SCHOLAR NAME":avil_std_list[k][1]+" "+avil_std_list[k][2],"YEAR LVL":avil_std_list[k][3],"PROGRAM":avil_std_list[k][4], "DEPARTMENT":avil_std_list[k][5]}
        table_avil_std.append(table)

    # to display std whitout assigmnt
    qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
    stduentNotAv = qury.fetchall()

    # to display std whitout assigmnt
    qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='av' ")
    studentAv = qury.fetchall()

    # this is for puting value to the pai charts
    qury.execute("SELECT `department` FROM `hk_users`")
    department_data_db = qury.fetchall()

    coa = []
    coed = []
    cite = []
    com = []
    ccje = []
    coe = []
    cahs = []
    come = []
    for k in department_data_db:

        if str(k[0]).upper() == "COA":
            coa.append(str(k[0]).upper())
        elif str(k[0]).upper() == "COED":
            coed.append(str(k[0]).upper())
        elif str(k[0]).upper() == "CITE":
            cite.append(str(k[0]).upper())
        elif str(k[0]).upper() == "COM":
            com.append(str(k[0]).upper())
        elif str(k[0]).upper() == "CCJE":
            ccje.append(str(k[0]).upper())
        elif str(k[0]).upper() == "COE":
            coe.append(str(k[0]).upper())
        elif str(k[0]).upper() == "CAHS":
            cahs.append(str(k[0]).upper())
        elif str(k[0]).upper() == "COME":
            come.append(str(k[0]).upper())

    qury.execute("SELECT * FROM `hk_users`")
    number_of_stndt = qury.fetchall()

    complirate = (len(stduentNotAv) / len(number_of_stndt)) * 100

    qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
    profilepicDb = qury.fetchall()[0][0]
    return render_template("dashboard admin/assignment.html",
                           logUser=session["adminUser"],profilepicDb=profilepicDb,
                           table_Assigment_Page_Admin=session["assigmentstdList"]
                           ,table_avil_std=table_avil_std ,supervi=supervi
                           ,stduentNotAv=len(stduentNotAv),studentAv=len(studentAv)
                           ,coa = len(coa), coed = len(coed),cite = len(cite),
                            com = len(com),ccje = len(ccje),coe = len(coe),
                            cahs = len(cahs),come = len(come),complirate=str(complirate.__round__())+"%",number_of_stndt=len(number_of_stndt))




@app.route("/Assigment_modal_process", methods =['POST'])
def Assigment_modal_process():

    try:

        checkList = request.form.getlist("selected_std")

        tc_selected = techer[len(techer)-1]

        session["supervi"]
        session['reqid']

        qury.execute("SELECT `Request` FROM `operation_request` WHERE `ID` = '"+session['reqid']+"'")
        req_Process_for_assigning_duty = qury.fetchall()




        if int(req_Process_for_assigning_duty[0][0]) == len(checkList):
    #       to assign a student to selected teacher
            for k in checkList:

                qury.execute(
                    "INSERT INTO `hk_assignd_teaecher`(`operatikon_ID`, `hk_ID`) VALUES ('" + tc_selected + "','" + k + "')")
                conn.commit()
                #to update if the std is avilable
                qury.execute("UPDATE `hk_users` SET `Status_avail`='Na' WHERE `idnum` = '" + k + "' ")
                conn.commit()

                # to update the sipervisor of the student in the student rec
                qury.execute("UPDATE `hk_users` SET `dutySupervisor`='"+str(session["supervi"])+"' WHERE `idnum` = '" + k + "'")
                conn.commit()

                #to update the DUTY DESIGNATION
                qury.execute("UPDATE `hk_users` SET `dutyDesignation`='"+session['hkDESIGNATION']+"'WHERE `idnum` = '" + k + "' ")
                conn.commit()

            #to remove the rows in the website
            qury.execute("SELECT * FROM `operation_request` WHERE `ID`='"+session['reqid']+"'")
    #       to remove the requst from list
            dataTodel=list(qury.fetchall()[0])

            tableTodel = {"DESIGNATION":dataTodel[0],"REQ":dataTodel[1], "REPORT DAY/S":dataTodel[2],"SUPERVISOR":dataTodel[5],"DEPT":dataTodel[4],"REQST":dataTodel[3],"REQ ID":dataTodel[6]}

            session["assigmentstdList"].remove(tableTodel)
            qury.execute("DELETE FROM `operation_request` WHERE `ID`='"+session['reqid']+"'")
            conn.commit()




        elif len(checkList) < int(req_Process_for_assigning_duty[0][0]) :
            for k in checkList:

                qury.execute(
                    "INSERT INTO `hk_assignd_teaecher`(`operatikon_ID`, `hk_ID`) VALUES ('" + tc_selected + "','" + k + "')")
                conn.commit()


                # to update the sipervisor of the student in the student rec
                qury.execute("UPDATE `hk_users` SET `Status_avail`='Na' WHERE `idnum` = '" + k + "' ")
                conn.commit()

                # to update the sipervisor of the student in the student rec

                qury.execute("UPDATE `hk_users` SET `dutySupervisor`='"+str(session["supervi"])+"' WHERE `idnum` = '" + k + "'")
                conn.commit()

                # to update the DUTY DESIGNATION
                qury.execute("UPDATE `hk_users` SET `dutyDesignation`='" + session[
                    'hkDESIGNATION'] + "'WHERE `idnum` = '" + k + "' ")
                conn.commit()


            req_need_std = int(req_Process_for_assigning_duty[0][0])-len(checkList)
            qury.execute("UPDATE `operation_request` SET `Request`='"+str(req_need_std)+"' WHERE `ID` ='"+session['reqid']+"' ")
            conn.commit()
        elif len(checkList) > int(req_Process_for_assigning_duty[0][0]):
            return '<script>alert("Exceeded number of request!!");window.location="/Duty Assignment And Management"</script>'
        else:
            pass

        techer.clear()
        session.pop("supervi", None)
        session.pop("reqid", None)

        return redirect(url_for("DutyAssig"))

    except Exception:
        return redirect(url_for('DutyAssig'))




#-----------------------------------------------------------------------------------------------------------------------




@app.route("/User Management")
def UserManagement():
    # try:


    qury.execute("SELECT `Faculty_Lname` FROM `operations_data`")
    operations_lname = qury.fetchall()

    qury.execute("SELECT `Faculty_Fname` FROM `operations_data`")
    operations_fname = qury.fetchall()

    qury.execute("SELECT  `Operation_Dept` FROM `operations_data`")
    operations_department = qury.fetchall()

    qury.execute("SELECT `Operations_Mname` FROM `operations_data`")
    operations_Mname = qury.fetchall()

    qury.execute("SELECT `Operation_Designation-Position` FROM `operations_data`")
    operations_Designate = qury.fetchall()

    qury.execute("SELECT `status_ol` FROM `operations_data`")
    status_ol = qury.fetchall()

    qury.execute("SELECT `color_status` FROM `operations_data`")
    color_status = qury.fetchall()

    qury.execute("SELECT `Faculty_Id_Number` FROM `operations_data`")
    operations_Id_number = qury.fetchall()

    operations_table =[]
    operations_counter = 0
    x=0
    for k in operations_lname:
        tbl = {"USER_ID":operations_Id_number[operations_counter][0], "NAME":str(operations_fname[operations_counter][0])+" "+str(k[0]), "DESIGNATION":operations_Designate[operations_counter][0],"DEPARTMENT":operations_department[operations_counter][0],"STATUS":status_ol[operations_counter][0],"color_status":color_status[operations_counter][0],"id":x}
        operations_table.append(tbl)
        operations_counter += 1
        x+=1

    qury.execute("SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`,`Operation_Designation-Position` FROM `opertaion_req_acc`")
    operation_req_acc_data_db = qury.fetchall()



    operation_req_acc_Table = []
    for k in operation_req_acc_data_db:
        table = {"EMP ID":k[2], "NAME":str(k[1])+" "+str(k[0])+" "+str(k[4]), "POSITION":k[5], "DEPARTMENT":k[3]}
        operation_req_acc_Table.append(table)



    qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
    profilepicDb = qury.fetchall()[0][0]







    return render_template("dashboard admin/UserManagement.html",logUser=session["adminUser"],profilepicDb=profilepicDb,operations_table=operations_table, operation_req_acc_Table=operation_req_acc_Table)

    # except Exception:
    #         return redirect(url_for("admin"))

    #this is for passing value to modal operations details
@app.route('/get_faculty_info', methods=['POST'])
def get_faculty_info():
    qury.execute("SELECT `Faculty_Lname` FROM `operations_data`")
    operations_lname = qury.fetchall()

    qury.execute("SELECT `Faculty_Fname` FROM `operations_data`")
    operations_fname = qury.fetchall()

    qury.execute("SELECT  `Operation_Dept` FROM `operations_data`")
    operations_department = qury.fetchall()

    qury.execute("SELECT `Operations_Mname` FROM `operations_data`")
    operations_Mname = qury.fetchall()

    qury.execute("SELECT `Operation_Designation-Position` FROM `operations_data`")
    operations_Designate = qury.fetchall()

    qury.execute("SELECT `status_ol` FROM `operations_data`")
    status_ol = qury.fetchall()

    qury.execute("SELECT `color_status` FROM `operations_data`")
    color_status = qury.fetchall()

    qury.execute("SELECT `Faculty_Id_Number` FROM `operations_data`")
    operations_Id_number = qury.fetchall()

    qury.execute("SELECT `Operations_Email` FROM `operations_data`")
    operations_email = qury.fetchall()

    qury.execute("SELECT `Address` FROM `operations_data`")
    operations_adress = qury.fetchall()

    qury.execute("SELECT `Operation_phone_Number` FROM `operations_data`")
    operations_Phone = qury.fetchall()

    qury.execute("SELECT `operations_about` FROM `operations_data`")
    operations_about = qury.fetchall()



    qury.execute("SELECT `twitter` FROM `operations_data`")
    operations_twiiter = qury.fetchall()

    qury.execute("SELECT `facebook` FROM `operations_data`")
    operations_fb = qury.fetchall()

    qury.execute("SELECT `instagram` FROM `operations_data`")
    operations_insta = qury.fetchall()

    qury.execute("SELECT `linkedin` FROM `operations_data`")
    operations_linkIn = qury.fetchall()

    qury.execute("SELECT `profilePics` FROM `operations_data`")
    operations_Pic = qury.fetchall()


    operations_table = []
    operations_counter = 0
    x = 0
    for k in operations_lname:
        tbl = {"USER_ID": operations_Id_number[operations_counter][0],
               "NAME": str(operations_fname[operations_counter][0]) + " " + str(k[0]),
               "DESIGNATION": operations_Designate[operations_counter][0],
               "DEPARTMENT": operations_department[operations_counter][0], "STATUS": status_ol[operations_counter][0],
               "color_status": color_status[operations_counter][0],"id":x, "email":operations_email[operations_counter][0],
               "Address":operations_adress[operations_counter][0],"phone":operations_Phone[operations_counter][0],
               "about":operations_about[operations_counter][0],"twitter":operations_twiiter[operations_counter][0],
               "fb": operations_fb[operations_counter][0],"insta":operations_insta[operations_counter][0],
               "linkIn": operations_linkIn[operations_counter][0], "pic": operations_Pic[operations_counter][0]

               }
        x+=1
        operations_table.append(tbl)
        operations_counter += 1

    qury.execute(
        "SELECT `Faculty_Lname`, `Faculty_Fname`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`,`Operation_Designation-Position` FROM `opertaion_req_acc`")
    operation_req_acc_data_db = qury.fetchall()
    ope_id = "" # use to qury data to show in modal
    id_checker_Minus = []
    id_splitNum = []
    faculty_id = request.form['faculty_id'] # from javascrip
    for k in range (len(operations_table)):
        id_checker_Minus.append(operations_table[k]['USER_ID'])


    ope_id = id_checker_Minus[int(faculty_id)]


    selected_faculty = next((row for row in operations_table if row['id'] == int(faculty_id)), None)


    # Fetch specific data based on faculty_id

    return jsonify(selected_faculty)



@app.route("/request_modal_Process_User_Management", methods = ['POST'])
def request_modal_Process_User_Management():

    delbtn = request.form.get('del')
    conbtn = request.form.get('con')
    confirmation = str(delbtn)+str(conbtn)

    if confirmation.split(">>")[0] == "del":

        register_Id = str(delbtn).split(">>")[1]
        qury.execute("DELETE FROM `opertaion_req_acc` WHERE `Faculty_Id_Number` = '"+register_Id+"'")
        conn.commit()
    else:



        register_Id = str(conbtn).split(">>")[1]
#       this line of code is if the admin approve the user can log in
        qury.execute("SELECT `Faculty_Password` FROM `opertaion_req_acc` WHERE  `Faculty_Id_Number`= '"+register_Id+"'")
        req_Pass = qury.fetchall()[0][0]
        new_data_cred = str(register_Id) + " " + str(req_Pass)
        faculty_credintials.append(new_data_cred)


        qury.execute("SELECT * FROM `opertaion_req_acc` WHERE `Faculty_Id_Number` = '"+register_Id+"'")
        data_to_Aprove = qury.fetchall()


        # to add the new user to the list so it can sign up
        add_user_data = str(data_to_Aprove[0][3]) + " " + str(data_to_Aprove[0][2])
        credintials.append(add_user_data)

        qury.execute("INSERT INTO `operations_data`(`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`) VALUES "
                     "('"+str(data_to_Aprove[0][0])+"','"+str(data_to_Aprove[0][1])+"','"+str(data_to_Aprove[0][2])+"','"+str(data_to_Aprove[0][3])+"','"+str(data_to_Aprove[0][4])+"','"+str(data_to_Aprove[0][5])+"','"+str(data_to_Aprove[0][6])+"','"+str(data_to_Aprove[0][7])+"','"+str(data_to_Aprove[0][8])+"')")
        conn.commit()


        qury.execute("DELETE FROM `opertaion_req_acc` WHERE `Faculty_Id_Number` = '" + register_Id + "'")
        conn.commit()

        qury.execute("UPDATE `operations_data` SET `status_ol`='INACTIVE',`color_status`='danger' WHERE `Faculty_Id_Number` = '" + register_Id + "' ")
        conn.commit()





    return redirect(url_for('UserManagement'))


@app.route("/modal_add_user", methods=['POST'])
def modal_add_user():
    empid = request.form['empid']
    lname = request.form['lname']
    fname = request.form['fname']
    mname = request.form['mname']
    email = request.form['email']
    phone = request.form['phone']
    dept = request.form.get('dept')
    Designation = request.form.get('Designation')
    psw = request.form['psw']

    #to add the new user to the list so it can sign up

    hashed_password = bcrypt.hashpw(psw.encode(), bcrypt.gensalt())# to encrypt password
    add_user_data = str(empid)+" "+str(hashed_password.decode())
    faculty_credintials.append(add_user_data)


    qury.execute(
        "INSERT INTO `operations_data`(`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`) VALUES "
        "('" + str(lname) + "','" + str(fname) + "','" + str(hashed_password.decode()) + "','" + str(empid) + "','" + str(dept) + "','" + str(mname) + "','" + str(phone) + "','" + str(Designation) + "','" + str(email) + "')")
    conn.commit()

    qury.execute(
        "UPDATE `operations_data` SET `status_ol`='INACTIVE',`color_status`='danger' WHERE `Faculty_Id_Number` = '" + empid + "' ")
    conn.commit()

    return redirect(url_for('UserManagement'))


#for modal details in user management




@app.route("/Export to Excel")
def Excel():
    try:
        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]
        return render_template("dashboard admin/Excel.html",logUser=session["adminUser"],profilepicDb=profilepicDb)
    except Exception:
        return redirect(url_for("admin"))
@app.route("/Setting and Configurations")
def Setting():
    try:
        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]


        #get data from admin db to display in front end using jinja
        qury.execute("SELECT `userName`, `About`, `Phone`, `Address`, `Email`, `Twitter`, `Facebook`, `Instagram`, `Linkedin` ,`adminIdNumber` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        adminData = qury.fetchall()


        return render_template("dashboard admin/Setting.html",logUser=session["adminUser"],profilepicDb=profilepicDb,fullName=adminData[0][0],about=adminData[0][1],phone=adminData[0][2],Address = adminData[0][3],emailacc=adminData[0][4],twitter=adminData[0][5],facebook=adminData[0][6],instagram=adminData[0][7],linkedin=adminData[0][8], adminId =adminData[0][8+1])
    except Exception:
        return redirect(url_for("admin"))


@app.route("/uplaodProfile_admin", methods=['POST']) #to upate profile picture of operations
def uplaodProfile_admin():

    try:
        profilePic = request.files['file']
        if str(profilePic) != "<FileStorage: '' ('application/octet-stream')>":
            try:
                profilePic.save(os.path.join(app.config['UPLOAD_DIR']+secure_filename(profilePic.filename)))
                qury.execute("UPDATE `admin` SET `profilePics`='"+str(secure_filename(profilePic.filename))+"' WHERE  `adminIdNumber` = '"+session["userIdAdmin"]+"' ")
                conn.commit()

                FullName = request.form['fulltName']
                about = request.form['about']
                phone = request.form['phone']
                address = request.form['Address']
                Email = request.form['email']
                Twitter  = request.form['twitter']
                Facebook  = request.form['facebook']
                Instagram  = request.form['instagram']
                Linkedin  = request.form['linkedin']

                qury.execute("UPDATE `admin` SET `userName`='"+str(FullName)+"',`About`='"+str(about)+"',`Phone`='"+str(phone)+"'"
                            ",`Address`='"+str(address)+"',`Email`='"+str(Email)+"',`Twitter`='"+str(Twitter)+"',`Facebook`='"+str(Facebook)+"'"
                            ",`Instagram`='"+str(Instagram)+"',`Linkedin`='"+str(Linkedin)+"' WHERE `adminIdNumber` = '"+str(session["userIdAdmin"])+"'")
                conn.commit()

                return redirect(url_for("Setting"))
            except Exception:
                return '<script>alert("Dont use apostrophe");window.location="/Setting and Configurations"</script>'
        else:
            try:

                FullName = request.form['fulltName']
                about = request.form['about']
                phone = request.form['phone']
                address = request.form['Address']
                Email = request.form['email']
                Twitter = request.form['twitter']
                Facebook = request.form['facebook']
                Instagram = request.form['instagram']
                Linkedin = request.form['linkedin']

                qury.execute(
                    "UPDATE `admin` SET `userName`='" + str(FullName) + "',`About`='" + str(about) + "',`Phone`='" + str(
                        phone) + "'"
                                 ",`Address`='" + str(address) + "',`Email`='" + str(Email) + "',`Twitter`='" + str(
                        Twitter) + "',`Facebook`='" + str(Facebook) + "'"
                                                                      ",`Instagram`='" + str(
                        Instagram) + "',`Linkedin`='" + str(Linkedin) + "' WHERE `adminIdNumber` = '" + str(
                        session["userIdAdmin"]) + "'")
                conn.commit()


                return redirect(url_for("Setting"))
            except Exception:
                return '<script>alert("Dont use apostrophe");window.location="/Setting and Configurations"</script>'

    except RequestEntityTooLarge:
        return '<script>alert("file to large");window.location="/Setting and Configurations"</script>'




@app.route("/semester_change", methods =['POST'])
def semester_change():
    semester = request.form.get('semester')
    qury.execute("UPDATE `hk_users` SET `semister`='"+str(semester)+"' ")
    conn.commit()

    return redirect(url_for('Setting'))

@app.route("/change_admin_password", methods = ['POST'])
def change_admin_password():


    currentPass = request.form['password']
    newPass = request.form['newpassword']


    if currentPass in adminuserpassWord:


        qury.execute("UPDATE `admin` SET `passWord`='"+str(newPass)+"' WHERE `adminIdNumber` = '"+session["userIdAdmin"]+"'")
        conn.commit()

        adminuserpassWord.insert(adminuserpassWord.index(str(currentPass)),str(newPass))
        adminuserpassWord.remove(str(currentPass))
        admin_cridentials.insert(admin_cridentials.index(str(session["userIdAdmin"])+" "+str(currentPass)),str(session["userIdAdmin"])+" "+str(newPass))
        admin_cridentials.remove(str(session["userIdAdmin"])+" "+str(currentPass))
        return redirect(url_for('Setting'))
    else:
        return redirect(url_for('Setting'))


@app.route("/System Health Logs")
def Systemhealth():
    try:

        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        qury.execute("SELECT * FROM `active_logs` WHERE 1")
        active_log_data_db = qury.fetchall()

        activity_log_table = []

        for k in active_log_data_db:
            tables= {"Date and Time":k[1],"ID":k[2],"USER":k[3],"DEPT":k[4],"ACT PERM":k[5]}
            activity_log_table.append(tables)

        qury.execute("SELECT * FROM `operation_feedback`")
        feeds = qury.fetchall()

        qury.execute("SELECT * FROM `operation_feedback`")
        total_feed = qury.fetchall()




        return render_template("dashboard admin/Systemhealth.html",logUser=session["adminUser"],
                               profilepicDb=profilepicDb, activity_log_table=activity_log_table,
                               feeds=feeds, total_feed=len(total_feed))
    except Exception:
        return redirect(url_for("admin"))
@app.route("/Feedback and Improvements")
def Feedback():
    try:

        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]
        return render_template("dashboard admin/Feedback.html",logUser=session["adminUser"],profilepicDb=profilepicDb)
    except Exception:
        return redirect(url_for("admin"))
@app.route("/assigment")
def assiment():
    try:


        qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
        profilepicDb = qury.fetchall()[0][0]

        return  render_template("dashboard admin/assignment.html",logUser=session["adminUser"],profilepicDb=profilepicDb)
    except Exception:
        return redirect(url_for("admin"))
@app.route("/student_records")
def student_records():

    try:
        session["adminUser"]
        return render_template("dashboard admin/ScholarRecordAdmin.html")
    except Exception:
        return redirect(url_for("admin"))


@app.route("/student_rec_process", methods=['POST'])
def student_rec_process():

    try:

        if request.form.get('select') == 'select':

            student_Id = request.form.get("Selected_Id")

            qury.execute("SELECT * FROM `hk_users` WHERE `idnum` = '" + str(student_Id) + "'")
            hkdetails = qury.fetchall()  # len of 17

            # details to show in profile of the student searched
            idnum= hkdetails[0][0]  # idnum
            Lname= hkdetails[0][2]  # Lname
            Fname= hkdetails[0][3]  # Fname
            totalDuty= hkdetails[0][5]  # totalDuty
            course_Program= hkdetails[0][6]  # course_Program
            department = hkdetails[0][7]  # department
            yearLvl= hkdetails[0][8]  # yearLvl
            scholarship= hkdetails[0][9]  # scholarship
            DUTY_DESIGNATION = hkdetails[0][10]  # DUTY_DESIGNATION
            DUTY_SUPERVISOR = hkdetails[0][11]  # DUTY_SUPERVISOR
            reqiredDuty = hkdetails[0][12]  # reqiredDuty
            remaningDuty = hkdetails[0][13]  # remaningDuty
            remDutyMin = str(float(hkdetails[0][14]).__round__()).split(".")# remDutyMin
            statsuForRenewal = hkdetails[0][15]  # statsuForRenewal
            Schoolyr = hkdetails[0][16]  # Schoolyr
            semister = hkdetails[0][17]  # semister


            qury.execute("SELECT `profilePics` FROM `admin` WHERE `adminIdNumber`= '" + session["userIdAdmin"] + "'")
            profilepicDb = qury.fetchall()[0][0]


        return render_template("dashboard admin/ScholarRecordAdmin.html",profilepicDb=profilepicDb,idnum=idnum,Lname=Lname,Fname=Fname,totalDuty=totalDuty,
            course_Program=course_Program,department=department,yearLvl=yearLvl,scholarship=scholarship,
            DUTY_DESIGNATION=DUTY_DESIGNATION,DUTY_SUPERVISOR=DUTY_SUPERVISOR,reqiredDuty=reqiredDuty,
            remaningDuty=remaningDuty,statsuForRenewal=statsuForRenewal,Schoolyr=Schoolyr,semister=semister, remDutyMin = remDutyMin[0])
    except Exception:
        return redirect(url_for('compliance'))

#-------------------------END OF ADMIN SIDE BARS------------------
@app.route("/Duty_Records", methods=['POST'])
def Duty_Records():
    try:
        DUTY_Id_Num = request.form.get('Duty_Id')
        session["student_Id_num"]=DUTY_Id_Num

        qury.execute("SELECT * FROM `scholar_duty_records` WHERE `Student_id_Number` = '"+DUTY_Id_Num+"'")
        rec_list_Db = qury.fetchall()


        rec_list = []
        for k in rec_list_Db:
            rec_list.append(k)
        record_table = []


        session["Duty_record_table"] = record_table
        time_in = ""
    #----- solve the renderd duty hours in minutes format-----------
        total_duty = 0
        for k in range (len(rec_list)):

            if rec_list[k][5]=="IN":
                inh = rec_list[k][1]
                inm = rec_list[k][2]
                time_in =  f"{rec_list[k][1]:}:{rec_list[k][2]:02d}"

            elif rec_list[k][5] == "OUT":
                time_out = f"{rec_list[k][1]:}:{rec_list[k][2]:02d}"
                durationoH = int(rec_list[k][1]) - int(inh)
                durationm = int(rec_list[k][2]) - int(inm)
                HourTo_min = durationoH * 60
                totalduty_mins = HourTo_min + durationm
                duration = f"{durationoH:}h {durationm:02d}m"
                total_duty += totalduty_mins
                rec_process = {"DATE": rec_list[k][0], "CHECK-IN TIME": time_in, "CHECK-OUT TIME": time_out, "DURATION": duration}
                record_table.append(rec_process)

                qury.execute("UPDATE `hk_users` SET `id_totalHours`='"+str(total_duty)+"' WHERE `idnum` = '" + DUTY_Id_Num + "' ")
                conn.commit()


        return render_template("dashboard admin/dutyrecords.html", DUTY_Id_Num =DUTY_Id_Num, record_table= record_table)
    except Exception:
        return redirect(url_for('compliance'))




#--------------------------Terminals----------------------


@app.route("/terminal")
def terminal():

    return render_template("Terminal/terminal.html")


@app.route("/StudentTimeIN_Out", methods=['POST'])
def StudentTimeIN_Out():
    # Get current date
    tday = datetime.date.today()
    # Get the current time
    current_time = datetime.datetime.now()
    current_date = datetime.date.today()
    # Extract the year, mont, day, hours, and minutes
    current_hour = current_time.hour
    current_minute = current_time.minute
    yr =current_date.year
    month = current_date.month
    date = current_date





    #checker if the id number had sign in or not
    time_In_Out = request.form.get('login')
    stdId = request.form['idstndt']
    total_duty = 0


    #data need for activity logs
    datez = str(datetime.datetime.now()).split(":")[0] + ":" + str(datetime.datetime.now()).split(":")[1]
    qury.execute("SELECT * FROM `hk_users` WHERE `idnum` = '" + stdId + "'")
    hkdetails = qury.fetchall()  # len of 17
    Lname = hkdetails[0][2]  # Lname
    Fname = hkdetails[0][3]  # Fname
    fullname = str(Fname)+" "+str(Lname)
    department = hkdetails[0][7]  # department

    try:
        if  time_In_Out == "IN":
            #to record activity od hk
            qury.execute("INSERT INTO `hk_user_activelogs`(`date_time`, `hk_id`, `hk_name`, `dept`, `act_perm`)"
                         " VALUES ('"+str(datez)+"','"+str(stdId)+"','"+str(fullname)+"','"+str(department)+"','Sing in')")
            conn.commit()

            # to check if the user already sign in and need to sign out
            if stdId in list_of_sign_in:
                errormess = "You already Sign in"
                return render_template("Terminal/terminal.html", errormess=errormess)
            # to check if the user already sign in and need to sign out


            else:
                #to insert the time in time
                timeInList.append(current_hour)# index 0
                timeInList.append(current_minute)# index 1
                list_of_sign_in.append(stdId)

                qury.execute("INSERT INTO `scholar_duty_records`"
                             "(`date`,`Hours_In_Out`, "
                             "`Minutes_In_Out`, `Student_id_Number`, "
                             "`Type_of_Process`) VALUES "
                             "('" + str(date) + "','" + str(current_hour) + "','" + str(current_minute) + "','" + stdId + "','" + time_In_Out + "')")
                conn.commit()
                #to insert the time in time


                #to get the name who sing in and out by id input
                qury.execute("SELECT `lname`, `fname` FROM `hk_users` WHERE `idnum` = '" + stdId + "' ")
                fullname = qury.fetchall()
                fname = fullname[0][1]
                lname = fullname[0][0]
                #to get the name who sing in and out


                return render_template("Terminal/terminal.html", tday=tday, hours=current_hour, mins=current_minute,time_In_Out=time_In_Out, stdId=stdId, fname=fname, lname=lname)
            return render_template("Terminal/terminal.html")


        elif time_In_Out =="OUT":
            # to record activity od hk
            qury.execute("INSERT INTO `hk_user_activelogs`(`date_time`, `hk_id`, `hk_name`, `dept`, `act_perm`)"
                         " VALUES ('" + str(datez) + "','" + str(stdId) + "','" + str(fullname) + "','" + str(
                department) + "','Sing out')")
            conn.commit()
            list_of_sign_in.remove(stdId)

            qury.execute("SELECT * FROM `scholar_duty_records` WHERE `Student_id_Number` = '" + stdId + "'")
            rec_list_Db = qury.fetchall()

            rec_list = []
            for k in rec_list_Db:
                rec_list.append(k)

        # ----- solve the renderd duty hours in minutes format-----------
            record_table = []
            time_in = ""

            for k in range(0,int(len(rec_list))):

                if rec_list[k][5] == "IN":
                    inh = rec_list[k][1]
                    inm = rec_list[k][2]
                    time_in = f"{rec_list[k][1]:}:{rec_list[k][2]:02d}"

                elif rec_list[k][5] == "OUT":
                    time_out = f"{rec_list[k][1]:}:{rec_list[k][2]:02d}"
                    durationoH = int(rec_list[k][1]) - int(inh)
                    durationm = int(rec_list[k][2]) - int(inm)
                    HourTo_min = durationoH * 60
                    totalduty_mins = HourTo_min + durationm


                    total_duty += totalduty_mins

                    duration = f"{durationoH:}h {durationm:02d}m"
                    rec_process = {"DATE": rec_list[k][0], "CHECK-IN TIME": time_in, "CHECK-OUT TIME": time_out,
                                   "DURATION": duration}
                    record_table.append(rec_process)

                    #update the renderd duty-----
                    qury.execute("UPDATE `hk_users` SET `id_totalHours`='" + str(
                        total_duty) + "' WHERE `idnum` = '" + stdId + "' ")
                    conn.commit()
                    #update the renderd duty-----


            #----------------------formulation of reminin duty hours
            timInHour = (float(timeInList[0])*60)
            timeInMin = (float(timeInList[1])+timInHour)
            timeOutHours = (float(current_hour)*60)
            timeOutMin = (float(current_minute)+timeOutHours)
            renderedDutyToday = (timeOutMin - timeInMin)


            qury.execute("SELECT `remaningDuty`, `remDutyMins`FROM `hk_users` WHERE `idnum` = '" + stdId + "'")
            remdutyDb = qury.fetchall()
            remdutymins = (float(remdutyDb[0][1]))
            remduty = (float(remdutyDb[0][0])*60)+remdutymins


            remdutyMins = remduty - renderedDutyToday
            remdutyHoursConverstion = str(remdutyMins / 60).split(".")
            remdutyHours = remdutyHoursConverstion[0]
            remdutyMinscpnvertion = (float("0."+remdutyHoursConverstion[1])*60)

            qury.execute("UPDATE `hk_users` SET `remaningDuty`='"+str(remdutyHours)+"',`remDutyMins`='"+str(remdutyMinscpnvertion)+"' WHERE `idnum` = '"+stdId+"'")
            conn.commit()
            timeInList.clear()
            #------------------formulation of remainin duty hours

            qury.execute("INSERT INTO `scholar_duty_records`"
                         "(`date`,`Hours_In_Out`, "
                         "`Minutes_In_Out`, `Student_id_Number`, "
                         "`Type_of_Process`) VALUES "
                         "('" + str(date) + "','" + str(current_hour) + "','" + str(
                current_minute) + "','" + stdId + "','" + time_In_Out + "')")
            conn.commit()
            qury.execute("SELECT `lname`, `fname` FROM `hk_users` WHERE `idnum` = '" + stdId + "' ")
            fullname = qury.fetchall()
            fname = fullname[0][1]
            lname = fullname[0][0]

            return render_template("Terminal/terminal.html", tday=tday, hours=current_hour, mins=current_minute,time_In_Out=time_In_Out, stdId=stdId, fname=fname, lname=lname)


    except Exception:
        errormess = "Sign in first"


    return render_template("Terminal/terminal.html", errormess =errormess  )


if __name__ == "__main__":
    app.run(debug=True)


    ### end ###