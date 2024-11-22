import random

#SE CREA UNA VALOR DE LA RULETA DE FORMA ALEATORIA DEL 1 A 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll

#SE PIDE AL USUARIO QUE INTRODUZCA LA CANTIDAD DE JUGADORES
while True:
    players = input("Introduzca el numero de jugadores (2 - 4): ")

    #SE VALIDA QUE SEA UN NUMERO    
    if(players.isdigit()):
        players = int(players)
        
        #SE VALIDA LA CANTIDAD DE JUGADORES EVALUANDO EN RANGO
        if (2 <= players <= 4):
            break
        else:
            print("Deberian de ser entre 2 a 4 jugadores")
    else:
        print("Invalido. Intente de nuevo.")

#PUNTUACION MAXIMA DEL JUEGO        
max_score = 50
#SE CREA UN ARRAY DINAMICO PASANDO LA CANTIDAD DE JUGADORES
#CADA JUGADOR TOMA POR DEFECTO EL VALOR DE 0 INICAL
player_score = [0 for _ in range(players)]

#LA RONDA SE TERMINA CUANDO ALGUN JUGADOR ALCANCE SU MAXIMO PUNTAJE
while max(player_score) < max_score:
    
    #RONDA PARA CADA JUGADOR
    for player_idx in range(players):
        print("\nJugador número (", player_idx + 1, ") <--- ¡ESTA EN TURNO!")
        print("Su puntuación total es:", player_score[player_idx],"\n")
        
        current_score = 0
        
        #RONDA DE TIRADAS Y ACUMULACION DE PUNTOS DE CADA JUGADOR
        while True:
            should_roll = input("¿Te gustaría tirar? (y): ")
            
            #SE LE PREGUNTA SI DESEA CONTINUAR CON EL JUEGO
            if should_roll.lower() != "y":
                break
            
            #GENERANDO EL VALOR
            value = roll()
            
            #SI ES UNO SE LE TERMINA EL TURNO
            #SINO ENTONCES SE VAN SUMANDO A LA PUNTUACION TOTAL DEL TURNO EN MARCHA
            if(value == 1):
                print("Te ha salido un 1! Turno terminado")
                current_score = 0
                break
            else:
                current_score += value
                print("Te a salido:", value)
            
            #SE IMPRIME LA PUNTUACION ACTUAL DEL TURNO
            print("Tu puntuacion es: ", current_score)
        
        #SE IMPRIME LA PUNTUACION OBTENIDA DE TODOS LOS TURNOS QUE HA JUGADO
        player_score[player_idx] += current_score    
        print("Su puntuación total es:", player_score[player_idx])
        
#SE SELECCIONA EL MAXIMO PUNTAJE Y AL JUGADOR CON ESE RESPECTIVO
max_score = max(player_score)
winnig_idx = player_score.index(max_score)
print("Jugador número (", winnig_idx+1 ,")<-- es el GANADOR con", max_score, "puntos")