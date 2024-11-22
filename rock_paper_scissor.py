import random

user_wins = 0
compurer_wins = 0

options = ["piedra", "papel", "tijera"]


print("\n***************************    BIENVENID@  **************************")
print("*************  JUGAREMOS A PIEDRA, PAPEL O TIJERA  ******************")
print("_____________________________________________________________________")
print("_____________________________________________________________________")
print("ENTONCES, COMENCEMOS. ¡BUENA SUERTE! >>>>>>>>>>>>\n")

while True:
    option_user = input("¿piedra, papel o tijera? // ó Q para sailr   -->> ").lower()

    if option_user == "q":
        break
    
    if option_user not in options:
        print("xx La Opción no existe xx")
        continue
    
    random_number = random.randint(0, 2)
    
    #0 piedra - 1 papel - 2 tijera
    computer_pick = options[random_number]
    print("La computadora bota: ", computer_pick)
    
    if option_user == "piedra" and computer_pick == "tijera":
        print("*** :D Suertud@ ¡Has ganado! :D ***")
        user_wins += 1
    elif option_user == "papel" and computer_pick == "piedra":
        print("*** :D Suertud@ ¡Has ganado! :D ***")
        user_wins += 1
    elif option_user == "tijera" and computer_pick == "papel":
        print("*** :D Suertud@ ¡Has ganado! :D ***")
        user_wins += 1
    else:
        print("xxx ¡Mala racha, Perdiste! :( xxx")
        compurer_wins +=1
        
print(">>>>>>>> Has tenido <", user_wins, "> VICTORIAS")
print(">>>>>>>> La computadora ha ganado <", compurer_wins, "> veces")
print("__________________________________________")
print("*************    ADIOS  ******************")