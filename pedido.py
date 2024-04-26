from te import te #importamos clase 

#definimos variables
sabor_te = 0
formato_te = 0
recomendacion = ""
precio_te = 0
tiempo_p = 0

#utilizamos las funciones creadas en la clase te 
print("Bienvenido, por favor ingrese su orden:")
sabor_te, tiempo_p = te.t_preparacion(int(input("Ingrese el Té que desea ordenar: \n1)Té Negro \n2)Té Verde \n3)Infusión de Hierbas\n")))
formato_te, precio_te = te.p_te(int(input("Ingrese el tamaño que desea: \n1) Pequeño (300gr)\n2) Grande (500gr)\n")))

# definimos valores finales de variables
if sabor_te ==1:
    sabor_text = "Té negro"
    recomendacion = "Consumir al desayuno"
elif sabor_te ==2:
    sabor_text = "Té Verde"
    recomendacion = "Consumir al medio día"
else:
    sabor_text = "Infusión de hierbas"
    recomendacion = "Consumir al atardecer"


#print final
print(f'El sabor del té es {sabor_text}')
print(f'El formato del té es {formato_te}gr')
print(f'El precio es {precio_te}')
print(f'El tiempo de preparacion es {tiempo_p} minutos')
print(f'{recomendacion}')

