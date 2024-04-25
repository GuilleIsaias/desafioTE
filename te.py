class te ():
    sabor = ["negro", "verde", "hierbas"]
    tamano = [300, 500]
    time_preparacion = [3, 5, 6]
    @staticmethod
    def t_preparacion(flavor):
        while True:
            if flavor == 1:
                t_preparacion = 3
            elif flavor == 2:
                t_preparacion = 5
            elif flavor == 3:
                t_preparacion = 6
            else:
                print("Ingrese una opción valida")
                input("Ingrese el Té que desea ordenar: \n1)Té Negro \n2)Té Verde \n3)Infusión de Hierbas\n")
            return flavor, t_preparacion
            
    @staticmethod    
    def p_te(size):
        while True:
            if size == 1:
                size = 300
                price = 3000
            elif size == 2:
                size  = 500
                price = 5000
            else:
                print("Ingrese una opción valida")
                size = int(input("Ingrese el tamaño que desea: \n1) Pequeño (300gr)\n2) Grande (500gr)\n"))
            return size, price
            




