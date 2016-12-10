#################################
# Task 12 - testing
# Desription: Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from front3 import front3

testjson = TestCaseJson.TestCaseJson()
testjson.Start("front3", r"Warmup1\front3\front3_test_case.txt", front3)