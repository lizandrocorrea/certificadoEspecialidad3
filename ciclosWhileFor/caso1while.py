#Dada la venta de una serie indetermnada de productos quee esten sin iva 
#se desea conocer 
#*** el presio total sin iva 
#*** el total del iva
#*** el presio total a pagar con  iva 
#***considerar el precio cero para el termino de ingreso de precio 


totalSinIVA = 0 #inicializacion 
precioSinIVA = int(input("ingrese precio sin iva (Cero para salir) : "))
while (precioSinIVA !=0):
    totalSinIVA = totalSinIVA + precioSinIVA #acomulador 
    precioSinIVA = int(input("ingrese precio sin IVA (CERO para salir): "))
totalIVA = totalSinIVA * 19 /100
totalConIVA = totalSinIVA + totalIVA  

print("total sin iva :", totalSinIVA)
print("total iva", totalIVA)
print("total con iva : ", totalConIVA)