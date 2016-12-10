#################################
# Task 3 - definitions
# Desription: Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# Author : Igor Kurchatov 5/12/2016
#################################

def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  else:
    return a + b

def sum_double_run():
  
  print("Given two int values, it's returned with the sum. Unless the two values are the same, then the sum will be doubled.")
    
  inp_first_num = 0.0
  inp_second_num = 0.0

  try:
    inp_first_num = float(input("Please, enter the first number: "))
    inp_second_num = float(input("Please, enter the second number: "))
  except ValueError as e:
      print(str(e))
      sum_double_run()
      return

  print(str.format("The result is {0}", sum_double(inp_first_num, inp_second_num)))