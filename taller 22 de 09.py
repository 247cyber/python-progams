#################################################################################################################################
 
# Ejercicios de Python: Casos Prácticos
#taller funciones
# 1
class PropinaRestaurante:  
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def aplicar_propina(self):
        total_actual = self.total()
        if total_actual > 30000:
            return total_actual + (total_actual * 0.15) 
        return total_actual

    def total(self):
        return sum(producto['precio'] for producto in self.productos)

# Pruebas
carrito = PropinaRestaurante()
carrito.agregar_producto('hamburguesa', 20000) # Cambié los nombres por comida para que coincida con el restaurante 🍔
carrito.agregar_producto('papas', 20000)
print("Total con propina:", carrito.aplicar_propina()) # Salida correcta: 46000.0

# numero 2
def es_valida(contrasena):
    return len(contrasena) >= 8
contraseña = input("Por favor, ingrese su contraseña: ")

if es_valida(contraseña):
    print("Contraseña válida! Cumple con los 8 caracteres requeridos.")
else:
    print("Contraseña inválida. Debe tener al menos 8 caracteres.")

#numero 3 
# app de rutas
 def km_a_millas(km):
    return km * 0.621371
print ("Conversión de kilómetros a millas:")
print(km_a_millas(10))  # Salida: 6.21371

# blucles y condicionales
 #4 
precios = [45000, 120000, 8000, 300000]

print("--- Precios Finales con Descuento ---")
for precio in precios:
    if precio > 100000:
        precio_final = precio * 0.85  # Aplica el 15% de descuento (100% - 15% = 85%)
        print(f"Producto de ${precio} -> Precio final con descuento: ${precio_final:.0f}")
    else:
        print(f"Producto de ${precio} -> No aplica descuento: ${precio}")

# 5
edades = [16, 20, 15, 30, 12, 25]

print("\n--- Control de Acceso ---")
for edad in edades:
    if edad >= 18:
        print(f"Edad: {edad} -> Acceso permitido")
    else:
        print(f"Edad: {edad} -> Acceso denegado")

# 6

# 1 significa asistió, 0 significa faltó
asistencias = [1, 1, 0, 1, 0, 0, 1]
inasistencias = 0

for asistencia in asistencias:
    if asistencia == 0:
        inasistencias += 1

print("\n--- Reporte de Inasistencias ---")
print(f"Total de fallas: {inasistencias}")

if inasistencias > 2:
    print("ALERTA: El aprendiz ha faltado más de 2 veces.")

# 7 

class Cliente:
    def __init__(self, nombre, membresia_activa):
        self.nombre = nombre
        self.membresia_activa = membresia_activa  # True o False

    def puede_entrenar(self):
        if self.membresia_activa:  # Es igual a escribir: if self.membresia_activa == True
            return f"{self.nombre} tiene acceso permitido para entrenar."
        return f"{self.nombre} tiene acceso denegado. Membresía inactiva."

# Pruebas
cliente1 = Cliente("Ana", True)
cliente2 = Cliente("Luis", False)

print("\n--- Gimnasio ---")
print(cliente1.can_entrenar() if hasattr(cliente1, 'can_entrenar') else cliente1.puede_entrenar())
print(cliente2.puede_entrenar())

# 8

class CarritoCompras:
    def __init__(self):
        self.productos = []  # Lista vacía

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def total(self):
        return sum(producto['precio'] for producto in self.productos)

# Pruebas
mi_carrito = CarritoCompras()
mi_carrito.agregar_producto("Camisa", 45000)
mi_carrito.agregar_producto("Pantalón", 89000)

print("\n--- Carrito de Compras ---")
print("Total acumulado:", mi_carrito.total())


# 9 

class Vehiculo:
    def __init__(self, placa, conductor, disponible):
        self.placa = placa
        self.conductor = conductor
        self.disponible = disponible  # True o False

    def cambiar_estado(self):
        # El operador 'not' invierte el valor booleano (True pasa a False, False pasa a True)
        self.disponible = not self.disponible
        return f"El vehículo de {self.conductor} ahora está {'Disponible' if self.disponible else 'Ocupado'}."

# Pruebas
taxi = Vehiculo("XYZ-123", "Carlos", True)
print("\n--- App de Transporte ---")
print(f"Estado inicial: {taxi.disponible}")
print(taxi.cambiar_estado())
print(f"Estado final: {taxi.disponible}")

# 10 

productos = [
    {"nombre": "Camisa", "precio": 45000}, 
    {"nombre": "Pantalón", "precio": 89000}, 
    {"nombre": "Media", "precio": 8000}
]

# Estructura: [lo_que_quiero_guardar for elemento in lista if condicion]
ofertas = [prod["nombre"] for prod in productos if prod["precio"] < 50000]

print("\n--- Productos en Oferta (< 50.000) ---")
print(ofertas)  # Salida: ['Camisa', 'Media']