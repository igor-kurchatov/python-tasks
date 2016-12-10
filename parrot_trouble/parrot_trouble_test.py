#################################
# Task 5 - testing
# Desription: We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
from parrot_trouble import parrot_trouble

testjson = TestCaseJson.TestCaseJson()
testjson.Start("parrot_trouble", r"parrot_trouble\parrot_trouble_test_case.txt", parrot_trouble)