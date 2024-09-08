sueldo=int(input("Ingrese su sueldo: "))

if sueldo>3500:
    print("Su sueldo no tiene bonificación")
else:
    sueldo_final = 1.2 * sueldo
    print("Su sueldo tiene bonificación este año y será de: {}".format(sueldo_final))
