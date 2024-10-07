"""
La media (promedio) de un conjunto de datos se encuentra al sumar todos los números 
en el conjunto de datos y luego al dividir entre el número de valores en el conjunto.
"""
import statistics # Se puede utilizar la libreria statictis

conjunto_datos = [12,23,31,16,52,32,12,27,41,11,15,28,72,75,87,43,62,68,22,14,29] #conjunto de datos ejemplo
# Opción No 1
media = statistics.mean(conjunto_datos)
print(f"La media es: {round(media, 2)}") # con el comando "round" se limita el número de decimales a mostrar

media = sum(conjunto_datos) / len(conjunto_datos)
print(f"La media es: {round(media, 2)}")
