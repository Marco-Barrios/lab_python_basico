var1=input("Ingrese su nombre y apellido: ")
var2=input("Ingrese su distrito de residencia: ")
var3=input("Ingrese su sueldo: ")

nombre, distrito, sueldo = var1, var2, var3

bono_final= int(sueldo)*3 + 0.1*int(sueldo)

diccionario1={}
diccionario1["nombre"]=nombre
diccionario1["distrito"]=distrito
diccionario1["sueldo"]=sueldo
diccionario1["bono final"]=bono_final

print("Sus datos correspondientes son: {}".format(diccionario1))
