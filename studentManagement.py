from tkinter import END
import mysql.connector
import tkinter as tk
from tkinter import ttk

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Kom+89&9@23",
    database="school"
)
cursor = mydb.cursor()


def addstudenttodb(idin, namein, agein, phonein, gradein, passwordin, genderin):
    studentid = idin.get(1.0, "end-1c")
    name = namein.get(1.0, "end-1c")
    age = int(agein.get(1.0, "end-1c"))
    phone = phonein.get(1.0, "end-1c")
    grade = int(gradein.get(1.0, "end-1c"))
    password = passwordin.get(1.0, "end-1c")
    if genderin.current() == 0:
        gender = "male"
    else:
        gender = "female"
    sql = "INSERT INTO student (studentid ,StudentName,Age,Phone,Grade,StudentPassword,Sex) VALUES (%s,%s, %s, %s, %s, %s, %s)"
    val = (studentid, name, age, phone, grade, password, gender)
    cursor.execute(sql, val)
    mydb.commit()


def addteachertodb(idin, namein, genderin, phonein, gradein, passwordin):
    teacherid = idin.get(1.0, "end-1c")
    name = namein.get(1.0, "end-1c")
    phone = phonein.get(1.0, "end-1c")
    grade = int(gradein.get(1.0, "end-1c"))
    password = passwordin.get(1.0, "end-1c")
    if genderin.current() == 0:
        gender = "male"
    else:
        gender = "female"
    sql = "INSERT INTO teacher (teacherID ,TeacherName,Sex,Phone,DegreeOfEducation,TeacherPassword) VALUES (%s,%s, %s, %s, %s, %s)"
    val = (teacherid, name, gender, phone, grade, password)
    cursor.execute(sql, val)
    mydb.commit()


def deletestudentfromdb(delinput, model):
    if model == 0:
        studentid = delinput.get(1.0, "end-1c")
        sql = "DELETE FROM student WHERE studentID = %s"
        adr = (studentid,)
        cursor.execute(sql, adr)
        mydb.commit()
    if model == 1:
        studentname = delinput.get(1.0, "end-1c")
        sql = "DELETE FROM student WHERE StudentName = %s"
        adr = (studentname,)
        cursor.execute(sql, adr)
        mydb.commit()


def deleteteacherfromdb(delinput, model):
    if model == 0:
        teacherid = delinput.get(1.0, END)
        print(teacherid)
        sql = "DELETE FROM teacher WHERE teacherID = %s"
        adr = (teacherid,)
        cursor.execute(sql, adr)
        mydb.commit()
    if model == 1:
        teachername = delinput.get(1.0, "end-1c")
        sql = "DELETE FROM teacher WHERE TeacherName = %s"
        adr = (teachername,)
        cursor.execute(sql, adr)
        mydb.commit()


def deletecoursefromdb(namein, teachin, roomin):
    name = namein.get(1.0, "end-1c")
    teacherid = teachin.get(1.0, "end-1c")
    roomid = roomin.get(1.0, "end-1c")
    sql = "DELETE FROM course WHERE CourseName=%s AND TeacherID=%s AND RoomID=%s"
    val = (name, teacherid, roomid)
    cursor.execute(sql, val)
    mydb.commit()
    Msg = tk.Message(text="deleted !")
    Msg.pack()


def deletestudent():
    deletestudentpannel = tk.Tk()
    label = tk.Label(text="delete by Student Id")
    idinputbox = tk.Text(height=2, width=20)
    label.pack()
    idinputbox.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            deletestudentfromdb(idinputbox, model=0), deletestudentpannel.destroy(), getstudents()]
    )
    button.pack()
    label = tk.Label(text="delete by Student name")
    nameinputbox = tk.Text(height=2, width=20)
    label.pack()
    nameinputbox.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            deletestudentfromdb(nameinputbox, model=1), deletestudentpannel.destroy(), getstudents()]
    )
    button.pack()
    button = tk.Button(
        text="back",
        command=lambda: [deletestudentpannel.destroy(), getstudents()]
    )
    button.pack()
    deletestudentpannel.mainloop()


def deleteteacher():
    deleteteacherpannel = tk.Tk()
    label = tk.Label(text="delete by Teacher Id")
    idinputbox = tk.Text(height=2, width=20)
    label.pack()
    idinputbox.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            deleteteacherfromdb(idinputbox, model=0), deleteteacherpannel.destroy(), getteachers()]
    )
    button.pack()
    label = tk.Label(text="delete by Teacher name")
    nameinputbox = tk.Text(height=2, width=20)
    label.pack()
    nameinputbox.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            deleteteacherfromdb(nameinputbox, model=1), deleteteacherpannel.destroy(), getteachers()]
    )
    button.pack()
    button = tk.Button(
        text="back",
        command=lambda: [deleteteacherpannel.destroy(), getteachers()]
    )
    button.pack()
    deleteteacherpannel.mainloop()


def deletecourse():
    deletecoursepannel = tk.Tk()
    label = tk.Label(
        text="course name"
    )
    cninput = tk.Text(
        height=2,
        width=20
    )
    cninput.pack()
    label.pack()
    label = tk.Label(
        text="teacher id"
    )
    tiinput = tk.Text(
        height=2,
        width=20
    )
    tiinput.pack()
    label.pack()
    label = tk.Label(
        text="room id"
    )
    riinput = tk.Text(
        height=2,
        width=20
    )
    riinput.pack()
    label.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [deletecoursefromdb(cninput, tiinput, riinput)]
    )
    button.pack()
    button = tk.Button(
        text="back",
        command=lambda: [deletecoursepannel.destroy(), getcourses()]
    )
    button.pack()
    deletecoursepannel.mainloop()


def addstudent():
    addstudentpanel = tk.Tk()
    label = tk.Label(text="Student Id")
    idinputbox = tk.Text(height=2, width=20)
    label.pack()
    idinputbox.pack()
    label = tk.Label(text="Name")
    nameinputbox = tk.Text(height=2, width=20)
    label.pack()
    nameinputbox.pack()
    label = tk.Label(text="Age")
    ageinputbox = tk.Text(height=2, width=20)
    label.pack()
    ageinputbox.pack()
    label = tk.Label(text="Phone")
    phonenumberinputbox = tk.Text(height=2, width=20)
    label.pack()
    phonenumberinputbox.pack()
    label = tk.Label(text="Grade")
    GradeinputBox = tk.Text(height=2, width=20)
    label.pack()
    GradeinputBox.pack()
    label = tk.Label(text="Password")
    PasswordinputBox = tk.Text(height=2, width=20)
    label.pack()
    PasswordinputBox.pack()
    label = tk.Label(text="Sex")
    gendercomboBox = ttk.Combobox(height=2, width=20)
    label.pack()
    gendercomboBox.pack()
    gendercomboBox['values'] = ('Male', 'Female')
    button = tk.Button(
        text="submit",
        command=lambda: [
            addstudenttodb(idinputbox, nameinputbox, ageinputbox, phonenumberinputbox, GradeinputBox, PasswordinputBox,
                           gendercomboBox), addstudentpanel.destroy(), getstudents()]
    )
    button.pack()
    button = tk.Button(
        text="back",
        command=lambda: [addstudentpanel.destroy(), getstudents()]
    )
    button.pack()
    addstudentpanel.mainloop()


def addteacher():
    addteacherpanel = tk.Tk()
    label = tk.Label(text="teacher Id")
    idinputbox = tk.Text(height=2, width=20)
    label.pack()
    idinputbox.pack()
    label = tk.Label(text="Name")
    nameinputbox = tk.Text(height=2, width=20)
    label.pack()
    nameinputbox.pack()
    label = tk.Label(text="Sex")
    gendercomboBox = ttk.Combobox(height=2, width=20)
    label.pack()
    gendercomboBox.pack()
    gendercomboBox['values'] = ('Male', 'Female')
    label = tk.Label(text="Phone")
    phonenumberinputbox = tk.Text(height=2, width=20)
    label.pack()
    phonenumberinputbox.pack()
    label = tk.Label(text="Degree Of Education")
    GradeinputBox = tk.Text(height=2, width=20)
    label.pack()
    GradeinputBox.pack()
    label = tk.Label(text="Password")
    PasswordinputBox = tk.Text(height=2, width=20)
    label.pack()
    PasswordinputBox.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            addteachertodb(idinputbox, nameinputbox, gendercomboBox, phonenumberinputbox, GradeinputBox
                           , PasswordinputBox), addteacherpanel.destroy(), getteachers()]
    )
    button.pack()
    button = tk.Button(
        text="back",
        command=lambda: [addteacherpanel.destroy(), getteachers()]
    )
    button.pack()
    addteacherpanel.mainloop()


def addcoursetodb(unitin, roomin, cnamein, holdingtimein, scorein, resourcein, studentin, teacherin):
    units = unitin.get(1.0, "end-1c")
    roomid = roomin.get(1.0, "end-1c")
    coursename = cnamein.get(1.0, "end-1c")
    holdingtime = holdingtimein.get(1.0, "end-1c")
    score = scorein.get(1.0, "end-1c")
    resource = resourcein.get(1.0, "end-1c")
    studentid = studentin.get(1.0)
    teacherid = teacherin.get(1.0)
    sql = "INSERT INTO course (Units, RoomID, CourseName, HoldingTime, ScoreIndex, Resources, StudentID, TeacherID) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"
    val = (units, roomid, coursename, holdingtime, score, resource, studentid, teacherid)
    cursor.execute(sql, val)
    mydb.commit()


def addcourse():
    addcoursepanel = tk.Tk()
    label = tk.Label(text="units")
    unitinputbox = tk.Text(height=2, width=20)
    label.pack()
    unitinputbox.pack()
    label = tk.Label(text="room id")
    roomidinputbox = tk.Text(height=2, width=20)
    label.pack()
    roomidinputbox.pack()
    label = tk.Label(text="Course Name")
    coursenameinputbox = tk.Text(height=2, width=20)
    label.pack()
    coursenameinputbox.pack()
    label = tk.Label(text="holding time")
    holdingtimeinputbox = tk.Text(height=2, width=20)
    label.pack()
    holdingtimeinputbox.pack()
    label = tk.Label(text="Score Index")
    ScoreindexinputBox = tk.Text(height=2, width=20)
    label.pack()
    ScoreindexinputBox.pack()
    label = tk.Label(text="Resource")
    ResourceinputBox = tk.Text(height=2, width=20)
    label.pack()
    ResourceinputBox.pack()
    label = tk.Label(text="student id")
    studentidinputBox = tk.Text(height=2, width=20)
    label.pack()
    studentidinputBox.pack()
    label = tk.Label(text="teacher id")
    teacheridinputBox = tk.Text(height=2, width=20)
    label.pack()
    teacheridinputBox.pack()

    button = tk.Button(
        text="submit",
        command=lambda: [
            addcoursetodb(unitinputbox, roomidinputbox, coursenameinputbox, holdingtimeinputbox, ScoreindexinputBox,
                          ResourceinputBox, studentidinputBox, teacheridinputBox), addcoursepanel.destroy(),
            getcourses()]
    )
    button.pack()
    button = tk.Button(
        text="back",
        command=lambda: [addcoursepanel.destroy(), getcourses()]
    )
    button.pack()
    addcoursepanel.mainloop()


def usercourses(uid, mod):
    if mod == 0:
        sql = "SELECT * FROM course INNER JOIN student ON course.StudentID = student.studentID AND student.studentID = %s"
    if mod == 1:
        sql = "SELECT * FROM course INNER JOIN teacher ON course.TeacherID = teacher.teacherID AND teacher.teacherID = %s"
    var = (uid,)
    cursor.execute(sql, var)
    courses = cursor.fetchall()
    courses = courses[0:][0:8]
    allcourse = tk.Tk()
    allcourse.geometry("900x900")
    e = tk.Label(width=15, text='units', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(width=15, text='roomId', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(width=15, text='CourseName', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(width=15, text='HoldingTime', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(width=15, text='ScoreIndex', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(width=15, text='Resource', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = tk.Label(width=15, text='StudentId', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    e = tk.Label(width=15, text='Teacherid', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=7)
    i = 1
    for x in courses:
        j = 0
        for y in x:
            e = tk.Label(text=y, width=15, fg="blue", borderwidth=2, relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            j += 1
            if j == 8:
                break
        i += 1
    if mod == 0:
        button5 = tk.Button(
            text="back",
            width=5,
            command=lambda: [allcourse.destroy(), studentpannel(uid)]
        )
        button5.grid(row=i, column=0)
    if mod == 1:
        button5 = tk.Button(
            text="back",
            width=5,
            command=lambda: [allcourse.destroy(), teacherpannel(uid)]
        )
        button5.grid(row=i, column=0)
    allcourse.mainloop()


def updatedb(uid, mod, kind, namein, phonein, passin):
    name = namein.get(1.0, "end-1c")
    phone = phonein.get(1.0, "end-1c")
    password = passin.get(1.0, "end-1c")
    if mod == 0:
        if kind == 0:
            sql = "UPDATE student SET StudentName = %s WHERE studentID = %s"
            var = (name, uid)
        if kind == 1:
            sql = "UPDATE student SET Phone = %s WHERE studentID = %s"
            var = (phone, uid)
        if kind == 2:
            sql = "UPDATE student SET StudentPassword = %s WHERE studentID = %s"
            var = (password, uid)
    if mod == 1:
        if kind == 0:
            sql = "UPDATE teacher SET TeacherName = %s WHERE teacherID = %s"
            var = (name, uid)
        if kind == 1:
            sql = "UPDATE teacher SET Phone = %s WHERE teacherID = %s"
            var = (phone, uid)
        if kind == 2:
            sql = "UPDATE teacher SET TeacherPassword = %s WHERE teacherID = %s"
            var = (password, uid)
    cursor.execute(sql, var)
    mydb.commit()
    Msg = tk.Message(text="updated !!")
    Msg.pack()


def updateuserpannel(mod, uid):
    upstudentpannel = tk.Tk()
    label1 = tk.Label(text="update name")
    nameinput = tk.Text(
        width=20,
        height=2
    )

    label2 = tk.Label(text="update phone number")
    phoneinput = tk.Text(
        width=20,
        height=2
    )

    label3 = tk.Label(text="update password")
    passinput = tk.Text(
        width=20,
        height=2
    )
    button1 = tk.Button(
        text="submit",
        command=lambda: [updatedb(uid, mod, 0, nameinput, phoneinput, passinput)]
    )
    button2 = tk.Button(
        text="submit",
        command=lambda: [updatedb(uid, mod, 1, nameinput, phoneinput, passinput)]
    )
    button3 = tk.Button(
        text="submit",
        command=lambda: [updatedb(uid, mod, 2, nameinput, phoneinput, passinput)]
    )
    label1.pack()
    nameinput.pack()
    button1.pack()
    label2.pack()
    phoneinput.pack()
    button2.pack()
    label3.pack()
    passinput.pack()
    button3.pack()
    if mod == 0:
        print(uid)
        button = tk.Button(
            text="back",
            command=lambda: [upstudentpannel.destroy(), studentpannel(uid)]
        )
        button.pack()
    if mod == 1:
        button = tk.Button(
            text="back",
            command=lambda: [upstudentpannel.destroy(), teacherpannel(uid)]
        )
        button.pack()
    upstudentpannel.mainloop()


def studentpannel(userid):
    studentmainpannel = tk.Tk()
    button = tk.Button(
        text="courses",
        command=lambda: [studentmainpannel.destroy(), usercourses(userid, 0)]
    )
    button.pack()
    button = tk.Button(
        text="update information",
        command=lambda: [studentmainpannel.destroy(), updateuserpannel(0, userid)]

    )
    button.pack()
    button = tk.Button(
        text="log out",
        command=lambda: [studentmainpannel.destroy(), mainwindow()]
    )
    button.pack()
    studentmainpannel.mainloop()


def teacherpannel(userid):
    teachermainpannel = tk.Tk()
    button = tk.Button(
        text="courses",
        command=lambda: [teachermainpannel.destroy(), usercourses(userid, 1)]
    )
    button.pack()
    button = tk.Button(
        text="update information",
        command=lambda: [teachermainpannel.destroy(), updateuserpannel(1, userid)]
    )
    button.pack()
    button = tk.Button(
        text="log out",
        command=lambda: [teachermainpannel.destroy(), mainwindow()]
    )
    button.pack()
    teachermainpannel.mainloop()


def injectuser(mod, idinput, passwordinput, pannel):
    userid = idinput.get(1.0, "end-1c")
    userpassword = passwordinput.get(1.0, "end-1c")
    if mod == 0:
        sql = ("SELECT * FROM student WHERE studentID=%s AND StudentPassword=%s")
        var = (userid, userpassword,)
        cursor.execute(sql, var)
        student = cursor.fetchall()
        if len(student) == 0:
            Msg = tk.Message(text="username or password is incorrect")
            Msg.pack()
        else:
            pannel.destroy()
            studentpannel(student[0][0])
    if mod == 1:
        sql = ("SELECT * FROM teacher WHERE teacherID=%s AND TeacherPassword=%s")
        var = (userid, userpassword,)
        cursor.execute(sql, var)
        teacher = cursor.fetchall()
        print(teacher)
        if len(teacher) == 0:
            print("varede if shodim")
            Msg = tk.Message(text="username or password is incorrect")
            Msg.pack()
        else:
            pannel.destroy()
            teacherpannel(teacher[0][0])


def studentlogin():
    studentloginpannel = tk.Tk()
    label = tk.Label(text="student id")
    studentidinput = tk.Text(
        width=20,
        height=2,
    )
    label.pack()
    studentidinput.pack()
    label = tk.Label(text="student password")
    studentpasswordinput = tk.Text(
        width=20,
        height=2
    )
    label.pack()
    studentpasswordinput.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            injectuser(mod=0, idinput=studentidinput, passwordinput=studentpasswordinput, pannel=studentloginpannel)
        ]
    )
    button1 = tk.Button(
        text="back",
        command=lambda: [studentloginpannel.destroy(), getstudents()]
    )
    button.pack()
    button1.pack()

    studentloginpannel.mainloop()


def teacherlogin():
    teacherloginpannel = tk.Tk()
    label = tk.Label(text="teacher id")
    teacheridinput = tk.Text(
        width=20,
        height=2,
    )
    label.pack()
    teacheridinput.pack()
    label = tk.Label(text="teacher password")
    teacherpasswordinput = tk.Text(
        width=20,
        height=2
    )
    label.pack()
    teacherpasswordinput.pack()
    button = tk.Button(
        text="submit",
        command=lambda: [
            injectuser(mod=1, idinput=teacheridinput, passwordinput=teacherpasswordinput, pannel=teacherloginpannel)]
    )
    button1 = tk.Button(
        text="back",
        command=lambda: [teacherloginpannel.destroy(), getstudents()]
    )
    button.pack()
    button1.pack()

    teacherloginpannel.mainloop()


def topstudent():
    sql = "SELECT * FROM student WHERE Grade > (SELECT AVG(Grade) FROM student)"
    cursor.execute(sql)
    students = cursor.fetchall()
    alltopstudent = tk.Tk()
    alltopstudent.geometry("900x900")
    e = tk.Label(width=15, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(width=15, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(width=15, text='Age', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(width=15, text='phonenumber', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(width=15, text='Grade', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(width=15, text='Password', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = tk.Label(width=15, text='Gender', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    i = 1
    for x in students:
        j = 0
        for y in x:
            e = tk.Label(text=y, width=15, fg="blue", borderwidth=2, relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            j += 1
        i += 1
    button6 = tk.Button(
        text="back",
        width=15,
        command=lambda: [alltopstudent.destroy(), mainwindow()]
    )
    button6.grid(row=i, column=0)
    alltopstudent.mainloop()


def getstudents():
    cursor.execute("SELECT * FROM student ORDER BY Grade DESC")
    students = cursor.fetchall()
    allstudent = tk.Tk()
    allstudent.geometry("900x900")
    e = tk.Label(width=15, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(width=15, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(width=15, text='Age', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(width=15, text='phonenumber', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(width=15, text='Grade', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(width=15, text='Password', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = tk.Label(width=15, text='Gender', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    i = 1
    for x in students:
        j = 0
        for y in x:
            e = tk.Label(text=y, width=15, fg="blue", borderwidth=2, relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            j += 1
        i += 1
    button6 = tk.Button(
        text="back",
        width=15,
        command=lambda: [allstudent.destroy(), mainwindow()]
    )
    button7 = tk.Button(
        text="top student",
        width=15,
        command=lambda: [allstudent.destroy(), topstudent()]
    )
    button10 = tk.Button(
        text="delete student",
        width=15,
        command=lambda: [allstudent.destroy(), deletestudent()]
    )
    button12 = tk.Button(
        text="add student",
        width=15,
        command=lambda: [allstudent.destroy(), addstudent()]
    )
    button6.grid(row=i, column=0)
    button7.grid(row=i, column=1)
    button10.grid(row=i, column=2)
    button12.grid(row=i, column=3)
    allstudent.mainloop()


def getteachers():
    cursor.execute("SELECT * FROM teacher")
    teachers = cursor.fetchall()
    allteacher = tk.Tk()
    allteacher.geometry("900x900")
    e = tk.Label(width=15, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(width=15, text='teacherName', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(width=15, text='sex', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(width=15, text='phone', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(width=15, text='DegreeOfEducation', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(width=15, text='TeacherPassword', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    i = 1
    for x in teachers:
        j = 0
        for y in x:
            e = tk.Label(text=y, width=15, fg="blue", borderwidth=2, relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            j += 1
        i += 1
    button5 = tk.Button(
        text="back",
        width=15,
        command=lambda: [allteacher.destroy(), mainwindow()]
    )
    button6 = tk.Button(
        text="add teacher",
        width=15,
        command=lambda: [allteacher.destroy(), addteacher()]
    )
    button9 = tk.Button(
        text="delete teacher",
        width=15,
        command=lambda: [allteacher.destroy(), deleteteacher()]

    )
    button5.grid(row=i, column=0)
    button6.grid(row=i, column=1)
    button9.grid(row=i, column=2)
    allteacher.mainloop()


def getcourses():
    cursor.execute("SELECT * FROM course ORDER BY ScoreIndex")
    courses = cursor.fetchall()
    allcourse = tk.Tk()
    allcourse.geometry("900x900")
    e = tk.Label(width=15, text='units', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(width=15, text='roomId', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(width=15, text='CourseName', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(width=15, text='HoldingTime', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(width=15, text='ScoreIndex', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(width=15, text='Resource', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = tk.Label(width=15, text='StudentId', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    e = tk.Label(width=15, text='Teacherid', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
    e.grid(row=0, column=7)
    i = 1
    for x in courses:
        j = 0
        for y in x:
            e = tk.Label(text=y, width=15, fg="blue", borderwidth=2, relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            j += 1
        i += 1
    button5 = tk.Button(
        text="back",
        width=5,
        command=lambda: [allcourse.destroy(), mainwindow()]
    )
    button6 = tk.Button(
        text="add course",
        width=15,
        command=lambda: [allcourse.destroy(), addcourse()]
    )
    button9 = tk.Button(
        text="delete course",
        width=15,
        command=lambda: [allcourse.destroy(), deletecourse()]
    )
    button5.grid(row=i, column=0)
    button6.grid(row=i, column=1)
    button9.grid(row=i, column=2)
    allcourse.mainloop()


def mainwindow():
    window = tk.Tk()
    window.geometry("500x500")
    button1 = tk.Button(
        text="teacher login",
        width=20,
        height=5,
        command=lambda: [window.destroy(), teacherlogin()]
    )
    button2 = tk.Button(
        text="student login",
        width=20,
        height=5,
        command=lambda: [window.destroy(), studentlogin()]
    )
    button3 = tk.Button(
        text="all students",
        width=20,
        height=5,
        command=lambda: [window.destroy(), getstudents()]
    )
    button4 = tk.Button(
        text="all teachers",
        width=20,
        height=5,
        command=lambda: [window.destroy(), getteachers()]
    )
    button5 = tk.Button(
        text="all courses",
        width=20,
        height=5,
        command=lambda: [window.destroy(), getcourses()]
    )
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()

    window.mainloop()


if __name__ == "__main__":
    mainwindow()
