# vamos a hacer un programa que nos diga si somos mayores de edad o no con la sentencia if else

edads = int(input("ingrese su edad : "))

if edads >= 18:
    print(" usted es mayor de edad ")

else : 
    print("usted es menor de edad ")

# ahora vamos a hacer un programa que nos diga si somos mayores de edad o no con la sentencia if else y elif

edad = int(input("ingrese su edad : "))

if edad >= 18:
    print(" usted es mayor de edad ")

elif edad == 17:
    print(" casi eres mayor de edad ")    

elif edad == 10:
    print(" usted es un niño ")

else : 
    print("usted es menor de edad ")

# ahora vamos a utiliar el metodo for o ciclo for para hacer un programa que nos diga los numeros del 1 al 10
for i in range(1, 11):
    print(i) # nos va a imprimir los numeros del 1 al 10

# ahora vamos a utiliar el metodo while o ciclo while para hacer un programa que nos diga los numeros del 1 al 10
x = 0
y = 3
while x < y:
    print(x)
    x += 1 # nos va a imprimir los numeros del 0 al 2

# ahora vamos a utilizar el metodo break
x = 0
y = 3

while x < y:
    print(x)
    x += 1
    if x == 2:
        break
    else:
        print("condicional") # nos va a imprimir los numeros del 1 al 4

# ahora vamos a utilizar el metodo continue
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i) # nos va a imprimir los numeros del 1 al 10 pero sin el 5