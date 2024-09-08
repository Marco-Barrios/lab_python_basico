"""Listas en python"""
"""Lista copy(): obtenemos todos los elementos de una lista en otra variable"""
var_1=["SQLServer", "RDS", "MYSQL", "Postgresql", "MaríaDB"]
var_2=var_1.copy()

print("El valor de mi variable 2 es {}".format(var_2))

var_2.append("SQLite3")

print("El valor actualizado de mi variable 2 es {}".format(var_2))
