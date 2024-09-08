"""Listas en python"""
"""Lista count(): cantidad de veces que aparece el elemento que se repite en la lista"""
var_1=["Python","Java","PHP","Javascript","TypeScript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("python")
var_1.append("Python")
var_1.append("NodeJS")

print("Mi lista actualizada es {}".format(var_1))

print("La cantidad de veces que se repite Python es {}".format(var_1.count("Python")))

