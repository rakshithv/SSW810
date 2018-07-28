#-----------------------------------------------------------------------------
# This is a class that will store student data
#
# Written by Rakshith Varadaraju, July 27 2018 for Homework 10 in SSW-810
#-----------------------------------------------------------------------------

from collections import defaultdict

class Student:
    '''This class is a datastructure that stores student information
    such as Student ID, Name, Major, Completed courses with grade,
    remaining required courses, remaining electives'''
    def __init__(self,id,name,major,required,electives):
        # This datastructure will store
        # Student ID
        # Student Name
        # Student Major
        # Student Completed Courses with grade information
        self.id = id
        self.name = name
        self.major = major
        self.courses = defaultdict(str)
        self.required = sorted(required)
        self.electives = sorted(electives)

    def get_summary(self):
        '''This function will return a summary of student data'''
        valid_grades = ('A','A-','B+','B','B-','C+','C')
        # Is there a way to modify this list, without affecting
        # all the object instances. Only solution I found was
        # to create a copy of what I thought was a local list.
        remain_req = self.required[:]
        for key, value in self.courses.items():
            if value in valid_grades:
                if key in self.electives:
                    self.electives = "None"
                elif key in remain_req:
                    remain_req.remove(key)

        return [self.id, self.name, sorted(list(self.courses.keys())),
        remain_req, self.electives]