#-----------------------------------------------------------------------------
# This is a class that will store student data
#
# Written by Rakshith Varadaraju, July 23 2018 for Homework 9 in SSW-810
#-----------------------------------------------------------------------------

from collections import defaultdict

class Student:
    '''This class is a datastructure that stores student information
    such as Student ID, Name, Major, Completed courses with grade'''
    def __init__(self,id,name,major):
        # This datastructure will store
        # Student ID
        # Student Name
        # Student Major
        # Student Completed Courses with grade information
        self.id = id
        self.name = name
        self.major = major
        self.courses = defaultdict(str)

    def get_summary(self):
        if self.courses:
            return [self.id, self.name, sorted(list(self.courses.keys()))]
        else:
            return [self.id, self.name, []]