# ejercicio numero 1
x = 10 
y = 5
if x > y:
    print("x es mayor que y")

# ejercicio numero 2
num1= int(input("Ingrese un número: ")) # utilizamos la funcion input para que el usuario ingrese un numero y lo convertimos a entero con int()
num2= int(input("Ingrese otro número: "))
num3= int(input("Ingrese un tercer número: "))

mayor = num1 # asuminos que el primer número es el mayor

if num2 > mayor: # miramos si el segundo número es mayor que el primero
    mayor = num2

if num3 > mayor: # miramos si el tercer número es mayor que el primero y el segundo
    mayor = num3

print("El número mayor es:", mayor) # imprimimos el número mayor

# ejercicio numero 3

numero = int(input("Introduce un número entero: "))

# Evaluamos si el residuo de dividir el número entre 2 es cero
if numero % 2 == 0:
    print(f"El número {numero} es PAR.") # si el numero es par, imprimimos que es par
else:
    print(f"El número {numero} es IMPAR.") # si el numero es impar, imprimimos que es impar


# ejercicio numero 4
# le pedimos al usuario que ingrese su nota
nota = int(input("Introduce tu nota (0-100): "))
# con el ciclo if else evaluamos si la nota es mayor o igual a 100,
if nota >= 100:
    print("Tu calificación es alta")

else:
    print("Tu calificación es baja")

# ejercicio numero 5

angulo = int(input("Introduce un ángulo en grados: "))

if angulo == 90:
    print("El ángulo es RECTO.")

elif angulo > 90:
    print("El ángulo es OBTUSO.")

else:
    print("El ángulo es AGUDO.")

# ejercicio numero 6 

suma = 0

for numero in range(1, 100): # utilizamos el ciclo for para recorrer los numeros del 1 al 100
    suma += numero # sumamos los numeros del 1 al 100

print(f"La suma de los números del 1 al 10 es: {suma}")

# ejercicio numero 7
for i in range(1, 21):
    cuadrado = i ** 2
    print(f"El cuadrado de {i} es {cuadrado}")

# ejercicio numero 8

for i in range(1, 31):
    resultado = 4 ** i
    print(f"4 elevado a {i} es: {resultado}")

# ejercicio numero 9
suma = 0
for i in range(2, 61, 2):
    suma += i

print(f"La suma de los 30 primeros números pares es: {suma}")

# ejercicio numero 10
limite = int(input("Ingrese el valor límite: "))

print("Salida:", end=" ")
for i in range(5, limite, 5):
    print(i, end=" ")
print()  # Salto de línea al final

# ejercicio numero 11

for i in range(2, 21, 2):
    cubo = i ** 3
    print(f"{i} {cubo}")
