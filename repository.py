#-----------------------------------------------------------------------------
# This class is a datastructure that holds information about a university
# such as name of institution, list of students, and list of instructors
#
# Written by Rakshith Varadaraju, July 23 2018 for Homework 9 in SSW-810
#-----------------------------------------------------------------------------

from instructor import Instructor
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
        self.student_list = []
        self.instructor_list = []
        self.update_student_data()
        self.update_instructor_data()
        self.process_grade_data()
    
    def update_student_data(self):
        '''This function reads in the student data and create
        individual student records'''
        for id, name, major in extract('students.txt',3):
            self.student_list.append(Student(id,name,major))
        self.student_list.sort(key=operator.attrgetter('id'))

    def update_instructor_data(self):
        '''This function reads in the instructor data and create
        individual instructor records'''
        for id,name,dept in extract('instructors.txt',3):
            self.instructor_list.append(Instructor(id,name,dept))
        self.instructor_list.sort(key=operator.attrgetter('id'))

    def process_grade_data(self):
        '''This function reads in the grades data and will update
        both student and instructor objects with course information'''
        for student_id, course_name, grade, instructor_id in extract('grades.txt', 4):
            for item in self.student_list:
                if item.id == student_id:
                    item.courses[course_name] = grade
                    break
            for item in self.instructor_list:
                if item.id == instructor_id:
                    item.courses[course_name] += 1
                    break


    def get_name(self):
        '''This function will return the name of the repository'''
        return self.name

    def print_student_summary(self):
        '''This function will print student data'''
        print('Student Summary')
        pt = PrettyTable(field_names=["CWID","Name","Completed Courses"])
        for item in self.student_list:
            pt.add_row(item.get_summary())
        print(pt)

    def print_instructor_summary(self):
        '''This function will print instructor data'''
        print('Instructor Summary')
        pt = PrettyTable(field_names=["CWID","Name","Dept","Course","Students"])
        for item in self.instructor_list:
            for summary in item.get_summary():
                pt.add_row(summary)
        print(pt)