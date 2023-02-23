# calcular el ppromedio de notas ingresadas por el usuario usuando lista 
#terminas cuando se ingrese una nota CERO

def sumar_notas(listado):
    suma = 0 #acomulador 
    for nota in listado:
        suma = suma + nota
    return suma

lista_nota = []
lista_nota.append(float(input("ingrese una nota (Cero para salir )  :")))

while (lista_nota[len(lista_nota) -1 ] > 0):
    lista_nota.append(float(input("ingrese una nota(cero para salir) : ")))
lista_nota.pop(len(lista_nota) -1  )
if (len(lista_nota) > 0):
    promedio = sumar_notas(lista_nota) / len(lista_nota)
    print("notas :", lista_nota)
    print("el promedio es : ",promedio)
