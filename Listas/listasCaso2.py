# calcular el ppromedio de notas ingresadas por el usuario (sin usar lista )
#terminas cuando se ingrese una nota CERO

sumatoria_notas = 0 #acomulador
cantidad_notas = 0 #acomulador 
nota = float(input("ingrse una nota (CERO para salir) :")) 
while (nota > 0):
    sumatoria_notas = sumatoria_notas + nota #acomulador
    cantidad_notas = cantidad_notas + 1 # conteo
    nota = float(input("ingrese una nota (CERO para salir ) :"))
if (cantidad_notas > 0):
        promedio = sumatoria_notas / cantidad_notas
        print("el promedio es  :",promedio)