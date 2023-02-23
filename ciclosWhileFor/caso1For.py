#Dada la venta de una serie indetermnada de productos quee esten sin iva 
#se desea conocer 
#*** el presio total sin iva 
#*** el total del iva
#*** el presio total a pagar con  iva 
#***considerar el precio cero para el termino de ingreso de precio 


totalSinIVA = 0 #inicializacion 
cantidad_prod = int(input("cuantos productos ? : "))

for i in range(1, cantidad_prod + 1, 1):
    precioSinIVA = int(input("ingrese precio sin IVA: "))
    totalSinIVA = totalSinIVA + precioSinIVA #acomulador
totalIVA = totalSinIVA * 19 /100
totalConIVA = totalSinIVA + totalIVA  

print("total sin iva :", totalSinIVA)
print("total iva", totalIVA)
print("total con iva : ", totalConIVA)