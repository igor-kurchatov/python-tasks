#################################
# Task 3 - testing
# Desription: Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from sum_double import sum_double

testjson = TestCaseJson.TestCaseJson()
testjson.Start("sum_double", r"sum_double\sum_double_test_case.txt", sum_double)



