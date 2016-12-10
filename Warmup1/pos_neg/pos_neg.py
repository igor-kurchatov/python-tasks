#################################
# Task 8 - definitions
# Desription: Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.
# Author : Igor Kurchatov 5/12/2016
#################################

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

def pos_neg_run():

  print("Task 8 - Given 2 int values, return True if one is negative and one is positive." 
        'Except if the parameter "negative" is True, then return True only if both are negative.')
    
  inp_first_num = 0
  inp_second_num = 0
  inp_neg = ""

  try:
    inp_first_num = int(input("Please, enter the first number: "))
    inp_second_num = int(input("Please, enter the second number: "))
    inp_neg = input("Please, enter the negative parameter [Y / N]. N is default value: ")

  except ValueError as e:
      print("Please enter valid integer value.\n" + str(e))
      pos_neg_run()
      return

  arg_neg = False  

  if str.upper(inp_neg) == "Y":
    arg_neg = True

  print(str.format("The result is {0}", pos_neg(inp_first_num, inp_second_num, arg_neg)))