import random
import numpy as np
from collections import Counter
import string
#funcion que devuleve el cuadrado de un arreglo
def cuadrados(arreglo):
    cuadrados = 0
    for i in range(len(arreglo)):
        cuadrados = cuadrados + arreglo[1]**2
    return print(cuadrados)
cuadrados([1,2,3])
#funcion que ordena un arreglo
def ord_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]


elementos = [8, 3, 1, 19, 14]
ord_burbuja(elementos)

print(elementos)
#funcion auxilia de contar_lista que cuenta cuantas veces ocurre una palabra especifica en una lista
def count(palabra,lista):
    contador = 0
    for i in range(len(lista)):
        if(palabra == lista[i]):
            contador = contador + 1
    return contador
#funcion que nos devuleve el numero de ocurreciencia de cada elemento de una lista
def contar_lista(lista):
    final_list = []
    for i in range(len(lista)):
        palabra = lista[i]
        n = count(palabra, lista)
        if (palabra, n) not in final_list:
            final_list.append((palabra, n))
    return final_list

print(contar_lista(["jorge","jorge","eduardo","pescado","goma"]))
#funcion que da la reversa de una serie de elementos que un usario ingresa
def inversa():
    pila = []
    reversa = []   
    n = int(input("¿Cuántos elementos vas a ingresar?\n"))
    for i in range(n):  
        entrada = input("\nIngresa el elemento: \n")
        pila.append(entrada)        
    while pila:    
        reversa.append(pila.pop())  
    print("La lista inversa es:", reversa)     
inversa() 
#funcion que elimina caracteres de una cadena y la devuelve
def eliminacion_caracteres(cadena):
    cadena_final = ""
    #caracteres que elimina
    caracteres_list = [",", ";", ":", ".", "'"]
    for i in range(len(cadena)):
        #checa en cada iteracion si el elemento de la cadena corresponde a lista de caracteres si es asi los ignora si no los concatena
        if cadena[i] not in caracteres_list:  
            cadena_final = cadena_final + cadena[i]
    return print("cadena sin caracteres:",cadena_final)
eliminacion_caracteres("hola; como'. estas;;;;")
def lanzamiento(arreglo):
    resultado = random.choice(['Sol', 'Águila'])
    if resultado == 'Sol':
        arreglo.insert(0, '*')  # Agrega una celda a la izquierda por Sol
    else:
        arreglo.append('*')  # Agrega una celda a la derecha por Águila

def simular_lanzamientos():
    arreglo = ['*']

    while True:
        n = int(input("Ingrese el número de lanzamientos (n): "))

        for _ in range(n):
            lanzamiento(arreglo)

        print("Estado actual del arreglo:", arreglo)

        continuar = input("¿Desea realizar más lanzamientos? (si/no): ").lower()
        if continuar != 'si':
            break

# Ejecutar la simulación
simular_lanzamientos()
def lanzamiento_tetraedro():
    arreglo = [0]  # Arreglo inicial de tamaño 1x1
    salida = False
    
    while not salida:
        opcion = int(input("Elige una opción:\n1 - Hacer lanzamientos\n2 - Salir\n"))
        if opcion == 1:
            lanzamientos = int(input("Dame el número de lanzamientos:\n"))
            for i in range(lanzamientos):
                cara = random.randint(1, 4)
                if cara == 1:
                    arreglo.insert(0, 0)  # Agrega una celda a la izquierda
                elif cara == 2:
                    arreglo.append(0)  # Agrega una celda a la derecha
                elif cara == 3:
                    nuevo_arreglo = [0] * (len(arreglo) + 1)  # Crea un nuevo arreglo con una fila más arriba
                    nuevo_arreglo[:len(arreglo)] = arreglo
                    arreglo = nuevo_arreglo
                else:
                    nuevo_arreglo = [0] * (len(arreglo) + 1)  # Crea un nuevo arreglo con una fila más abajo
                    nuevo_arreglo[1:] = arreglo
                    arreglo = nuevo_arreglo
                
                print("Arreglo actual:", arreglo)
        elif opcion == 2:
            salida = True
        else:
            print("Escogiste una opción incorrecta, vuelve a intentarlo")

lanzamiento_tetraedro()   

def escalar_matriz(matriz):
    matriz_log = np.log(matriz)
    matriz_sqrt = np.sqrt(matriz)
    matriz_05 = np.power(matriz, 0.5)

    return matriz_log, matriz_sqrt, matriz_05

# Ejemplo de uso
filas = int(input("Ingrese el número de filas (m): "))
columnas = int(input("Ingrese el número de columnas (n): "))

# Lectura de la matriz
matriz_original = np.zeros((filas, columnas))
for i in range(filas):
    for j in range(columnas):
        matriz_original[i, j] = float(input(f"Ingrese el elemento [{i+1}, {j+1}]: "))

# Escalar la matriz
matriz_log, matriz_sqrt, matriz_05 = escalar_matriz(matriz_original)

# Mostrar resultados
print("\nMatriz Original:\n", matriz_original)
print("\nMatriz Escalada (Logaritmo):\n", matriz_log)
print("\nMatriz Escalada (Raíz Cuadrada):\n", matriz_sqrt)
print("\nMatriz Escalada (Potencia 0.5):\n", matriz_05)

#Se usa la biblioteca NumPy para realizar las operaciones de escalamiento. Ingresa las dimensiones de la matriz y luego proporcionas los elementos de la matriz. El programa devuelve la matriz original y las versiones escaladas utilizando logaritmo, raíz cuadrada y potencia de 0.5.

def identificar_enfermedad(sintoma):
    enfermedades = {
        'fiebre': 'Resfriado común',
        'dolor de cabeza': 'Migraña',
        'tos': 'Bronquitis',
        'dolor abdominal': 'Gastritis',
        'fatiga': 'Anemia',
        'dolor en las articulaciones': 'Artritis',
        'sibilancias al respirar': 'Asma'
        # Puedes agregar más síntomas y enfermedades aquí
    }

    enfermedad = enfermedades.get(sintoma.lower(), 'No se puede identificar la enfermedad')
    return enfermedad
def enfermedad():
    sintoma_usuario = input("Ingresa un síntoma: ")
    enfermedad_identificada = identificar_enfermedad(sintoma_usuario)
    print(f"Según el síntoma '{sintoma_usuario}', podrías tener: {enfermedad_identificada}")

enfermedad()
def contar_palabras_iguales_entre_documentos(ruta_documento1, ruta_documento2):
    try:
        with open(ruta_documento1, 'r') as archivo1, open(ruta_documento2, 'r') as archivo2:
            contenido_doc1 = archivo1.read()
            contenido_doc2 = archivo2.read()
            palabras_doc1 = contenido_doc1.split()
            palabras_doc2 = contenido_doc2.split()

            palabras_iguales = set(palabras_doc1) & set(palabras_doc2)
            cantidad_palabras_iguales = len(palabras_iguales)
            return cantidad_palabras_iguales
    except FileNotFoundError:
        return "Al menos uno de los archivos no fue encontrado"

# Ejemplo de uso:
ruta_documento_1 = "Descargas/P/texto.txt"  # Reemplaza con la ubicación y nombre de tu primer archivo
ruta_documento_2 = "Descargas/P/texto.txt"  # Reemplaza con la ubicación y nombre de tu segundo archivo

resultado = contar_palabras_iguales_entre_documentos(ruta_documento_1, ruta_documento_2)
print(f"La cantidad de palabras iguales en ambos documentos es: {resultado}")

def mostrar_frecuencia_palabras(nombre_archivo):
    # Leer el archivo y procesar las palabras
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().lower()  # Leer contenido y convertirlo a minúsculas
        # Quitar puntuaciones
        contenido = contenido.translate(str.maketrans('', '', string.punctuation))
        palabras = contenido.split()

    # Contar la frecuencia de las palabras
    conteo_palabras = Counter(palabras)

    # Obtener las palabras y sus frecuencias más comunes
    palabras_comunes = conteo_palabras.most_common(10)  # Cambia el número para mostrar más o menos palabras

    # Mostrar las palabras y sus frecuencias
    print("Palabra : Frecuencia")
    for palabra, frecuencia in palabras_comunes:
        print(f"{palabra} : {frecuencia}")

# Llamar a la función con el nombre de tu archivo
mostrar_frecuencia_palabras('Descargas/P/texto.txt') #cuida de poner bien la ruta del txt si no no funciona










