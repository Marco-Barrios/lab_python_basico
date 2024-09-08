"""Listas en python"""
""" del lista[]: elimina un valor indicando el índice del valor de la lista"""
paises=[]
paises.append("Perú")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Canadá")
paises.append("España")
paises.append("Colombia")
print("Mi lista es {}".format(paises))

del paises[2]
print("Mi lista actualizada es {}".format(paises))

