#################################
# Task 4 - testing
# Desription: Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from diff21 import diff21

testjson = TestCaseJson.TestCaseJson()
testjson.Start("diff21", r"Warmup1\diff21\diff21_test_case.txt", diff21)
