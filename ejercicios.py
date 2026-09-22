# EJERCICO 1 
# Valores iniciales
a = 1
b = 2
c = 3
# Operaciones de suma
a = a + 2
b = a + 2 + b
c = a + 2 + c
# Operaciones de división
a = a / 2
b = b / 2
c = c / 2
# Mostrar los valores finales
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# EJERCICIO 2
# Valores iniciales
a = 2
b = 4
c = 6
# Operación de multiplicación
x = a * b * c
# Mostrar el resultado
print(f"El valor de x es: {x}")
 
 # EJERCICIO 3
 # Valor inicial
a = 2
# Expresión algebraica traducida
x = 4 * (a ** 2) - 2 * a + 7
# Mostrar el resultado
print(f"El valor de x es: {x}")

# EJERCICIO 4
# Valores iniciales
a = 2 
b = 4 
c = 6
d = 8
# Operaciion 
x = (c - a) ** 2 + (d - b)
# Mostrar el resultado
print(f"El valor de x es: {x}")
#EJERCICIO 5
# importar la biblioteca math para funciones matemáticas
import math
# Valor inicial
r = 2
# Cálculo usando math.sqrt para la raíz cuadrada
x = math.sqrt(4 / 3)
# Mostrar el resultado
print(f"El valor de x con raíz es: {x}")

 # EJERCICIO 6
 # Valores iniciales
a = 2
b = 6
# Expresión algebraica traducida
x = (a + b) / a - (3 * a) / 5
# Mostrar el resultado
print(f"El valor de x es: {x}")

# EJERCICIO 7
import math
# Valores iniciales
a = 2
b = 4
c = 1
# Cálculo del discriminante (lo que va dentro de la raíz)
discriminante = (b ** 2) - (4 * a * c)
# Cálculo de las dos soluciones (una con + y otra con -)
x1 = (-b + math.sqrt(discriminante)) / (2 * a)
x2 = (-b - math.sqrt(discriminante)) / (2 * a)
# Mostrar los resultados
print(f"El valor de x1 es: {x1}")
print(f"El valor de x2 es: {x2}")

# EJERCICO 8 
# valor inicial 
a = 2
b = 4
c = 6
d = 8 
#(Numerador de la gran fracción)
numerador_grande = a + ((a + b) / (c + d))
#(Denominador de la gran fracción)
denominador_grande = a + (a / b)
# Ecuación final
x = a + (numerador_grande / denominador_grande)
# Mostrar el resultado
print(f"El valor de x es: {x}")

#EJERCICIO 9
# Valores iniciales
# Valores iniciales
a = 2
b = 4
c = 6
# Nivel 1: La fracción del fondo del todo
nivel1 = b / (c + a)
# Nivel 2: La suma del fondo
nivel2 = a + nivel1
# Nivel 3: La fracción que divide a esa suma
nivel3 = b / (c * nivel2)
# Nivel 4: El denominador de la fracción principal
denominador_principal = a + b + nivel3
# Ecuación final para x
x = a + (b / denominador_principal)
# Mostrar el resultado
print(f"El valor de x es: {x}")

# EJERCICIO 10
# Valores iniciales vistos en clase
a = 2
b = 4
c = 6
d = 8
# Ecuación en una sola línea respetando la jerarquía de operaciones
x = a + b + (c / (d + (a / ((b - c) / (a / (b + c))))))
# Mostrar el resultado final
print(f"El valor de x es: {x}")


