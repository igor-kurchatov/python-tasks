#################################
# Task 8 - testing
# Desription: Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from pos_neg import pos_neg

testjson = TestCaseJson.TestCaseJson()
testjson.Start("pos_neg", r"pos_neg\pos_neg_test_case.txt", pos_neg)