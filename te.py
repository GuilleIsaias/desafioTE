class te ():
    sabor = ["negro", "verde", "hierbas"]
    tamano = [300, 500]
    time_preparacion = [3, 5, 6]
    @staticmethod
    def t_preparacion(flavor):
        if flavor == 1:
            print("Su tiempo de preparacion es de 3 minutos")
            print("Se recomienda consumir al desayuno")
        elif flavor == 2:
            print("Su tiempo de preparacion es de 5 minutos")
            print("Se recomienda consumir al medio día")
        elif flavor == 3:
            print("Su tiempo de preparacion es de 6 minutos")
            print("Se recomienda consumir al atardecer")
        else:
            print("Ingrese una opción valida")

    @staticmethod    
    def p_te(size):
        if size == 1:
            print("El valor es $3000")
        elif size == 2:
            print("El valor es $5000")
        else:
            print("Ingrese una opción valida")
        




