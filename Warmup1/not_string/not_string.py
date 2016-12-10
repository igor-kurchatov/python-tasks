#################################
# Task 9 - definitions
# Desription: Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
# Author : Igor Kurchatov 5/12/2016
#################################

def not_string(str):
  if str[0:3] == 'not':
    return str
  else:
    return 'not ' + str

def not_string_run():

  print('Task 9 - Given a string, return a new string where "not " has been added to the front.'
        'However, if the string already begins with "not", return the string unchanged.')
    
  inp_str = input("Please, enter the string: ")
  
  print(str.format("The result is {0}", not_string(inp_str)))