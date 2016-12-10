#################################
# Task 12 - definitions
# Desription: Given a string, we'll say that the front is the first 3 chars of the string. 
# If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
# Author : Igor Kurchatov 5/12/2016
#################################

def front3(str):
  return str[:3] * 3