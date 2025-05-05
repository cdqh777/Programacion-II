class Teleferico:
    def __init__(self, color, tramo, nroCabinas, nroEmpleados=0):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = nroEmpleados
        self.empleados = []
        self.edades = []
        self.sueldos = []
    
    def agregar_empleado(self, nombre, apellido_paterno, apellido_materno, edad, sueldo):
        if self.nroEmpleados < 100:
            self.empleados.append([nombre, apellido_paterno, apellido_materno])
            self.edades.append(edad)
            self.sueldos.append(sueldo)
            self.nroEmpleados += 1
        else:
            print("No se pueden agregar más empleados, capacidad llena.")
    
    def eliminar_por_apellido(self, apellido_x):
        indices_a_eliminar = []
        for i in range(self.nroEmpleados):
            if self.empleados[i][1] == apellido_x or self.empleados[i][2] == apellido_x:
                indices_a_eliminar.append(i)
        
        for i in sorted(indices_a_eliminar, reverse=True):
            del self.empleados[i]
            del self.edades[i]
            del self.sueldos[i]
            self.nroEmpleados -= 1
    
    def __add__(self, otro_teleferico):
        if self.nroEmpleados > 0 and otro_teleferico.nroEmpleados < 100:
            empleado = self.empleados[-1]
            edad = self.edades[-1]
            sueldo = self.sueldos[-1]
            
            otro_teleferico.agregar_empleado(empleado[0], empleado[1], empleado[2], edad, sueldo)
            
            del self.empleados[-1]
            del self.edades[-1]
            del self.sueldos[-1]
            self.nroEmpleados -= 1
        return self
    
    def mostrar_mayor_edad(self):
        if self.nroEmpleados == 0:
            print("No hay empleados.")
            return
        
        max_edad = max(self.edades)
        print("Empleados con la mayor edad ({}) años:".format(max_edad))
        for i in range(self.nroEmpleados):
            if self.edades[i] == max_edad:
                print("- {} {} {}".format(*self.empleados[i]))
    
    def mostrar_menor_edad(self):
        if self.nroEmpleados == 0:
            print("No hay empleados.")
            return
        
        min_edad = min(self.edades)
        print("Empleados con la menor edad ({}) años:".format(min_edad))
        for i in range(self.nroEmpleados):
            if self.edades[i] == min_edad:
                print("- {} {} {}".format(*self.empleados[i]))
    
    def mostrar_mayor_sueldo(self):
        if self.nroEmpleados == 0:
            print("No hay empleados.")
            return
        
        max_sueldo = max(self.sueldos)
        print("Empleados con el mayor sueldo (${}):".format(max_sueldo))
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == max_sueldo:
                print("- {} {} {}".format(*self.empleados[i]))
    
    def mostrar_menor_sueldo(self):
        if self.nroEmpleados == 0:
            print("No hay empleados.")
            return
        
        min_sueldo = min(self.sueldos)
        print("Empleados con el menor sueldo (${}):".format(min_sueldo))
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == min_sueldo:
                print("- {} {} {}".format(*self.empleados[i]))

teleferico1 = Teleferico("Rojo", "Estación Central, Estación Cementerio, Estación 16 de julio", 20)
teleferico1.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500)
teleferico1.agregar_empleado("Lucy", "Sosa", "Ríos", 28, 2300)
teleferico1.agregar_empleado("Ana", "Perez", "Rojas", 42, 2800)
teleferico1.agregar_empleado("Saul", "Arce", "Calle", 39, 2600)

teleferico2 = Teleferico("Azul", "Estación Extranca, Estación UPEA, Estación 16 de julio", 15)
teleferico2.agregar_empleado("Juan", "Mendez", "Garcia", 45, 3000)
teleferico2.agregar_empleado("Maria", "Lopez", "Vargas", 31, 2700)

print("\nEmpleados con menor edad en teleférico 1:")
teleferico1.mostrar_menor_edad()

print("\nEmpleados con menor sueldo en teleférico 2:")
teleferico2.mostrar_menor_sueldo()