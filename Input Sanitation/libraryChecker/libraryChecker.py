import socket
# A simple application to check if a Python library exists.
def main():
    try:
        print("\nA simple Python app to check if library exists!")
        ip = input("IP To Bind On [default 127.0.0.1] : ")
        if ip == "":
            ip == '127.0.0.1'
        port = input("Port To Bind On : ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            port = int(port)
        except:
            print("Invalid Port Number")
        print("Binding...")
        s.bind((ip, port))
        print("Binded Successfully, Starting Listener")
        s.listen(0)
        while True:
            print("Waiting For Connection")
            conn,addr = s.accept()
            print("Connection Recieved From " + str(addr))
            data = conn.recv(1024)
            library = data.decode()
            try:
                #Here is the exploit.
                #The Python program executes a query from the user without checking the contents of it, leading to remote code execution (RCE)
                exec("import " + library)
                conn.send(b"[+] Library Does Exist")
            except Exception as e:
                print(e)
                conn.send(b"[-] Library Does Not Exist")
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            print("Connection Closed Successfully\n")
    except Exception as e:
        print(e)

while True:
    main()
