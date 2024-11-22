import turtle
import time
import random

WIDTH, HEIGHT = 500, 500 #TAMAÑO DE LA VENTANA DEL JUEGO
COLORS = ['red', 'blue', 'cyan','green', 'orange', 'yellow', 'black', 'brown', 'purple', 'pink']

def get_number_of_racers():
    racers = 0
    
    while True:
        racers = input("Ingrese el numero de corredores (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Ingrese un numero... intente de nuevo!")
            continue
    
        if 2 <= racers <= 10:
            return racers
        else:
            print("Ingrese un numero que este dentro del rango (2 - 10)... intente de nuevo!")
            continue
        
def race(colors):
    turtles = create_turtles(colors)  
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance) #A QUE DISTANCIA SE MOVERA EL OBJETO
            x, y = racer.pos() #MUESTRA LA POSICION ACTUAL DEL CURSOR O LA TORTUGA
            
            if y >= HEIGHT//2 - 10: #SI LLEGA AL TOPE DE LA VENTANA 10px de la barra del titulo
                return colors[turtles.index(racer)]
        
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1) #ANCHO COMPLETO / JUGADORES MAS 1 PARA HACER ESPACIO A LOS LADOS
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #Establecer la posicion para 2 jugadores
        # x = -500//2 + (1 + 1) * 166
        # x = -250 + 2 * 166
        # x = -250 + 332
        # x1 = -84
        # x2 = 82
        x = -WIDTH//2 + (i + 1) * spacingx
        
        # y = -500//2 + 20
        # y = -250 + 20 -> El 20 es el tamaño de la tortuga
        # y = -230
        y = -HEIGHT//2 + 20
        
        racer.setpos(x,y)
        racer.pendown()
        turtles.append(racer)
    
    return turtles    

#CREAMOS LA INTERFAZ GRAFICA BASICA DE LA APLICACION
def init_turtle():
    screen = turtle.Screen() #UTILIZAMOS LA CLASE SCREEN
    screen.setup(WIDTH, HEIGHT) #LE DAMOS VALORES A LAS DIMENSIONES
    screen.title("Carrera de tortugas!") #EL TITULO DE LA VENTANA

racers = get_number_of_racers() 
init_turtle()
random.shuffle(COLORS) #BARAJEA LOS COLORES DEL ARRAY
colors = COLORS[:racers] #SELECCIONA LOS COLORES DEPENDIENDO DE LA CANTIDAD DE JUGADORES
winner = race(colors) 
print("El ganador es la tortuga de color:",winner)
time.sleep(3)

'''
racer = turtle.Turtle()
racer.speed(1)
racer.penup() #No dibuja la linea o el movimiento
racer.shape("turtle")
racer.color("cyan")
racer.forward(100)
racer.pendown() #Dibuja la linea del movimiento
racer.left(90) #RECIBER EL VALOR EN ANGULOS POR EL CUAL VA A ROTAR EL OBJETO COMENZANDO DESDE LA IZQUIERDA
racer.forward(100)
racer.right(150) #RECIBER EL VALOR EN ANGULOS POR EL CUAL VA A ROTAR EL OBJETO COMENZANDO DESDE LA DERECHA
racer.backward(100) 
'''

#time.sleep(5) #TIEMPO QUE SE MANTENDRA LA VENTANA ABIERTA DESPUES DE EJECUTARSE EL CODIGO