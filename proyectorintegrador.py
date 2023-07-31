import readchar
from readchar import readkey, key
def Juego():
    d=0
    jueg=True
    while d==0:
        print(f"Bienvenido al juego del laberinto, escribe tu nombre para comenzar")
    nombre=input()
    if nombre =="1":
        d=1
    else:
        print(f"Escribe algo aleatorio")
        while jueg == True:
            tecla = readchar.readkey()
            teclaespecial= readkey()
            print(tecla, end="")
            if teclaespecial == key.UP:
                print(f"Gracias por jugar")
                break

if __name__ == "__main__":
    Juego()