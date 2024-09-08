"""Listas en Python"""
var_1=[]
var_2=[]
var_1.append("Marco")
var_1.append(24)
var_1.append("Ing. Sistemas")
var_2.append("Antonio")
var_2.append(30)
var_2.append("Arquitecto")

suma_edades = var_1[1]+var_2[1]
print("La suma de las edades es {}".format(suma_edades))
suma_listas = var_1+var_2
print("La suma de las listas es {}".format(suma_listas))
suma_listas.reverse()
print("La lista invertida es {}".format(suma_listas))
del var_1[1]
del var_2[1]
suma_listas2 = var_1+var_2
print("La nueva lista es {}".format(suma_listas2))

