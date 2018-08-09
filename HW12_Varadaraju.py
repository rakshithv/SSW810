#-----------------------------------------------------------------------------
# This is a program that will read a database that has information about a 
# university. It will then send a query to generate a table of instructor
# data with ID, Name, Dept, Course and # of students in Course. The table
# will be displayed in a web browser at address 127.0.0.1:5000/instructor_courses
#
# Written by Rakshith Varadaraju, August 8 2018 for Homework 12 in SSW-810
#-----------------------------------------------------------------------------

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
DB_FILE = "/Users/rakra/Desktop/Stevens_Summer/SSW810/810_startup.db"

@app.route('/instructor_courses')
def instructor_courses():

    db = sqlite3.connect(DB_FILE)

    # This query selects CWID, Name, Dept from the instructor table
    # and Courses, and count of students in courses from the grades table.
    # It then groups the data by Courses and orders by CWID
    db_query = """select i.CWID, i.Name, i.Dept, g.Course, count(g.course) as Students
                   from HW11_instructors i
                   join HW11_grades g on i.CWID=g.Instructor_CWID
                   group by g.Course
                   order by i.CWID"""
    
    rows = db.execute(db_query)

    data = [{'cwid' : cwid, 'name' : name, 'department' : department, 'courses' : courses, 'students' : students}
             for cwid, name, department, courses, students in rows]

    db.close()

    return render_template('instructor_courses.html',
                            title="Stevens Repository",
                            table_title="Number of students by course and instructor",
                            instructors=data)

app.run(debug=True)