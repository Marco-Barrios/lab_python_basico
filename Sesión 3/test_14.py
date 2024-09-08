"""Diccionarios en Python"""
"""del: elimina una key y su valor del diccionario"""
var_1={"nombre":"Matias", "edad":26, "promedio":14}
print("El diccionario es {}".format(var_1))
var_1["distrito"]="Lince"
del var_1["edad"]
del var_1["promedio"]

print("El diccionario actualizado es {}".format(var_1))