while True:
  try:
    #Gets the input string from user
    string = input("String To Convert To List : ")
    #Evals it to convert it to a list
    lst = eval(string)
    #Iterates through list and prints results
    for _ in lst:
       print(_)
  except Exception as e:
    print(e)
    #Prints the caught error
    print("Failed to convert string to list...")
  print("\n")

# The python 'eval' statement executes a variable. It is sometimes used to convert a string to a list.
#
# In this example, someone could enter a Python array and it would iterate through the array which you provided. However, they could also enter 'print("abc")' into the input and your query will be executed, which means that they could execute code through 'eval'. The limits to eval RCE is that 'eval' can't execute very complicated queries without throwing errors, unlike 'exec'.
#
#
# Better RCE with eval can be achieved through using an 'exec' statement in the initial RCE. For example : 
#
# eval('''exec("import subprocess; print(subprocess.check_output('cat /etc/passwd', shell=True))")''')
#
# - As opposed to :
# eval("import subprocess; print(subprocess.check_output('cat /etc/passwd')")
#
# Which would throw an error.
#
#
# A better option to convert a string to list would be to use 'ast.literal_eval(string)'. This will throw an error if the statement is not a valid data type, but the unwanted code will not be executed.

