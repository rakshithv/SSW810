#-----------------------------------------------------------------------------
# This class is a datastructure that holds information about a university
# such as name of institution, list of students, and list of instructors
#
# Written by Rakshith Varadaraju, July 26 2018 for Homework 10 in SSW-810
#-----------------------------------------------------------------------------

from collections import defaultdict
from instructor import Instructor
from major import Major
from prettytable import PrettyTable
from text_file_importer import extract
from student import Student
import operator

class Repository:
    '''This class takes as an input the name of the university'''
    def __init__(self,name):
        # This datastructure will store
        # Name of the college
        self.name = name
        self.major_list = defaultdict(Major)
        self.student_list = defaultdict(Student)
        self.instructor_list = defaultdict(Instructor)
        self.update_major_data()
        self.update_student_data()
        self.update_instructor_data()
        self.process_grade_data()
    
    def update_major_data(self):
        '''This function reads in the major data and create
        individual major records'''
        # Is there a way to refactor this code so that 
        # the loop doesnt have to be done twice
        for dept, flag, course in extract('majors.txt', 3):
            self.major_list[dept] = Major(dept)
        for dept, flag, course in extract('majors.txt', 3):
            self.major_list[dept].courses[flag].append(course)        
        
    def update_student_data(self):
        '''This function reads in the student data and create
        individual student records'''
        for id, name, major in extract('students.txt',3):
            self.student_list[id] = Student(id,name,major)

    def update_instructor_data(self):
        '''This function reads in the instructor data and create
        individual instructor records'''
        for id,name,dept in extract('instructors.txt',3):
            self.instructor_list[id] = Instructor(id,name,dept)

    def process_grade_data(self):
        '''This function reads in the grades data and will update
        both student and instructor objects with course information'''
        for student_id, course_name, grade, instructor_id in extract('grades.txt', 4):
            self.student_list[student_id].courses[course_name] = grade
            self.instructor_list[instructor_id].courses[course_name] += 1

    def get_name(self):
        '''This function will return the name of the repository'''
        return self.name

    def print_major_summary(self):
        '''This function will print major data'''
        print('Major Summary')
        pt = PrettyTable(field_names=["Dept", "Required", "Electives"])
        for item in (self.major_list.values()):
            pt.add_row(item.get_summary())
        print(pt)

    def print_student_summary(self):
        '''This function will print student data'''
        print('Student Summary')
        pt = PrettyTable(field_names=["CWID","Name","Completed Courses"])
        for item in self.student_list.values():
            pt.add_row(item.get_summary())
        print(pt)

    def print_instructor_summary(self):
        '''This function will print instructor data'''
        print('Instructor Summary')
        pt = PrettyTable(field_names=["CWID","Name","Dept","Course","Students"])
        for item in self.instructor_list.values():
            for summary in item.get_summary():
                pt.add_row(summary)
        print(pt)