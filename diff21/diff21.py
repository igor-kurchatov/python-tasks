#################################
# Task 4 - definitions
# Desription: Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
# Author : Igor Kurchatov 5/12/2016
#################################

def diff21(n):
  if n > 21:
    return abs(21 - n) * 2
  else:
    return abs(21 - n)

def diff21_run():
      
  print("Task 4 - Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.")
    
  inp_num = 0

  try:
    inp_num = int(input("Please, enter the number n: "))
  except ValueError as e:
    print("Please enter valid integer value.\n" + str(e))
    diff21_run()
    return

  print(str.format("The result is {0}", diff21(inp_num)))
