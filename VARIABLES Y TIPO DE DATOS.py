#       VARIABLES Y TIPOS DE DATOS  

#Nivel Principiante (1-5):
"""
Asignación de variables: Crea variables con diferentes nombres y asígnales valores de distintos tipos de datos 
(números enteros, decimales, cadenas de texto, booleanos). Imprime el valor de cada variable.
"""
num = 10
floata = 15.5
string = "hola mundo"
bool = True
indefinido = None
lista = [1,10,20,30,40] #mutables e iterables
tupla = (10,"hola", True, 7.8)# INMUTABLES e iterables
diccionario = {"nombre":"alexander","edad":30, "estatura":180.1}#mutable e iterable
"""
Operaciones básicas: Realiza operaciones aritméticas básicas (+, -, *, /) 
con variables numéricas. Imprime el resultado de cada operación.
"""
num1 = 10
num2 = 20
sumar = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2
"""
Conversión de tipos: Convierte variables de un tipo de dato a otro 
(por ejemplo, de entero a flotante o de cadena a entero) utilizando las funciones de conversión adecuadas.
"""
numero1 = 10
numero_flotante = float(numero1)
print(numero_flotante)
"""
Entrada de datos por teclado: Solicita al usuario que ingrese un valor por teclado y 
almacena ese valor en una variable. Imprime el valor ingresado.
"""
usuario = input("ingresar dato: ")
print(usuario)
"""
Cadenas de texto: Concatenar, interpolar y dar formato a cadenas de texto 
utilizando las operaciones y funciones de cadenas de Python.
"""
texto1 = "hola"
texto2 =  "mundo"
oracion = texto1 + " " + texto2
print(oracion)
print(f"primer texto:{texto1}, segundo mensaje:{texto2}")

#Nivel Intermedio (6-10):
"""
Entrada y salida de archivos: Lee el contenido de un archivo de texto y almacena cada línea en una lista. 
Imprime el contenido de la lista o realiza alguna operación con los datos leídos.
"""
nombre_texto = input("ingresar nombre archivo: ")
def lector_archivo(nombre_texto):
    try:
        with open(nombre_texto,"r") as texto:
            lineas = texto.readlines()
                 
    except FileExistsError:
        print("archivo no existe")
        return []
    else:
    # Eliminar las líneas en blanco al final del archivo
        lineas.pop()  # Elimina la última línea (que suele ser vacía)
        return lineas

lineas_archivo = lector_archivo(nombre_texto)
if lineas_archivo:
    print(f"Contenido del archivo '{nombre_texto}':")
    for linea in lineas_archivo:
        print(linea.rstrip())  # Elimina los espacios en blanco al final de la línea
else:
  print("No se pudo leer el archivo.")

"""
Listas: Crea listas de diferentes tipos de datos (números, cadenas, booleanos). 
Accede a elementos de una lista por índice y modifica su contenido.
"""
lista_1 = [11,22,33,44,55,66,77,88,99]
lista_1[2] = "cambiado"
print(lista_1)
"""
Tuplas: Crea tuplas con diferentes tipos de datos. Compara dos tuplas para verificar si son iguales.
"""
tupla_1 = (20,True,"hola")
tupla_2 = (20,False,"chao")
comparacion = tupla_1 == tupla_2
print(comparacion)
"""
Diccionarios: Crea diccionarios con claves y valores de diferentes tipos. 
Accede a valores de un diccionario por clave y modifica su contenido.
"""
diccionario_1 = {"nombre":"alexander", "edad": 30}
diccionario_1["nombre"] = "chronos"
print(diccionario_1)

"""
Operaciones con listas y diccionarios: Realiza operaciones comunes con listas y diccionarios, 
como agregar, eliminar, buscar y ordenar elementos.
"""
