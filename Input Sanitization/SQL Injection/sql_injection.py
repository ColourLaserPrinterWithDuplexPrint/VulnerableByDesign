print("[+] Creating Database...")

#Set The Username And Password Here
usernames = ["admin","ocelot"]
passwords = ["admin","P@55w0rd!"]

###################################

#Imports the 'sqlite3' library
import sqlite3

#Checks to see if file exists
try:
    #If the file does not exist, create a file called 'database'
    fileHandler = open('sqlDatabase','x')
    fileHandler.close()

    #Connect to the database
    con = sqlite3.connect("sqlDatabase")
    cursor = con.cursor()

    #Create a new table called 'users' with the values 'username' and 'password'
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username text, password text);")
    
except:
    #If the database already exists, connect to the database
    print("[?] Database Already Exists...")
    con = sqlite3.connect("sqlDatabase")
    cursor = con.cursor()

print("\n")

#Inserts the usernames and passwords into the database
for username,password in zip(usernames,passwords):
    cursor.execute("INSERT INTO users (username,password) VALUES('"+username+"','"+password+"');")
print("[+] Database Created")
#Run forever
while True:

    try:

        #Gets input for the username and password
        username = input("Username : ")
        password = input("Password : ")

        #Makes an SQL Query using the username and password from the inputs
        val = "SELECT username,password FROM users WHERE username = '"+username+"' AND password = '"+password+"';"

        print("[+] Running SQL Query : " + val)
        #Executes the SQL Query
        cursor.execute(val)

        #Saves the output of the SQL Query to 'queryOutput'
        queryOutput = cursor.fetchall()

        #Prints the output of the SQL Query
        print("[+] Output Of Query : " + str(queryOutput))
        
        #Checks if the query returned anything.
        if len(queryOutput) > 0:
            #Authenticate if the query returned anything
            print("[+] Authenticated")
        else:
            #If it didn't return anything, it means that there were no entries where the username and password matched up, so deny access.
            print("[-] Access Denied")
        print("\n")
        
    except Exception as e:
        #If an error happened, print the error
        print(e)
