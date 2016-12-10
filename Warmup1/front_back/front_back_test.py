#################################
# Task 11 - testing
# Desription: Given a string, return a new string where the first and last chars have been exchanged.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from front_back import front_back

testjson = TestCaseJson.TestCaseJson()
testjson.Start("front_back", r"Warmup1\front_back\front_back_test_case.txt", front_back)