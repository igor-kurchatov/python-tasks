#################################
# Task 10 - testing
# Desription: Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from missing_char import missing_char

testjson = TestCaseJson.TestCaseJson()
testjson.Start("missing_char", r"Warmup1\missing_char\missing_char_test_case.txt", missing_char)