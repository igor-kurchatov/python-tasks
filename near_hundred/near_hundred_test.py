#################################
# Task 7 - testing
# Desription: Given an int n, return True if it is within 10 of 100, 200, 300, -100, -200, etc. Note: abs(num) 
# computes the absolute value of a number.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from near_hundred import near_hundred

testjson = TestCaseJson.TestCaseJson()
testjson.Start("near_hundred", r"near_hundred\near_hundred_test_case.txt", near_hundred)