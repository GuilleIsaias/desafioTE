class te ():
    sabor = ["negro", "verde", "hierbas"]
    tamano = [300, 500]
    time_preparacion = [3, 5, 6]
    @staticmethod
    def t_preparacion(flavor):
        while True:
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
                flavor = int(input("Ingrese el Té que desea ordenar: \n1)Té Negro \n2)Té Verde \n3)Infusión de Hierbas\n"))
            break
        
    @staticmethod    
    def p_te(size):
        while True:
            if size == 1:
                print("El valor es $3000")
            elif size == 2:
                print("El valor es $5000")
            else:
                print("Ingrese una opción valida")
                size = int(input("Ingrese el tamaño que desea: \n1) Pequeño (300gr)\n2) Grande (500gr)\n"))
            break




