import getpass
#imports the 'getpass' library

user = getpass.getuser()
#Uses getpass to get the current user

if user == "root":
    #If the user is 'root'
    print("[+] You Are Authorized. The Password Is abc123")
    
else:
    print("[-] You Are Not Authorized.")
    exit()
    
input("Press Enter To Exit >> ")
exit()

# The problem with 'getpass.getuser()' is that it searches for environment variables to get the username of the current logged in user, and environment variables can be manipulated.
#
# getpass.getuser() checks the following environment variables : LOGNAME, USER, LNAME and USERNAME
#
# On Unix/Linux, you can use the following code to bypass this program :
#           export LOGNAME='root'
#           export USER='root'
#           export LNAME='root'
#           export USERNAME='root'

