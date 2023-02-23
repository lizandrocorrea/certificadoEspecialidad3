#listas  Variables multipropositos con indice 
#acciones:
#append() agregar 
#pop() eliminar
#lista{position} leer/asignar 
#len (lista) longitud o cantidad de posiciones

# calcular el promedio de 3 notas (sin usar listas)


#nota1 = 6.5
#nota2 = 4.8
#nota3 = 5.8
#promedio = (nota1 + nota2 + nota3) / 3
#print("el promedio es =", promedio)

#calcular el promedio de notas de 3 (utiizando listas)
notas = [6.5, 4.8, 5.8]
promedio = (notas[0] + notas[1] + notas[2]) /len(notas)
print("el promedio es : ", promedio)