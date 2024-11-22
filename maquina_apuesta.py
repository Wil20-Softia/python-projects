'''
TITULO: MAQUINA DE APUESTAS
DESCRIPCION: SIMULAR LAS FUNCIONES BASICAS DE UNA MAQUINA DE APUESTA QUE TENGA 4 SIMBOLOS DISTINTOS
DEBE PERMITIR AL USUARIO REGISTRAR UN CREDITO BASE POR EL CUAL JUGARA HASTA QUE SE LE AGOTE
EL JUEGO TENDRA 3 FILAS Y 3 COLUMNAS EL JUGADOR GANA SI ACIERTA LA CANTIDAD DE FILAS A APOSTAR
INFORMAR AL JUGADOR CUANTO TIENE DE CREDITO EN CADA RONDA DEL JUEGO Y SI HA GANADO, CUANTO HA
GANADA EN LA RONDA

LA MATRIZ DE 3X3 DE SIMBOLOS SE CREARA ALEATORIAMENTE
CADA SIMBOLO TENDRA DISTINTOS VALORES
A = 5
B = 4
C = 3
D = 2

APUESTA MAXIMA POR RONDA SERA DE $100

VALIDAR LA ENTRADA DE DATOS:
    EL CREDITO
    LAS FILAS A APOSTAR
    CANTIDAD DE DOLARES POR RONDA
'''
#MODULO PARA TRABAJAR CON NUMERO ALEATOREOS
import random

MAX_LINES = 3 #MAXIMO FILAS APUESTA
MIN_BET = 1 #MINIMO DE APUESTA
MAX_BET = 100 #MAXIMO DE APUESTA

ROWS = 3 #FILAS
COLS = 3 #COLUMNAS

#DICCIONARIO QUE CONTIENE LOS SIMBOLOS Y LA CANTIDAD MAXIMA A MOSTRAR DE CADA UNO
symbol_count = {
    "A": 2, #20% DE PROBABILIDAD DE QUE SALGA
    "B": 4, #40% DE PROBABILIDAD DE QUE SALGA
    "C": 6, #60% DE PROBABILIDAD DE QUE SALGA
    "D": 8, #80% DE PROBABILIDAD DE QUE SALGA
}

#ASIGNANDO VALORES EN DOLARES A LOS SIMBOLOS
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

#FUNCION QUE SIRVE PRINCIPALMENTE PARA CHEQUEAR LAS FILAS ACERTADAS
#RETORNA EL VALOR EN DOLARES Y LAS FILAS ACERTADAS
#RECIBE 
# EL ARRAY CREADO ALEATORIAMENTE -> columns [["A","A","D"],["B","C","B"],["C","C","B"]]
# CANTIDAD DE FILAS APOSTADAS -> lines
# APUESTA DE LA RONDA POR FILAS -> bet
# DICCIONARIO DE LOS VALORES DE CADA SIMBOLO -> values
def check_winnigs(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    
    #BUCLE PARA LA CANTIDAD DE LINEAS APOSTADAS
    for line in range(lines):
        #SE GUARDA EL PRIMER SIMBOLO DE LA PRIMERA COLUMNA-> "A"
        symbol = columns[0][line]
        
        #SE RECORREN TODAS LAS COLUMNAS
        for column in columns:
            #PARA CADA COLUMNA SE GUARDA EL SIMBOLO
            symbol_to_check = column[line]

            #SI EL SIMBOLO 
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    
    return winnings, winning_lines

#FUNCION QUE CREA LA MATRIZ ALEATORIA DE SIMBOLOS DE 3X3
#RECIBE CANTIDAD DE FILAS Y COLUMNAS Y EL DICCIONARIO DE SIMBOLOS
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] #CREANDO UN ARRAY VACIO
    #SE LLENA EL ARRAY all_symbols CON TODOS LOS VALORES EN EL DICCIONARIO
    #["A","A","B","B","B","B","C","C","C","C","C","C","D","D","D","D","D","D","D","D"]
    for symbol, symbol_count in symbols.items():        
        for _ in range(symbol_count):
            all_symbols.append(symbol) 
    columns = [] #ARRAY FUNDAMENTA PARA CREAR LA MATRIZ DE 3X3 ALEATORIA
    for _ in range(cols): #SE RECORRE HASTA EL NUMERO DE COLUMNAS
        column = [] #ARRAY PARA RELLENAR UNA COLUMNA
        current_symbols = all_symbols[:] #CREANDO UNA COPIA EXACTA DE TODOS LOS SIMBOLOS
        for _ in range(rows): #RECORRE HASTA EL NUMERO DE FILAS
            
            value = random.choice(current_symbols) #SELECCIONA UN VALOR AL AZAR DE TODOS LOS SIMBOLOS
            
            current_symbols.remove(value) #ELIMINA EL VALOR SELECCIONADO
            
            #["A"] - ["A","A"] - ["A","A","D"]
            column.append(value) #AGREGA EL ELEMENTO A LA COLUMNA
        
        #LUEGO QUE RELLENA LOS VALORES DEL LA FILA ENTONCES SE AGREGA AL LA COLUMNA
        #[["A","A","D"],["B","C","B"],["C","C","B"]]
        columns.append(column) 
    return columns #RETORNANDO EL ARRAY DE 3X3

#FUNCION QUE IMPRIME EL FORMATO DE TABLA PARA LA MATRIZ CREADA DE 3X3
#RECIBE POR PARAMETRO LA MATRIZ
def print_slot_machine(columns):
    #RECORRE EL TAMAÑO EXACTO DE LA FILA DE LA TABLA (3)
    #len(columns[0]) = 3 ["A","A","D"]
    for row in range(len(columns[0])):
        #IMPRIME UNA FILA
        #enumerate(columns) = 3 (3 elems dentro de columns)
        for i, column in enumerate(columns):
            #SI LA POSICION ACTUAL NO ES EL ULTIMO DE LA FILA SE IMPRIME -> A |
            #SINO SOLO SE IMPRIME EL CARACTER -> A
            '''
            i=0 i=1 i=2
            A |  B |  C  row = 0
            --------------
            A |  C |  C  row = 1
            --------------
            D |  B |  B  row = 2
            '''
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
            
        #SALTO DE LINEA POR FILA
        print()

#VALIDANDO DEPOSITO INICIAL
def deposit():
    while(True):
        amount = input("Introduzca el deposito: ")
        if(amount.isdigit()):
            amount = int(amount)
            if(amount>0):
                break
            else:
                print("El deposito tiene que ser mayor a 0")
        else:
            print("Introduzca un número por favor!")
    
    return amount

#VALIDANDO EL NUMERO DE FILAS A APOSTAR
def get_number_of_lines():
    while(True):
        lines = input("Introduzca el numero de lineas a apostar 1 y " + str(MAX_LINES) + ": ")
        if(lines.isdigit()):
            lines = int(lines)
            if(1<=lines<=MAX_LINES):
                break
            else:
                print("El numero de lineas debe de estar entr 1 y " + str(MAX_LINES))
        else:
            print("Introduzca un número por favor!")
            
    return lines

#VALIDANDO LA CANTIDAD DE DINERO A APOSTAR POR RONDA
def get_bet():
    while(True):
        amount = input("Introduzca el monto de la apuesta: ")
        if(amount.isdigit()):
            amount = int(amount)
            if(MIN_BET<=amount<=MAX_BET):
                break
            else:
                print(f"El monto debe de estar entre ${MIN_BET} y ${MAX_BET}")
        else:
            print("Introduzca un número por favor!")
            
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while(True):
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"No tienes suficiente dinero para apostar, el balance actual es de: ${balance}")        
        else:
            break
        
    print(f"Has apostado ${bet} en {lines} lineas. El total de la apuesta es ${total_bet}")
    
    #GENERANDO ALEATORIAMENTE LAS TRES LIENAS POR DEFECTO DE LOS SIMBOLOS
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    
    #IMPRIMIENDO LA MATRIZ GENERADA
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnigs(slots, lines, bet, symbol_value)
    
    print(f"Has ganado ${winnings}.")
    print(f"Has ganado en la(s) linea(s):", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"El credito total es de ${balance}")
        respuesta = input("Presione ENTER para continuar! o <q> para Salir!")
        if respuesta.lower() == "q":
            break
        
        balance += spin(balance)
        
    print(f"Tienes de credito ${balance}")

main()