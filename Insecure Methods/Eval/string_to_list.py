while True:
  try:
    #Gets the input string from user
    string = input("String To Convert To List : ")
    #Evals it to convert it to a list
    lst = eval(string)
    #Iterates through list and prints results
    for _ in lst:
       print(_)
  except:
    print("Failed to convert string to list...")
  print("\n")

# The python 'eval' statement executes a variable. It can be used to convert a string to a list.
#
# However, you could also enter 'print("abc")' as the list and your query will be executed, which means that you could execute code through 'eval'. The limits to eval RCE is that eval can't execute very sophisticated queries, unlike 'exec'.
#
# A better option to convert a string to list would be to use 'ast.literal_eval(string)'. This will throw an error if the statement is not a list, but the evil code will not be executed.

