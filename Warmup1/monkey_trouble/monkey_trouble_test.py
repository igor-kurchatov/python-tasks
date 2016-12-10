#################################
# Task 2 - testing
# Desription: We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. 
# Author : Igor Kurchatov 5/12/2016
#################################

import TestCaseJson
import monkey_trouble

testjson = TestCaseJson.TestCaseJson()
testjson.Start("monkey_trouble", r"Warmup1\monkey_trouble\monkey_trouble_test_case.txt", monkey_trouble.monkey_trouble)