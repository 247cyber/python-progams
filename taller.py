#TUPLAS EJERCICIOS

# ejercicio 1 
# Creación de la tupla con las coordenadas GPS de Popayán
coordenadas_popayan = (2.4419, -76.6063)

# Imprimir cada valor por separado usando sus índices
print("Latitud:", coordenadas_popayan[0])
print("Longitud:", coordenadas_popayan[1])

#ejercico 2
# Creación de la tupla del estudiante (nombre, edad, curso)
# estudiante = ("Eduardo", 21, "Matemáticas")

# Intento de modificar el curso (cambiarlo a "Programación")
# Al ejecutar la línea de abajo, el programa fallará inmediatamente
# estudiante[2] = "Programación"
# print(estudiante)  
# Esto no se ejecutará debido al error anterior
# El error TypeError: 'tuple' object does not support item assignment (el objeto tipo tupla no soporta la asignación de elementos) ocurre por la naturaleza misma de las tuplas:Inmut

#EJERCICIO 3

dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
print(dias[2])  # miercoles

#LISTAS 
#ejercicio 1
notas = [2.0, 2.5, 3.0, 5.0, 4.0]
notas.append(4.5) # agrega un elemento al final de la lista
notas.remove(2.0) # elimina un elemento de la lista

print("La lista de notas : ", notas) # La lista de notas es:  [2.5, 3.0, 5.0, 4.0, 4.5]

#ejercicio 2

asistencias = [1, 1, 0, 1, 1, 0, 1]

contador_asistencias = 0

for registro in asistencias:
    if registro == 1:
        contador_asistencias = contador_asistencias + 1  # También se puede escribir: contador_asistencias += 1

# . Mostramos el resultado final
print("El estudiante asistió ", contador_asistencias, "dias a clases.")

#ejercicio 3

estudiantes = ["carlos", "ana", "jose", "maria", "pedro", "laura"]

ordenador = sorted(estudiantes) # ordena la lista alfabéticamente
print("Lista de estudiantes ordenada alfabéticamente: ", ordenador) # Lista de estudiantes

# ejercicio 4

precios = [15000, 20000, 25000, 30000, 35000]

suma_manual = 0
cantidad = 0 

for precio in precios:
    suma_manual += precio  # Suma el precio actual al total acumulado
    cantidad += 1        # Cuenta un elemento más (hace lo mismo que len())

#Calculamos el promedio
promedio = suma_manual / cantidad

print("El promedio de los precios es: ", promedio) # El promedio de los precios es:  25000

#ejercicio 5

edades = [15, 22, 17, 30, 16, 25]

# Creamos las dos listas vacías donde guardaremos los resultados
mayores_edad = []
menores_edad = []

# recorremos la lista original elemento por elemento
for edad in edades:
    if edad >= 18:
        mayores_edad.append(edad)  # Agrega a la lista de mayores si tiene 18 o más
    else:
        menores_edad.append(edad)  # Agrega a la lista de menores en caso contrario

# Imprimimos los resultados finales
print("Mayores de edad:", mayores_edad)  # Imprime: [22, 30, 25]
print("Menores de edad:", menores_edad)  # Imprime: [15, 17, 16]

# DICIONARIOS 

# ejercicio 1
producto = {
    "nombre": "Camiseta",
    "talla": "M",
    "color": "Azul",
    "precio": 25.99,
    "cantidad stock": 10
}

# 1. Simulamos la venta de un producto (restamos 1 al stock)
venta_producto = 1
producto["cantidad stock"] -= venta_producto  # Ahora el stock baja a 9

# 2. Imprimimos el producto recorriendo sus claves y valores correctamente
print(f"\n--- Producto: {producto['nombre']} ---")
for clave, valor in producto.items():
    print(clave, ":", valor)
