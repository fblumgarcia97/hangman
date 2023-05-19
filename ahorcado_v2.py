from encodings import utf_8
from os import system
from secrets import choice
from draw import draw
import time


def readData():
    words = [] 
    with open("./archivos/data.txt", "r", encoding="utf_8") as f: #Abre el archivo como lectura
        for word in f:
            words.append(str(word)) #Se añade a una lista
    return choice(words) # escoje una palabra aleatoria


def play():
    word = readData().upper() #llama la función leer 
    print(word)
    downG = ["_" for i in range(len(word)-1)] #imprime todos los _ con la cantidad de letras
    full = 0
    countLose = 0
    countWin = 0
    wordsUser = [] #Para guardar las letras seleccionadas
    while(full != 5):
        time.sleep(2)
        system("cls")  
        print(" ".join(downG)) #Une los _ para verse más estético       
        print("Ya has seleccionado: ") 
        print(sorted(wordsUser))
        wordUser = input("Ingrese una letra: ").upper()
        if wordUser.isalpha() and len(wordUser)==1: #es alfabeto y tiene un elemento
            wordsUser.append(wordUser)
            if wordUser in word: #Comprueba que la letra este dentro de la palabra
                if countWin == len(word) - 2:
                    print("¡¡¡¡¡¡Has ganado!!!!!")
                    print("La palabra es " + word)
                    break
                else:                        
                    count = word.count(wordUser) #Cuantas veces esta dentro de la palabra
                    countWin = countWin + count
                    print("La letra " + wordUser + " esta "+ str(count) + " veces.")
                    countLetter = 0 # Un contador para ubicar la letra donde es
                for i in word: # ciclo que ubica la letra en posición
                    if i == wordUser:
                        downG[countLetter] = wordUser                        
                    countLetter = countLetter + 1
            else:                
                print("No esta la letra " + wordUser) 
                print(draw[countLose]) # Dibuja el muñeco correspondiente
                if countLose == len(draw) - 1: # Cuando acaba los intentos vuelve al menú
                    print("¡¡¡¡¡Has perdido!!!!")
                    break
                else: #Resta a los intentos
                    countLose = countLose + 1 
        else:
            print("Ingrese una sóla letra")
            

def menu():
    print("¡¡¡Bienvenido!!! al juego del ahorcado por fblumgarcia".center(60, " "))
    option = 9
    while(option != 2): #Para hacer que el menú corra indefinidamente
        time.sleep(2) #Tiempo de espera de 2 s
        system("cls") # Borra lo de la pantalla
        print("\n 1. Jugar \n 2. Salir \n")
        try: # Esto sirve para restringir la entrada de sólo números 
            option = int(input("Seleccione una opción: "))
            if option == 1:
                play() #Abre la función jugar
            elif option == 2:
                option = 2
            else:
                print("Ingrese una opción correcta")
        except ValueError:
            print("Ingrese sólo números")        
    print("¡¡¡Espero te haya gustado el juego!!!".center(60, " ")) 

def main():
    menu()

if __name__ == "__main__":
    main()