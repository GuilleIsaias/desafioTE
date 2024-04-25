from te import te

t_sabor = te.sabor
size_te = te.tamano

print(f'{type(t_sabor)}, {type(size_te)}')

if type(t_sabor) == type(size_te):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")




