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

# A problem with 'getpass.getuser()' is that it searches for environment variables to get the username of the current logged in user, and environment variables can be manipulated.
#
# On Unix/Linux systems, getpass.getuser() checks the following environment variables : LOGNAME, USER, LNAME and USERNAME
# And on Windows systems, getpass.getuser() checks the 'USERNAME' environment variable.
#
#
# On Unix/Linux, the following command line calls can be used to bypass this program :
#           export LOGNAME='root'
#           export USER='root'
#           export LNAME='root'
#           export USERNAME='root'
#
# And on Windows :
#           set USERNAME='root'
