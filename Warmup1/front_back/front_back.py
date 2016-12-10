#################################
# Task 11 - definitions
# Desription: Given a string, return a new string where the first and last chars have been exchanged.
# Author : Igor Kurchatov 5/12/2016
#################################

def front_back(str):
  if (len(str) > 1):
    return str[-1:] + str[1:-1] + str[0]
  else:
    return str