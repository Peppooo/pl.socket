import socket
import sys
import os

def send_commands(s, conn):
    print("$~: ", end="")
    while True:
        try:
            cmd = input()
            if cmd == "exit":
                conn.close()
                s.close()
                sys.exit()
            if cmd == "clear":
                os.system("cls")
                cmd = ""
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(4096)
                print(data.decode("utf-8"), end="")
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            sys.exit()         
        
def server(address):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Inizializzato. Sono in ascolto...")
    except Exception as e:
        print("\nSembra che qualcosa sia andato storto.")
        print(e)
        restart = input("\nVuoi che reinizializzi il server? s/n ")
        if restart.lower() == "s" or restart.lower() == "si":
            exit(1)
            server(address)
        else:
            sys.exit()
    conn, client_addr = s.accept()
    print(f"Connessione Stabilita: {client_addr}")
    send_commands(s, conn)


if __name__ == "__main__":
    try:
        host = sys.argv[1]
    except:
        host = socket.gethostbyname(socket.gethostname())
    try:
        port = int(sys.argv[2])
    except:
        port = 12000
    print(f"Host: {host}   Port: {str(port)}")
    server((host, port))
