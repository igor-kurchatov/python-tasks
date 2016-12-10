#################################
# Task 7 - definitions
# Desription: Given an int n, return True if it is within 10 of 100, 200, 300, -100, -200, etc. Note: abs(num) 
# computes the absolute value of a number.
# Author : Igor Kurchatov 5/12/2016
#################################

def near_hundred(n):
    
  hund_n = round(abs(n) / 100) * 100
  
  if hund_n == 0:
    hund_n = 100
    
  return abs(abs(n) - hund_n) <= 10

def near_hundred_run():
    
  print("Task 7 - Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.")
    
  inp_first_num = 0

  try:
    inp_first_num = int(input("Please, enter the number n: "))
  except ValueError as e:
      print("Please enter valid integer value.\n" + str(e))
      near_hundred_run()
      return

  print(str.format("The result is {0}", near_hundred(inp_first_num)))