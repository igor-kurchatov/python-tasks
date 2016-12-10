#################################
# Task 6 - definitions
# Desription: Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
# Author : Igor Kurchatov 5/12/2016
#################################

def makes10(a, b):
  return (a == 10 or b == 10 or a + b == 10)

def makes10_run():
  
  print("Task 6 - Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.")
    
  inp_first_num = 0
  inp_second_num = 0

  try:
    inp_first_num = int(input("Please, enter the first number: "))
    inp_second_num = int(input("Please, enter the second number: "))
  except ValueError as e:
      print("Please enter valid integer value.\n" + str(e))
      makes10_run()
      return

  print(str.format("The result is {0}", makes10(inp_first_num, inp_second_num)))