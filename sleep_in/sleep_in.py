#################################
# Task 1
# Desription: We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# Author : Igor Kurchatov 5/12/2016
#################################

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def sleep_in_run():
  print("Can you sleep in?")
    
  inp_weekday = input("Is it a weekday? Please, enter [Y / N]. N is default value]: ")
  inp_vacation = input("Is it a vacation? Please, enter [Y / N]. N is default value]: ")

  arg_weekday = False
  arg_vacation = False

  if str.upper(inp_weekday) == "Y":
    arg_weekday = True

  if str.upper(inp_vacation) == "Y":
    arg_vacation = True

  print(str.format("The result is {0}", sleep_in(arg_weekday, arg_vacation)))