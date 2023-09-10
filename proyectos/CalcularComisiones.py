nombre_vendedor = input("Ingresa El nombre del Vendedor: ")
ventas_realizadas = int(input("ingresa el monto vendido en el mes: "))
comision_total = round( ventas_realizadas * 13 / 100, 2)
print(f"Hola,{nombre_vendedor} tus comisiones de este mes son: ${comision_total} pesos")
