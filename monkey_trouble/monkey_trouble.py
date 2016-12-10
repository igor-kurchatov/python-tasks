#################################
# Task 2 - definitions
# Desription: We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. 
# Author : Igor Kurchatov 5/12/2016
#################################

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or not (a_smile or b_smile)

def monkey_trouble_run():
  
  print("Are the monkeys in trouble?")
    
  inp_first_smile = input("Is the first monkey smiling? Please, enter [Y / N]. N is default value]: ")
  inp_second_smile = input("Is the second monkey smiling? Please, enter [Y / N]. N is default value]: ")

  arg_first_smile = False
  arg_second_smile = False

  if str.upper(inp_first_smile) == "Y":
    arg_first_smile = True

  if str.upper(inp_second_smile) == "Y":
    arg_second_smile = True

  print(str.format("The result is {0}", monkey_trouble(arg_first_smile, arg_second_smile)))

