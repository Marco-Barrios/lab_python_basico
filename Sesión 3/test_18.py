"""Asignación múltiple"""
"""Referencia a 2 o más variables con sus respectivos datos"""
var1=input("Ingrese su nombre de usuario: ")
var2=input("Ingrese su nombre: ")
var3=input("Ingrese su edad: ")

#usuario=var1
#nombre=var2
#edad=var3

usuario, nombre, edad = var1, var2, var3
print("Su nombre de usuario es {} y tiene {} años".format(usuario, edad))
