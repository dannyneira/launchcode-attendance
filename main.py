from app import app, db
from flask import request, redirect, render_template, session, flash 
from models import Student, Teacher, Attendance

# @app.before_request
# def require_login():
#     blocked_routes = ['index', 'student_login', 'edit_student', 'attendance', 'add_student', 'students']
#     allowed_routes = ['teacher_login', 'teacher_signup']
#     if request.endpoint not in allowed_routes and 'username' not in session:
#         return redirect('/teacher_login')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teacher_login", methods=['GET', 'POST'])
def teacher_login():
    session['email'] = "blah@gmail.com"
    return render_template("teacher_login.html", title="Login", login="active")

@app.route("/student_login", methods=['GET', 'POST'])
def student_login():
    if request.method == "POST":
        pass
    else:
        stu1 = Student( "John", "Doe")
        stu2 = Student("Mike", "Smith")
        stu3 = Student("Jane", "Doe")
        stu4 = Student("Maggie", "Smith")
        students = [ stu1, stu2, stu3, stu4 ]
        session['email'] = "blah@gmail.com"
        return render_template("student_login.html", title="Student Login", students=students)

@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        date_now = request.form['date_now']
        attendance = Attendance.query.filter_by(date_now=date_now).all()
        return render_template("attendance.html", attendance=attendance)
    else:
        dates = Attendance.query.filter_by().all()
        return render_template("attendance.html", dates=dates)



if __name__ == "__main__":
    app.run()