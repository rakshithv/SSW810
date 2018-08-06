#-----------------------------------------------------------------------------
# This is a program that will read a database that has information about a 
# university. It will then send a query to generate a table of instructor
# data with ID, Name, Dept, Course and # of students in Course. The table
# will be printed to the console using Pretty Table.
#
# Written by Rakshith Varadaraju, August 5 2018 for Homework 11 in SSW-810
#-----------------------------------------------------------------------------

from prettytable import PrettyTable
import sqlite3

def main():
    # Path for where the DB File exists
    DB_FILE = "/Users/rakra/Desktop/Stevens_Summer/SSW810/810_startup.db"
    db = sqlite3.connect(DB_FILE)
    pt = PrettyTable(field_names=["CWID","Name","Dept","Course","Students"])

    # This query selects CWID, Name, Dept from the instructor table
    # and Courses, and count of students in courses from the grades table.
    # It then groups the data by Courses and orders by CWID
    db_query = "select i.CWID, i.Name, i.Dept, g.Course, count(g.Course) as Students" + \
    " from HW11_instructors i" + \
    " join HW11_grades g on i.CWID=g.Instructor_CWID" + \
    " group by g.Course" + \
    " order by i.CWID"
    for row in db.execute(db_query):
        pt.add_row(row)
    print(pt)
    db.close()

main()