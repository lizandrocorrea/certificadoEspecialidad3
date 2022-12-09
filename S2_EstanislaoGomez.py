##Se necesita un programa que pida al usuario su nombre y su edad.
##La respuesta que se espera obtener es la cantidad de años que tendrá el usuario dentro de una década.
##La salida para el usuario debe tener el siguiente aspecto:
##Estimado Juan, en una década su edad será de 34 años.
##En este ejemplo se está considerando que Juan es el nombre introducido por el usuario y que tiene 24 años
##al momento de probar nuestro programa.
##Debe crear una función (por medio de la instrucción def) que sea capaz de realizar el cálculo de la edad
##futura, utilizando operadores aritméticos y retornando el resultado




# variables 

def cal (e, d):
    result = e + d
    return result

nonbre = str(input("profavor ingresa un tu nombre :", ))
edad = int(input("por ingrese tu edad :", ))
dec = 10
#proceso 

calculo = cal(edad,dec)

#salida 

print("Estimado usuario ", nonbre, "la edad que tendra en una decada  ",calculo,  "años de edada")