import os, readchar
from readchar import readkey
def borrar_terminal():
    cont=0
    print("Bienvenido a borrar ternminal")
    while cont <50:
        tecla = readchar.readkey()
        if ord(tecla)>0:
            os.system('cls' if os.name=='nt' else 'clear')
            cont=cont+1
            print(cont)

if __name__ == "__main__":
    borrar_terminal()