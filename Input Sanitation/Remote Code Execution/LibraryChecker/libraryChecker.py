import socket
# A simple application to check if a Python library exists.
def main():
    try:
        print("\nA simple Python app to check if library exists!")
        ip = input("IP To Bind On [default 127.0.0.1] : ")
        #Defaults to 127.0.0.1 (localhost)
        if ip == "":
            ip == '127.0.0.1'
        port = input("Port To Bind On : ")
        #Initialises socket type
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Checks if port is a valid integer
        try:
            port = int(port)
        except:
            print("Invalid Port Number")
        print("Binding...")
        #Binds on the specified port and IP
        s.bind((ip, port))
        print("Binded Successfully, Starting Listener")
        #Starts Listening On Port
        s.listen(0)
        while True:
            print("Waiting For Connection")
            #Waits for a connection and saves the connection object to 'conn' and the connected IP/Port to 'addr'. The 'conn' variable handles sending and receiving data between the client (attacker) and the server (target).
            conn,addr = s.accept()
            print("Connection Recieved From " + str(addr))
            #Receives sent data
            data = conn.recv(1024)
            #Decodes data and saves it to a variable called 'library'
            library = data.decode()
            try:
                #Here is the exploit.
                #To check if the library is valid, the Python program executes a query from the user without checking the contents of it, leading to remote code execution (RCE).
                exec("import " + library)
                #If this hasn't thrown an error, the library does exist
                conn.send(b"[+] Library Does Exist")
            except Exception as e:
                #If the try statement threw an error while importing the library, it means that the library does not exist
                print(e)
                conn.send(b"[-] Library Does Not Exist")
            #Shuts down and closes the connection
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            print("Connection Closed Successfully\n")
    except Exception as e:
        print(e)

#Runs forever
while True:
    main()
