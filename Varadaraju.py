#-----------------------------------------------------------------------------
# This is a program that will compile student and instructor data for a 
# university. This program will take as an input a folder that contains
# data for students, instructors and grades
#
# Written by Rakshith Varadaraju, July 27 2018 for Homework 10 in SSW-810
#-----------------------------------------------------------------------------
import os
import unittest
from repository import Repository

def create_repo(path):
    '''This function will take as an input a directory that contains
    information for a university. If the directory exists, it will
    then read the contents and compile them into several 
    datastructures'''
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Invalid directory mentioned")
    else:
        return Repository(os.path.basename(path))

def main():
    sit = create_repo("/Users/rakra/Desktop/Stevens_Summer/SSW810/SIT")
    sit.print_major_summary()
    sit.print_student_summary()
    sit.print_instructor_summary()

class RepositoryTest(unittest.TestCase):
    def test_simple_files(self):
        sit = create_repo("/Users/rakra/Desktop/Stevens_Summer/SSW810/Simple")
        actual_list = []
        for item in sit.student_list.values():
            actual_list.append(item.get_summary())
        expected_list = [['10103', 'Baldwin, C', ['SSW 567'],['SSW 540','SSW 555','SSW 564'],
        ['CS 501','CS 513','CS 545']]]
        self.assertEqual(actual_list,expected_list)

        actual_list = []
        for item in sit.instructor_list.values():
            for summary in item.get_summary():
                actual_list.append(summary)
        expected_list = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 1]]
        self.assertEqual(actual_list, expected_list)

        actual_list = []
        for item in sit.major_list.values():
            actual_list.append(item.get_summary())
        expected_list = [['SFEN',['SSW 540','SSW 555', 'SSW 564', 'SSW 567'],['CS 501','CS 513','CS 545']]]
        self.assertEqual(actual_list,expected_list)

main()
unittest.main(exit=False, verbosity=2)