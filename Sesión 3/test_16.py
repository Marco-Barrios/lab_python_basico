"""Diccionarios en Python"""

var_1={"nombre": "Mysql", "tipo":"BD Relacional"}

"""Convirtiendo un diccionario en una lista"""

var_2=list(var_1)
print("Mi diccionario convertido en lista es {}".format(var_2))

keys = list(var_1.keys())
print(keys)

var_3=list(var_1.items())
print(var_3)