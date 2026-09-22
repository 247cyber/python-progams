def cal_propinas (v_cuenta,p_propina=10):
    return v_cuenta * (p_propina/100)

print(cal_propinas(180000))

# parqueadero 

def calcular_costo_parqueadero(horas, tarifa_por_hora=2000):
    if horas > 8 :
        return 10000
    return horas * tarifa_por_hora
print(calcular_costo_parqueadero(4))  # Salida: 8000
print(calcular_costo_parqueadero(10))  # Salida: 10000

# si gana o no la medalla 

def puntaje_nota (nota):
    if nota >= 4.5:
        return "Medalla de Oro"
    elif nota >= 4.0:
        return "Medalla de Plata"
    elif nota >= 3.0:
        return "Medalla de Bronce"
    else:
        return "No gana medalla"
print(puntaje_nota(2.0))  

# carrito compras 

class carrito_compras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})
    
    def total (self):
        return sum(producto['precio'] for producto in self.productos)

carrito = carrito_compras()
carrito.agregar_producto('camisa', 10000)
carrito.agregar_producto('pantalon', 20000)
print("Total de la compra:", carrito.total())

# descuento de carrito 
class Carrito_descuento:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append({'nombre': nombre, 'precio': precio})

    def aplicar_descuento(self):
        total_actual = self.total()
        if total_actual > 30000:
            return total_actual * 0.85
        return total_actual

    def envio_gratis(self):
        ciudad = str(input("Ingrese la ciudad de envío: "))
        if ciudad == "popayán" :
            return 0
        return 15000

    def total(self):
        return sum(producto['precio'] for producto in self.productos)

# Pruebas
carrito = Carrito_descuento()
carrito.agregar_producto('camisa', 20000)
carrito.agregar_producto('pantalon', 20000)
print("Total con descuento:", carrito.aplicar_descuento()) 
print("Envío gratis:", carrito.envio_gratis())
