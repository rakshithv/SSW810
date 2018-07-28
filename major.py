#-----------------------------------------------------------------------------
# This class is a datastructure that holds information about the majors
# offered by a university. It contains the dept name, required course
# and electives
#
# Written by Rakshith Varadaraju, July 27 2018 for Homework 10 in SSW-810
#-----------------------------------------------------------------------------

from collections import defaultdict

class Major:
    '''This class holds information about the department name,
    required course, and list of electives'''
    def __init__(self,dept):
        # This datastructure will store
        # Department Name
        # Courses - Required and Electives
        self.dept = dept
        self.courses = defaultdict(list)

    def get_summary(self):
        '''This function will return a summary of major data'''
        return [self.dept, sorted(self.courses.get("R")), sorted(self.courses.get("E"))]