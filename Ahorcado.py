#Juego del ahorcado
from os import system
import time
import random
while True:
    print("¡¡¡Bienvenido!!! al juego del ahorcado por FBG97".center(60," "))
    palabras=[["ARGENTINA","BRASIL","COLOMBIA","ITALIA","ALEMANIA"],["FRESA","MORA","GUAYABA","MANGO","BANANO"],["POP","ROCK","VALLENATO","REGGAE","CARRANGA"],["PERRO","IGUANA","GATO","ARDILLA","SAPO"]]
    menu=["1Países","2Frutas","3Géneros musicales","4Animales"]
    for i in range(len(menu)): #Imprimir menú
        print(f"{i+1}. {menu[i][1:]}")
    selec=int(input("Seleccione la categoria de juego: "))
    pal=palabras[selec-1][random.randint(0,4)] #Aleatorio de palabra según categoria
    lispal=list(pal) #Lista de la palabra
    lisbus=[] #lista que busca usuario
    letselec=[] #Lista de letras seleccionadas
    conterror=0
    contpal=0
    ahorcado=['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']
    for i in range(len(lispal)): #Para crear la misma longitud de que se busca y la real
        lisbus.append("_")
    print(lisbus)
    while True:
        time.sleep(2)
        system("cls")
        print(lisbus)
        print(f"Usted ha elegido: {letselec}")
        if contpal==len(lisbus):
            print(f"Usted ha completado la palabra y es: {pal}".center(100," "))
            desea=int(input("Desea vover a jugar:\n1. Si 2. No\n"))
            if desea==2:
                quit()
            elif desea==1:
                break
        else:
            ingpal=str(input("Favor ingrese la letra: ")).upper()
            if ingpal in letselec:
                continue
            else:
                letselec.append(ingpal)
                letselec.sort()
                if ingpal in lispal:
                    cuent=lispal.count(ingpal)
                    if cuent==1:
                        ind=lispal.index(ingpal)
                        lisbus[ind]=ingpal
                        contpal=contpal+1
                        print("La letra esta")
                    else:
                        for i in range(cuent):
                            ind=lispal.index(ingpal)
                            lisbus[ind]=ingpal
                            lispal[ind]="0"
                            contpal=contpal+1
                        print("La letra esta")                
                else:
                    if conterror<6:
                        print(ahorcado[conterror])
                        conterror=conterror+1
                    else:
                        print("¡¡¡¡Has perdido!!!!".center(60," "))
                        print(ahorcado[conterror].center(60," "))
                        desea=int(input("Desea vover a jugar:\n1. Si 2. No\n"))
                        if desea==2:
                            quit()
                        elif desea==1:
                            break