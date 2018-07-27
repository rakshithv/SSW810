#-----------------------------------------------------------------------------
# This is a class that will store instructor data
#
# Written by Rakshith Varadaraju, July 23 2018 for Homework 9 in SSW-810
#-----------------------------------------------------------------------------

from collections import defaultdict

class Instructor:
    '''This class is a datastructure that stores instructor information
    such as Instructor ID, Name, Department, Courses taught with number
    of students in each course'''
    def __init__(self,id,name,dept):
        # This datastructure will store
        # Instructor ID
        # Instructor Name
        # Instructor Department
        # Instructor courses taught with number of students
        self.id = id
        self.name = name
        self.dept = dept
        self.courses = defaultdict(int)

    def get_summary(self):
        for keys, values in sorted(self.courses.items()):
            yield[self.id, self.name, self.dept, keys, values]