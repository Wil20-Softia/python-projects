import random
import string

def generate_password(min_length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    #print(letter,digits,special)
    
    characters = letters
    
    if numbers:
        characters += digits
    
    if special_character:
        characters += special
    
    pwd = ""
    
    meets_criteria = False
    has_number = False
    has_special = False
    
    #MIENTRAS meets_criteria SEA FALSO O EL TAMÑANO DE LA PASSWORD SEA MENOR AL TAMAÑO PERSONALIZADO
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char #SE AGREGA UN CARACTER
        
        if new_char in digits: #SI EL CARACTER ES UN DIGITO
            has_number = True #has_number = True que es igual a decir que tiene un numero
        elif new_char in special: #SI EL CARACTER ES UN SIGNO DE PUNTUACION
            has_special = True #has_special = True  que es igual a decir que tiene un signo de puntuacion
        
        #SE LE COLOCA TRUE YA QUE EL BUCLE TERMINA CUANDO ESTE SE HACE TRUE Y LLEGA AL MAXIMO DEL
        #TAMAÑO REQUERIDO
        #QUE QUIERE DECIR QUE SINO SE SOLICITA ALGUNO DE LOS CRITERIOS ESTE SE HACE TRUE 
        #Y SOLO FALTARIA CUMPLIR CON EL TAMAÑO DE LA CONTRASEÑA, SINO ENTONCES 
        #ESTE TOMA EL VALOR DE HAS_NUMBER O HAS_ESPECIAL TANTO COMO SI SE SOLICITO UNO U OTRO
        #PARA ROMPER EL CICLO
        meets_criteria = True
        
        if numbers: #SI EL USUARIO QUIERE NUMEROS EN SU CONTRASEÑA ENTONCES
            meets_criteria = has_number
        
        if special_character: #SI EL USUARIO QUIERE CARACTERES ESPECIALES EN SU CONTRASEÑA ENTONCES
            meets_criteria = meets_criteria and has_special
            
    
    return pwd

length_pwd = int(input("Ingrese el tamaño de la contraseña: "))
has_number = input("Desea que tenga números? (y/n): ").lower() == "y"
has_special = input("Desea que tenga caracteres especiales? (y/n): ").lower() == "y"

pwd = generate_password(length_pwd, has_number, has_special)
print(pwd)