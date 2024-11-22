#SE ABRE EL ARCHIVO EN SOLO LECRUTA Y SE GUARDA EN UNA VARIABLE GLOBAL EL CONTENIDO
with open("story.txt","r") as f:
    story = f.read()

#words = [] CREANDO UN ARRAY DE PALABRAS EL PROBLEMAS ES QUE ACEPTA DUPLICADOS
words = set() #UNA LISTA
start_of_words = -1 

target_start = "<"
target_end = ">"

# SE RECORRE TODO EL CONTENIDO CARACTER POR CARACTER
#FINALIDAD: SELECCIONAR LAS PALABRASE QUE ESTAN ENTRE LLAVES ANGULADAS
for i, char in enumerate(story):
    #print("#",i,"character:",char)
    if char == target_start:
        start_of_words = i
        
    if char == target_end and start_of_words != -1:
        word = story[start_of_words : i + 1]
        #words.append(word) #AGREGANDO UNA PALABRA AL ARRAY
        words.add(word) #AGREGANDO UNA PALABRA A LA LISTA
        start_of_words = -1

answers = {}

#SE LE PIDE AL USUARIO QUE INGRESE LA PALABRA RESPECTIVA A LA PALABRA CLAVE QUE SE LE PIDE
for word in words:
    answer = input("Ingrese una palabra para: " + word + ": ")
    answers[word] = answer
    
#SE REEMPLAZAN TODAS LA PALABRAS EN EL CONTENIDO ORIGINAL PARA MOSTRAR UNA HISTORIA PERSONALIZADA
for word in words:
    #SE REESCRIBE EL VALOR DE STORY YA QUE LA SENTENCIA CREA UNA NUEVA CADENA 
    story = story.replace(word, answers[word])

print(story)