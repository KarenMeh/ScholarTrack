import os

from flask import  Flask, render_template, request, redirect, url_for, session, flash
from flaskext.mysql import MySQL
import datetime

from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "i love you cute"
mysql = MySQL()

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

#----student id numbers---
qury.execute("SELECT `idnum` FROM `hk_users`")
idnumberStdnt = qury.fetchall()
stdntIdNumberAvilable =[]
for k in idnumberStdnt:
    stdntIdNumberAvilable.append(k[0])
print(stdntIdNumberAvilable)



#------------------------admin side request data--------------------------------

qury.execute("SELECT `email`, `date`, `timeIn`, `timeOut`, `id` FROM `request` WHERE 1 ")
reqdata = qury.fetchall()

reqdataList = []
for i in reqdata:
    reqdataList.append(i)
print(reqdataList)



#storage for admin usernames dont delete this
adminls = []
#------------admin data---------------------


qury.execute("SELECT `adminIdNumber` FROM `admin` ")
adminUsername = qury.fetchall()

adminusernamels=[]
for k in adminUsername:
    adminusernamels.append(k[0])
print(adminusernamels)

qury.execute("SELECT `passWord` FROM `admin` ")
adminpass = qury.fetchall()

adminuserpassWord=[]
for k in adminpass:
    adminuserpassWord.append(k[0])
print(adminuserpassWord)

admin_cridentials = []
indexadmin = 0
for i in adminusernamels:
    admin_cridentials.append(i +" "+ adminuserpassWord[indexadmin])
    indexadmin+=1
print(admin_cridentials)


#-----------------operations Datas-------------------------------------------

qury.execute("SELECT `Faculty_Id_Number` FROM `operations_data`")
Faculty_Id_Number = qury.fetchall()

faculty_id = []
for k in Faculty_Id_Number:
    faculty_id.append(k[0])
print(faculty_id)

qury.execute("SELECT `Faculty_Password`FROM `operations_data`")
Faculty_PassWord = qury.fetchall()

faculty_psw = []
for k in Faculty_PassWord:
    faculty_psw.append(k[0])
print(faculty_psw)

#faculty credintials
faculty_credintials =[]
faculty_counter = 0

for k in faculty_id:
    compress = (k+" "+faculty_psw[faculty_counter])
    faculty_credintials.append(compress)
    faculty_counter+=1
print(faculty_credintials)





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
print(table_Assigment_Page_Admin)



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
    return '<script>alert("Log Out");window.location="/"</script>'


#------------------------------------log out----------------------------------------------
@app.route("/Logout", methods=['POST'])
def logOut():
    session.pop("user",None)
    session.pop("username",None)
    session.pop("lname",None)
    session.pop("fname", None)
    session.pop("assigmentstdList", None)
    session.pop("opration_Id", None)
    



    return '<script>alert("Log Out");window.location="/"</script>'


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
    try:

        gmail = request.form["email"]
        password = request.form["psw"]
        repPaswrd = request.form['cnfrpsw']
        idnum = request.form['idnum']
        fname = request.form['fname']
        lname = request.form['lname']
        mname = request.form['Mname']
        phone = request.form['phone']
        Position = request.form['Position']
        dept = request.form['dept']


        if password == repPaswrd:

            faculty_credintials.append(idnum+" "+password)
            qury.execute("INSERT INTO `operations_data`(`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`,"
                         " `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`)"
                         " VALUES ('"+lname+"','"+fname+"','"+password+"','"+idnum+"','"+dept+"','"+mname+"','"+phone+"','"+Position+"','"+gmail+"')")
            conn.commit()

            return '<script>alert("Registered Complete");window.location="/register"</script>'
        else:
            return '<script>alert("wrong pass");window.location="/register"</script>'

    except:

        return '<script>alert("Email already used");window.location="/register"</script>'


#---------------------------------/Sign in-----------------------------------------------------


@app.route("/Sign in")
def signInPAge():
    print(faculty_credintials)
    return render_template("SignIn.html")


@app.route("/signed in", methods= ["POST"])
def signInprocess():

    idNum = request.form['email']
    password = request.form['psw']
    logindata = idNum+" "+password
    session["user"]=idNum

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


        return '<script>alert("Log in");window.location="/Dash board"</script>'

    else:

       
        return '<script>alert("Wrong password or Email");window.location="/Sign in"</script>'



#-------------------------------dash board-----------------------------------------
@app.route("/Dash board")
def Dashboard():

    if "username" in session:

        # to get data reports from db to display
        qury.execute("SELECT `content`, `date`, `time`, `adminName`, `id` FROM `reports/announcement`")
        db_announc_data = qury.fetchall()
        announcment_List = []

        for k in db_announc_data:
            announcment_List.append(k)
        print(announcment_List)
        #       to display date and time
        dateTimeLista_announcment = []
        for k in range(len(announcment_List)):
            dateTimeLista_announcment.append(
                str(announcment_List[k][1]) + " " + str(announcment_List[k][2]) + "\n\n" + str(
                    announcment_List[k][3]) + " >" + str(announcment_List[k][0]))
        print(dateTimeLista_announcment)

        # select profile pic
        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '" + session["user"] + "'")
        profilepicDb = qury.fetchall()[0][0]
        print(profilepicDb)

        # to display how many hk student there are
        qury.execute("SELECT * FROM `hk_users`")
        number_of_stndt = qury.fetchall()

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
        stduentNotAv = qury.fetchall()

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='av' ")
        studentAv = qury.fetchall()

        # comliance rate data
        complirate = (len(stduentNotAv) / len(number_of_stndt)) * 100

        return render_template("dashboard operations/OpartionsDashBoard.html",
                               logUser = session['username'],
                               dateTimeLista_announcment=dateTimeLista_announcment,
                               profilepicDb=profilepicDb,complirate=str(complirate.__round__())+"%",
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
        print("my student",mYStudent_Db_Id)


        for k in mYStudent_Db_Id:
            print(k[0])
            qury.execute("SELECT `idnum`,`lname`, `fname`, `id_totalHours`,  `remaningDuty`, `remDutyMins`,`statsForRenewal` FROM `hk_users` WHERE `idnum`= '"+k[0]+"'")
            listahan.append(qury.fetchall()[0])
        print(listahan)

        student_underMe=[]
        for k in range(len(listahan)):
            tables = {"STUDENT ID":listahan[k][0],"SCHOLAR NAME":listahan[k][1]+" "+listahan[k][2],"COMPLETED HOURS":listahan[k][3],"REMAINING HOURS":listahan[k][4]+"h "+str(float(listahan[k][5]).__round__()).split(".")[0]+"m","STATUS":listahan[k][6]}
            student_underMe.append(tables)
        #select profile pic
        qury.execute("SELECT `profilePics` FROM `operations_data` WHERE `Faculty_Id_Number`= '" + session["user"] + "'")
        profilepicDb = qury.fetchall()[0][0]
        print(profilepicDb)
        return render_template("dashboard operations/requestmanage.html",logUser = session['username'], student_underMe =student_underMe,profilepicDb=profilepicDb)

    except Exception:
        return redirect(url_for("signInPAge"))
@app.route("/Modal_request_process", methods=['POST'])
def Modal_request_process():
    Designation = request.form['Designation']
    Requirements = request.form['Requirements']
    Report_Days = request.form['Report Day/s']
    Request = request.form['Request']

    qury.execute("SELECT `Operation_Dept` FROM `operations_data` WHERE `Faculty_Id_Number` = '"+str(session["user"])+"' ")
    dept = qury.fetchall()
    print(dept[0][0])


    qury.execute("INSERT INTO `operation_request`(`Designation`, `Requirements`, `Report Day/s`, `Request`, `DEPT`, `SUPERVISOR`) VALUES ('"+Designation+"','"+Requirements+"','"+Report_Days+"','"+Request+"', '"+dept[0][0]+"', '"+str(session['lname'])+" "+str(session['fname'])+"') ")
    conn.commit()

    process = {"DESIGNATION": Designation, "REQ": Requirements,
               "REPORT DAY/S": Report_Days, "SUPERVISOR": str(session["lname"])+" "+str(session["fname"]),
               "DEPT":dept[0][0] , "REQST":Request }
    table_Assigment_Page_Admin.append(process)

    return '<script>alert("Request Sent!!");window.location="/Request and Scholar Management"</script>'


#-----------------------------end of operations requesr--------------------------------------------------


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

            qury.execute("UPDATE `operations_data` "
                         "SET `twitter`='"+twitter+"',`facebook`='"+facebook+"',"
                         "`instagram`='"+instagram+"',`linkedin`='"+linkedin+"',"
                         "`operations_about`='"+about+"',`Faculty_Lname`='"+lasttName+"'"
                         ",`Faculty_Fname`='"+firstName+"',`Operation_phone_Number`='"+phone+"'"
                         ",`Operations_Email`='"+email+"',`Address`='"+Address+"' WHERE `Faculty_Id_Number`= "
                         "'"+session["opration_Id"]+"' ")
            conn.commit()
        else:
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

            qury.execute("UPDATE `operations_data` "
                        "SET `twitter`='" + twitter + "',`facebook`='" + facebook + "',"
                        "`instagram`='" + instagram + "',`linkedin`='" + linkedin + "',"
                        "`operations_about`='" + about + "',`Faculty_Lname`='" + lasttName + "'"
                        ",`Faculty_Fname`='" + firstName + "',`Operation_phone_Number`='" + phone + "'"
                        ",`Operations_Email`='" + email + "',`Address`='"+Address+"' WHERE `Faculty_Id_Number`= '" +
                         session["opration_Id"] + "' ")
            conn.commit()








    except RequestEntityTooLarge:
        return '<script>alert("file to large");window.location="/Profile"</script>'




    return redirect(url_for("Profile_Operations"))


@app.route("/change_password_operations", methods=['POST'])
def change_password_operations():

    old_password = request.form['password']
    new_password = request.form['newpassword']
    re_enter_password = request.form['renewpassword']
    print(old_password,new_password,re_enter_password)

    qury.execute("SELECT `Faculty_Password` FROM `operations_data` WHERE `Faculty_Id_Number` = '"+session["opration_Id"]+"'")
    old_password_db = qury.fetchall()[0][0]
    if old_password == old_password_db:
        if new_password == re_enter_password:
            qury.execute("UPDATE `operations_data` SET `Faculty_Password`='"+str(new_password)+"' WHERE `Faculty_Id_Number` = '"+session["opration_Id"]+"' ")
            conn.commit()

            # -----------------operations Datas-------------------------------------------

            faculty_credintials.insert(faculty_credintials.index(session["opration_Id"]+" "+old_password),session["opration_Id"]+" "+new_password)
            faculty_credintials.remove(str(session["opration_Id"]+" "+old_password))



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
    print(timeToDisplay)
    session["duty"]=timeToDisplay
    print(session["duty"])
#this is for remaining duty hours
    target = 10800
    H = int(session["hours"]) * 60
    remM = target - H
    dataTime = str(remM / 60).split(".")
    Hour = dataTime[0]
    Minutes = str(int((float("0." + dataTime[1]) * 60)))
    reamining = str(Hour) + ":" + Minutes
    session["reamining"] =reamining
    print(dataTime)
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

    useraAdmin = request.form['email']
    pswAdmin = request.form['pass']

    qury.execute("SELECT `userName` FROM `admin` WHERE `adminIdNumber` = '"+useraAdmin+"'")
    adminfullname = qury.fetchall()
    session["adminUser"] = adminfullname[0][0]


    check = useraAdmin+" "+pswAdmin
    if check in admin_cridentials:
        return '<script>alert("Welcome");window.location="admindashBoard"</script>'
    else:
        return  '<script>alert("Wrong Credetials!");window.location="/adminLanding"</script>'

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
        print(announcment_List)
#       to display date and time
        dateTimeLista_announcment = []
        for k in range (len(announcment_List)):
            dateTimeLista_announcment.append(str(announcment_List[k][1])+" "+str(announcment_List[k][2])+"\n\n"+str(announcment_List[k][3])+" >"+str(announcment_List[k][0]))
        print(dateTimeLista_announcment)

        # to display how many hk student there are
        qury.execute("SELECT * FROM `hk_users`")
        number_of_stndt = qury.fetchall()

        #to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='Na' ")
        stduentNotAv = qury.fetchall()

        # to display std whitout assigmnt
        qury.execute("SELECT  `Status_avail` FROM `hk_users` WHERE `Status_avail` ='av' ")
        studentAv = qury.fetchall()

        #comliance rate data
        complirate = (len(stduentNotAv)/len(number_of_stndt))*100

        return render_template('dashboard admin/dashboardAdminFinal.html',
                               logUser=session["adminUser"],
                               dateTimeLista_announcment=dateTimeLista_announcment,
                               number_of_stndt=len(number_of_stndt),
                               stduentNotAv=len(stduentNotAv),
                               studentAv=len(studentAv),complirate=str(complirate.__round__())+"%")
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
        print(len(student_info))

        table_OfStudent_Info = []
        counter_Table1 = 0
        # details to show in profile of the student searched #
        for k in student_info:
            std_fullNmae = str(student_info[counter_Table1][3]) + " " + str(student_info[counter_Table1][2])
            dataProcess = {"STUDENT ID": student_info[counter_Table1][0], "SCHOLAR NAME": std_fullNmae,
                           "COMPLETED HOURS": student_info[counter_Table1][5] + "m",
                           "REMAINING HOURS": student_info[counter_Table1][13] + "h " +str(float(student_info[counter_Table1][14]).__round__()).split(".")[0] + "m",
                           "STATUS": student_info[counter_Table1][15]}
            table_OfStudent_Info.append(dataProcess)
            counter_Table1 += 1

        print(table_OfStudent_Info)

        return render_template("dashboard admin/compliance.html", logUser=session["adminUser"],
                               table_OfStudent_Info=table_OfStudent_Info)

    else:
        return redirect(url_for("admin"))

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
                                              str(float(student_info_25[counter_Table1][14]).__round__()).split(".")[0] + "m",
                           "STATUS": student_info_25[counter_Table1][15]}
            table_OfStudent_Info_25.append(dataProcess)
            counter_Table1 += 1


        return render_template("dashboard admin/compliance_Hk_25.html",logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_25)
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
                                              str(float(student_info_50[counter_Table1][14]).__round__()).split(".")[0] + "m",
                           "STATUS": student_info_50[counter_Table1][15]}
            table_OfStudent_Info_50.append(dataProcess)
            counter_Table1 += 1

        return render_template("dashboard admin/compliance_Hk_50.html",logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_50)
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
                                              str(float(student_info_75[counter_Table1][14]).__round__()).split(".")[0] + "m",
                           "STATUS": student_info_75[counter_Table1][15]}
            table_OfStudent_Info_75.append(dataProcess)
            counter_Table1 += 1


        return render_template("dashboard admin/compliance_Hk_75.html",logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_75)
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
                                              str(float(student_info_100[counter_Table1][14]).__round__()).split(".")[0] + "m",
                           "STATUS": student_info_100[counter_Table1][15]}
            table_OfStudent_Info_100.append(dataProcess)
            counter_Table1 += 1

        return render_template("dashboard admin/compliance_Hk_100.html",logUser=session["adminUser"], table_OfStudent_Info = table_OfStudent_Info_100)
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
        print(table_Assigment_Page_Admin1)

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

        print(coa ,coed ,cite ,com ,ccje,coe,cahs,come)


        return render_template("dashboard admin/assignment.html",
                               logUser=session["adminUser"],
                               table_Assigment_Page_Admin = table_Assigment_Page_Admin1
                               ,stduentNotAv=len(studentAv),studentAv=len(stduentNotAv)
                               ,coa = len(coa), coed = len(coed),cite = len(cite),
                               com = len(com),ccje = len(ccje),coe = len(coe),
                               cahs = len(cahs),come = len(come) )
    except Exception:

        return redirect(url_for("admin"))
#---------------for announcment methodss
@app.route("/Announcement", methods=['POST'])
def Announcement():
    # Get current date
    tday = datetime.date.today()
    # Get the current time
    current_time = datetime.datetime.now()
    curtime =str(current_time.hour)+":"+str(current_time.minute)

    announcemnet = request.form.get('comment')
    print(tday, curtime,announcemnet)

    #INSERT ANNOUNCMENT TO DB
    qury.execute("INSERT INTO `reports/announcement`(`content`, `date`, `time`, `adminName`)"
                " VALUES ('"+announcemnet+"','"+str(tday)+"','"+str(curtime)+"','"+session["adminUser"]+"')")
    conn.commit()

    return render_template("dashboard admin/assignment.html",
                           logUser=session["adminUser"],
                           table_Assigment_Page_Admin = session["assigmentstdList"]
                           )





#to assign a studen to a faculty
techer =[]
@app.route("/Duty Assignment", methods=['POST'])
def DutyAssig_process():
    # messages = request.args['h'] mag pass value halin sa url_for
    qury.execute("SELECT `idnum`, `lname`, `fname`,`program_course`, `department`, `yrLvL` FROM `hk_users` WHERE `Status_avail` = 'av'")
    student_db_data = qury.fetchall()

    supervi = request.form['operations_Id_Selected']
    reqid = request.form['operationId']
    hkDESIGNATION = request.form['hkDESIGNATION']
    session["supervi"] = supervi
    session['reqid'] = reqid
    session['hkDESIGNATION'] = hkDESIGNATION
    techer.append(supervi)


    avil_std_list = []
    for k in student_db_data:
        avil_std_list.append(k)
    print("selected supervisur:", supervi)
    print("id of req", reqid)
    print(avil_std_list)

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

    return render_template("dashboard admin/assignment.html",
                           logUser=session["adminUser"],
                           table_Assigment_Page_Admin=session["assigmentstdList"]
                           ,table_avil_std=table_avil_std ,supervi=supervi
                           ,stduentNotAv=len(stduentNotAv),studentAv=len(studentAv)
                           ,coa = len(coa), coed = len(coed),cite = len(cite),
                            com = len(com),ccje = len(ccje),coe = len(coe),
                            cahs = len(cahs),come = len(come))

@app.route("/Assigment_modal_process", methods =['POST'])
def Assigment_modal_process():

    checkList = request.form.getlist("selected_std")
    print(len(checkList))
    tc_selected = techer[len(techer)-1]

    session["supervi"]
    session['reqid']
    print(session["supervi"],session['reqid'])
    qury.execute("SELECT `Request` FROM `operation_request` WHERE `ID` = '"+session['reqid']+"'")
    req_Process_for_assigning_duty = qury.fetchall()
    print(">>>",req_Process_for_assigning_duty[0][0])



    if int(req_Process_for_assigning_duty[0][0]) == len(checkList):
#       to assign a student to selected teacher
        for k in checkList:
            print(k)
            qury.execute(
                "INSERT INTO `hk_assignd_teaecher`(`operatikon_ID`, `hk_ID`) VALUES ('" + tc_selected + "','" + k + "')")
            conn.commit()
            #to update if the std is avilable
            qury.execute("UPDATE `hk_users` SET `Status_avail`='Na' WHERE `idnum` = '" + k + "' ")
            conn.commit()

            # to update the sipervisor of the student in the student rec
            qury.execute("UPDATE `hk_users` SET `dutySupervisor`='"+str(session["lname"])+" "+str(session["fname"])+"' WHERE `idnum` = '" + k + "'")
            conn.commit()

            #to update the DUTY DESIGNATION
            qury.execute("UPDATE `hk_users` SET `dutyDesignation`='"+session['hkDESIGNATION']+"'WHERE `idnum` = '" + k + "' ")
            conn.commit()

        #to remove the rows in the website
        qury.execute("SELECT * FROM `operation_request` WHERE `ID`='"+session['reqid']+"'")
#       to remove the requst from list
        dataTodel=list(qury.fetchall()[0])
        print(dataTodel)
        tableTodel = {"DESIGNATION":dataTodel[0],"REQ":dataTodel[1], "REPORT DAY/S":dataTodel[2],"SUPERVISOR":dataTodel[5],"DEPT":dataTodel[4],"REQST":dataTodel[3],"REQ ID":dataTodel[6]}
        print(tableTodel)
        session["assigmentstdList"].remove(tableTodel)
        qury.execute("DELETE FROM `operation_request` WHERE `ID`='"+session['reqid']+"'")
        conn.commit()




    elif len(checkList) < int(req_Process_for_assigning_duty[0][0]) :
        for k in checkList:
            print(k)
            qury.execute(
                "INSERT INTO `hk_assignd_teaecher`(`operatikon_ID`, `hk_ID`) VALUES ('" + tc_selected + "','" + k + "')")
            conn.commit()


            # to update the sipervisor of the student in the student rec
            qury.execute("UPDATE `hk_users` SET `Status_avail`='Na' WHERE `idnum` = '" + k + "' ")
            conn.commit()

            # to update the sipervisor of the student in the student rec
            qury.execute("UPDATE `hk_users` SET `dutySupervisor`='" + str(session["lname"]) + " " + str(
                session["fname"]) + "' WHERE `idnum` = '" + k + "'")
            conn.commit()

            # to update the DUTY DESIGNATION
            qury.execute("UPDATE `hk_users` SET `dutyDesignation`='" + session[
                'hkDESIGNATION'] + "'WHERE `idnum` = '" + k + "' ")
            conn.commit()


        req_need_std = int(req_Process_for_assigning_duty[0][0])-len(checkList)
        qury.execute("UPDATE `operation_request` SET `Request`='"+str(req_need_std)+"' WHERE `ID` ='"+session['reqid']+"' ")
        conn.commit()
    elif len(checkList) > int(req_Process_for_assigning_duty[0][0]):
        print("nagsubra mango")
    else:
        print("error")








    techer.clear()
    session.pop("supervi",None)
    session.pop("reqid", None)



    return redirect(url_for("DutyAssig"))
#-----------------------------------------------------------------------------------------------------------------------




@app.route("/User Management")
def UserManagement():
    try:
        return render_template("dashboard admin/UserManagement.html",logUser=session["adminUser"])
    except Exception:
        return redirect(url_for("admin"))


@app.route("/Export to Excel")
def Excel():
    try:
        return render_template("dashboard admin/Excel.html",logUser=session["adminUser"])
    except Exception:
        return redirect(url_for("admin"))
@app.route("/Setting and Configurations")
def Setting():
    try:

        return render_template("dashboard admin/Setting.html",logUser=session["adminUser"])
    except Exception:
        return redirect(url_for("admin"))
@app.route("/System Health Logs")
def Systemhealth():
    try:
        return render_template("dashboard admin/Systemhealth.html",logUser=session["adminUser"])
    except Exception:
        return redirect(url_for("admin"))
@app.route("/Feedback and Improvements")
def Feedback():
    try:
        return render_template("dashboard admin/Feedback.html",logUser=session["adminUser"])
    except Exception:
        return redirect(url_for("admin"))
@app.route("/assigment")
def assiment():
    try:

        return  render_template("dashboard admin/assignment.html",logUser=session["adminUser"])
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
    if request.form.get('select') == 'select':
        print('selected')
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


    return render_template("dashboard admin/ScholarRecordAdmin.html",idnum=idnum,Lname=Lname,Fname=Fname,totalDuty=totalDuty,
        course_Program=course_Program,department=department,yearLvl=yearLvl,scholarship=scholarship,
        DUTY_DESIGNATION=DUTY_DESIGNATION,DUTY_SUPERVISOR=DUTY_SUPERVISOR,reqiredDuty=reqiredDuty,
        remaningDuty=remaningDuty,statsuForRenewal=statsuForRenewal,Schoolyr=Schoolyr,semister=semister, remDutyMin = remDutyMin[0])



@app.route("/Duty_Records", methods=['POST'])
def Duty_Records():
    DUTY_Id_Num = request.form.get('Duty_Id')

    qury.execute("SELECT * FROM `scholar_duty_records` WHERE `Student_id_Number` = '"+DUTY_Id_Num+"'")
    rec_list_Db = qury.fetchall()

    rec_list = []
    for k in rec_list_Db:
        rec_list.append(k)
    record_table = []
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
            total_duty +=totalduty_mins
            duration = f"{durationoH:}h {durationm:02d}m"
            rec_process = {"DATE": rec_list[k][0], "CHECK-IN TIME": time_in, "CHECK-OUT TIME": time_out, "DURATION": duration}
            record_table.append(rec_process)

            qury.execute("UPDATE `hk_users` SET `id_totalHours`='"+str(total_duty)+"' WHERE `idnum` = '" + DUTY_Id_Num + "' ")
            conn.commit()




    return render_template("dashboard admin/dutyrecords.html", DUTY_Id_Num =DUTY_Id_Num, record_table= record_table)

#-------------------------END OF ADMIN SIDE BARS------------------




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

    try:
        if  time_In_Out == "IN":
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
                print(list_of_sign_in)
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

                    print("ngaa",totalduty_mins)
                    total_duty += totalduty_mins
                    print(total_duty)
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
            print("renderd today",renderedDutyToday)

            qury.execute("SELECT `remaningDuty`, `remDutyMins`FROM `hk_users` WHERE `idnum` = '" + stdId + "'")
            remdutyDb = qury.fetchall()
            remdutymins = (float(remdutyDb[0][1]))
            remduty = (float(remdutyDb[0][0])*60)+remdutymins

            print(remduty)


            remdutyMins = remduty - renderedDutyToday
            remdutyHoursConverstion = str(remdutyMins / 60).split(".")
            remdutyHours = remdutyHoursConverstion[0]
            remdutyMinscpnvertion = (float("0."+remdutyHoursConverstion[1])*60)

            print("remdutyMins",remdutyMins)
            print("remdutyHoursConverstion", remdutyHoursConverstion)
            print("remdutyHours", remdutyHours)
            print("remdutyMinscpnvertion", remdutyMinscpnvertion)
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