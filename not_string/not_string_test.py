#################################
# Task 9 - testing
# Desription: Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from not_string import not_string

testjson = TestCaseJson.TestCaseJson()
testjson.Start("not_string", r"not_string\not_string_test_case.txt", not_string)