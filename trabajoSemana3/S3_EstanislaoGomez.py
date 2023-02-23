#Se necesita un programa que sea capaz de calcular los descuentos en el área de ventas de
#una empresa de retail.
#Un usuario deberá cargar los precios de los productos en el programa, la cantidad de precios
#que cargará es indeterminada. Por lo tanto, se ha decidido que la carga finalizará al ingresar
#el precio CERO.
#Una vez que se cuente con el total de la operación de venta, se podrán aplicar descuentos
#dependiendo del monto alcanzado:

#Si el monto de la sumatoria de los precios es inferior a $ 50.000, entonces el descuento será del
#7% sobre el total.
#Si el monto de la sumatoria de los precios alcanza o sobrepasa los $ 50.000, entonces el
#descuento aplicado debe ser del 12%.
#La salida que se espera por pantalla corresponde a:
#• La sumatoria de todos los precios ingresados (total de la venta sin descuentos)
#• El monto de descuento logrado.
#• El monto a pagar (con los descuentos aplicados)


valorProducto = 0 #inicializacion 
precioTotal = int(input("ingrese monto de venta  (CERO para salir): "))
condicion = 1


while (precioTotal !=0):
    valorProducto = valorProducto + precioTotal #acomulador 
    precioTotal = int(input("ingrese monto de venta  (CERO para salir): "))

if (valorProducto <= 5000):
        descuento7 = valorProducto / 100 * 7
        pagoTotal = valorProducto - descuento7
        print("total de la venta sin descuentos  :", valorProducto)
        print("descuento del 7% : ", descuento7)
        print("total a pagar : ", pagoTotal)
else:
        descuento12 = valorProducto / 100 * 12
        pagoTotal = valorProducto - descuento12
        print("total de la venta sin descuentos  :",valorProducto)
        print("descuento del 12% : ", descuento12)
        print("total a pagar : ", pagoTotal)



print("hasta luego")


