# Este programa contiene múltiples violaciones 
# a las convenciones de nombres de variables

# Instrucciones:
#  - Analiza el programa y encuentra todas las violaciones 
#    a las convenciones de nombres de variables descritas 
#    en la lista de chequeo del capítulo 11 "The powe of 
#    variable names" del libro "Clean Code" de Robert C. Martin.
#  - Para cada violación, explica por qué el nombre no cumple
#    con la convención y propon un nombre alternativo que 
#    respete las buenas prácticas.
#  - Refactoriza el programa para corregir todas las violaciones
#    y asegúrate de que sea más legible y mantenible.

PI = 3.14159  # ¿Por qué se usa "PI" aquí? Porque es el nombre de una constante matemática.

numeros = [10, 20, 30, 40, 50]  # ¿Qué representa "g"? Se lo cambiamos a "numeros" para que sea más descriptivo.

def calculadora_media(x): # Quitamos la y que estaba aqui porque no la usa en el programa y ponemos un nombre más descriptivo para la función.
    media = sum(x) / len(x)  # ¿Qué representa "temp"? Representa la media de los números en la lista "x". Se lo cambiamos a "media" para que sea más descriptivo.
    maximo = max(x)  # ¿Qué representa "z"? Representa el valor máximo de los números en la lista "x". Se lo cambiamos a "maximo" para que sea más descriptivo.
    minimo = min(x)  # ¿Qué representa "w"? Representa el valor mínimo de los números en la lista "x". Se lo cambiamos a "minimo" para que sea más descriptivo.
    return media, maximo, minimo

color_RED = 1
color_GREEN = 2
color_BLUE = 3

# Función con un nombre que no describe su propósito, por eso la cambiamos a "mostrar_estadisticas" para que sea descriptivo.
def mostrar_estadisticas(): 
    # Uso de nombres de variables booleanas poco claros.
    mostrar_resultados = True  # ¿Qué significa "flag"? Le cambiasmos flag a "mostrar_resultados" porque flag no describe lo que hace.
    if mostrar_resultados:
        # Uso de nombres de variables que no describen su propósito
        resultados = calculadora_media(numeros)  #Representa los resultados de la función calculadora_media. Se lo cambiamos a "resultados" porque "a" no describe lo que hace.
        print("Resultados:", mostrar_resultados) 

for numero in numeros:  #Representa cada elemento de la lista "numeros". Se lo cambiamos a "numero" para que sea más facil de entender.
    print("Elemento:", numero)

# Llamada a la función principal
mostrar_estadisticas()