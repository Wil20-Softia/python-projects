#NUMBER GUESSER
import random

#LIMITE MAXIMO DEL JUEGO
top_of_range = input("Tye of number: ")

#VALIDANDO EL NUMERO
if(top_of_range.isdigit()):
    top_of_range = int(top_of_range)
    
    if(top_of_range<=0):
        print("Please type a number larger than 0 next time!")
        quit()
else:
    print("Please type of number next time.")
    quit()

#CREANDO UN NUMERO ALEATORIO 
random_number = random.randint(0, top_of_range)
#print(random_number)
guesses = 0 #OPORTUNIDAD

while True:
    guesses += 1
    #PIDIENDO AL USUARIO UN NUMERO
    user_guess = input("Make a guess: ")
    #VALIDANDO
    if(user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    #SI ES IGUAL AL NUMERO ALEATORIO GANA
    if(user_guess == random_number):
        print("You got it!")
        break
    else:
        #SI ES MAYO SE LE DICE QUE ES MUY ALTO Y VICEVERZA
        if(user_guess > random_number):
            print("You were above the number!")
        else:
            print("You were below the number!")

#INFORMANDO EN CUANTAS OPORTUNIDADES TERMINO EL JUEGO
print("You got it in",guesses,"guesses")