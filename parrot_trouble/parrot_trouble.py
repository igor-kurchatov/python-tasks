#################################
# Task 5 - definitions
# Desription: We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
# Author : Igor Kurchatov 5/12/2016
#################################

def parrot_trouble(talking, hour):
  return (talking and (  hour < 7 or hour > 20 ))

def parrot_trouble_run():

  print('Task 5 - We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.\n' 
        'We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.')
    
  inp_talking = ""
  inp_hour = 0

  try:
    inp_talking = input("Is the parrot is talking? Please, enter [Y / N]. N is default value: ")
    inp_hour = abs(int(input("Please, enter the hour in the range 0..23: ")))
  except ValueError as e:
    print("Please enter valid integer value.\n" + str(e))
    parrot_trouble_run()
    return

  arg_talking = False  

  if str.upper(inp_talking) == "Y":
    arg_talking = True
    
  if inp_hour < 0:
    inp_hour = 0
  elif inp_hour > 23:
    inp_hour = 23    

  print(str.format("The result is {0}", parrot_trouble(arg_talking, inp_hour)))