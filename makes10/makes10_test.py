#################################
# Task 6 - testing
# Desription: Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from makes10 import makes10

testjson = TestCaseJson.TestCaseJson()
testjson.Start("makes10", r"makes10\makes10_test_case.txt", makes10)