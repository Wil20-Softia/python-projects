#pip install windows-curses
#LIBRERIA PARA TRABAJAR CON LA CONSOLA Y PODER MANIPULARLA EN WINDOWS
import curses
from curses import wrapper
import time
import random

#MOSTRANDO LA PANTALLA AL PRINCIPIO DE LA APLICACION
def startscreen(stdscr):
    stdscr.clear() #LIMPIA LA CONSOLA
    stdscr.addstr("Bienvenido a la prueba de velocidad de tecleado!")
    stdscr.addstr("\nPresione una tecla para empezar!")
    stdscr.refresh() #COLOCA EL CURSOR AL INICIO
    stdscr.getkey() #OBTIENE LA TECLA PULSADA

#RECIBE EL OBEJETO PARA TRABAJAR EN LA CONSOLA
#LA LINEA DE TEXTO A EVALUAR
#EL TEXTO QUE SE ESTA ESCRIBIENDO
#Y EL WPM
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target) #SE IMPRIME LA LINEA DE TEXTO
    stdscr.addstr(1, 0, f"WPM: {wpm}") #SE IMPRIME EL WPM
    
    #BUCLE QUE EVALUA CARACTER POR CARACTER PARA PINTALO, SI ESTA MAL O BIEN
    for i, char in enumerate(current):
        correct_char = target[i] #OBTENEMOS EL CARACTER DE LA LINEA DE TEXTO
        color = curses.color_pair(1) #SE CONFIGURA AL COLOR CORRECTP
        
        #SE EVALUA PARA VER SI EL CARACTER CONINCIDE AL DE LA LINEA
        if char != correct_char:
            color = curses.color_pair(2) #SE CONFIGURA EL COLOR DE ERROR
            
        stdscr.addstr(0, i, char, color) #SE SOBREESCRIBE LA LINEA CON EL CARACTER Y EL COLOR RESPECTIVO

#PARA CARGAR LAS LINEAS DE TEXTOS GUARDADAS EN UN ARCHIVO .TXT EN LA MISMA DIRECCION
def load_text():
    with open("text.txt","r", encoding="utf-8") as f:
        lines = f.readlines()
        return random.choice(lines).strip() 


def wpm_test(stdscr):
    target_text = load_text() #CARGA LA LINEA ALEATORIA CONTENIDA EN EL ARCHIVO
    current_text = []
    wpm = 0
    start_time = time.time() #SE COMIENZA UN CONTADOR DE SEGUNDOS
    stdscr.nodelay(True) #PARA EVITAR EL BLOQUEO POR NO PULSAR UNA TECLA
    
    while True: #EL WHILE FUNCIONARA COMO UN ESCUCHADOR DE EVENTOS --> EVEN LOOPS
        #TIEMPO TRANSCURRIDO SE RESTA EL VALOR ACTUAL AL VALOR EN QUE SE INICIO LA PRUEBA
        #SI EL VALOR DE LA RESTA ES MENOR A UNO ENTONCES TOMA ESE VALOR DE 1
        time_elapsed = max(time.time() - start_time, 1) #MILISEGUNDOS EN DECIMALES
    
        #MUESTRA LA CANTIDAD DE PALABRAS POR MINUTO EL 5 ES LA LONGITUD MEDIA DE UNA PALABRA
        #DIVIDE LA CANTIDAD DE LETRAS ENTRE LA CANTIDAD DE SEGUNDO
        #SI time_elapsed es 60 es igual 1 que significa 1 minuto
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        
        stdscr.clear() #BORRA LA PANTALLA DEL MENSAJE DE BIENVENIDA
        #INVOCAMOS A LA FUNCION QUE EVALUA LAS PALABRAS POR MINUTO
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        #EVALUAMOS EL TEXTO ESCRITO ACTUALMENTE Y LA LINEA DE PREBA
        #Y SI ES IDENTICO ENTONCES SE SALE DE LA PRUEBA
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        
        #UN TRY CATCH PARA CORREGIR EL ERROR DE PRESIONAR UNA TECLA
        try:
            key = stdscr.getkey()
        except:
            continue
        
        #SI PRESIONA ESCAPE ENTONCES SE SALE DEL PROGRAMA DE TECLEADO
        #REPRESENTACION NUMERICA ASCII DE LA TECLA ESCAPE
        if ord(key) == 27:
            break
        
        #SI SE PRESIONA LA TECLA DE BORRAR ENTONCES ELIMINAMOS EL ULTIMO CARACTER DEL ARRAY ESCRITO
        #SINO ENTONCES SE AGREGA EL CARACTER AL ARRAY
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):        
            current_text.append(key)
        
        
        
def main(stdscr):
    #SE DEFINEN COMO TIPO CONSTANTES PARA CONFIGURAR LOS COLORES A TRABAJAR EN EL CMD
    # COLOR 1 = LETRA NEGRA FODO VERDE
    # COLOR 2 = LETRA ROJA FODO BLANCO
    # COLOR 3 = LETRA BLANCA FODO NEGRO
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    #INICIA LA PANTALLA PRINCIPAL DEL JUEGO
    startscreen(stdscr)
    
    #COMIENZA EL BUCLE DEL JUEGO 
    while True:
        #EJECUTANDO LA FUNCION QUE PERMITE, MOSTRAR Y EVALUAR EL TEXTO ALEATORIO
        wpm_test(stdscr)
        
        #DESPUES QUE EVALUA EL TEXTO ENTONCES MUESTRA ESTE MENSAJE
        stdscr.addstr(2, 0, "Has completado el texto, Persione una tecla para continuar!")
        
        #SI PRESIONA ESCAPE SE SALE DEL PROGRAMA
        #SINO CONTINUA
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
    
wrapper(main)