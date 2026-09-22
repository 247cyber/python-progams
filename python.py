x = 13 
y = 40

if x > y:
    print("x es mayor que  y")
else :
    print("x es menor que y")

# numero complejos 

num_complejo = 3.2 + 7j

print(num_complejo) # muestra el mismo resultado (3.2+7j)

# notacion cientifica

num_real = 0.4e-7

print(num_real) # muestra el mismo resultado (4e-08)

# sistema binario
num_binario = 0b111
print(num_binario) # muestra el mismo resultado (7)

# sistema octal
num_octal = 0o10
print(num_octal) # muestra el mismo resultado (8)

#sistema hexadecimal
num_hexadecimal = 0xff
print(num_hexadecimal) # muestra el mismo resultado (255)

# operadores aritmetricos

a = 30 
b = 12
print("Suma: ", a + b) # Suma: 42
print("Resta: ", a - b) # Resta: 18
print("Multiplicación: ", a * b) # Multiplicación: 360
print("División: ", a / b) # División: 2.5

# división entera
print("División entera: ", a // b) # División entera: 2

# resto de una divicion
a = 15
b = 6 
print(a%b) #3
# exponenciacion 
a = 7 
b = 2 
print (a**b) #49

#expresiones
a = 12 
b = 5 
c = 6 

resultado = (a + b ) * c

print(resultado) # 102 

# valor absoluto 
valor_absoluto = abs(-47.67)
print (valor_absoluto) # 47.67

# raiz cuadrada 
# se importa la funcion de math para hayar la raiz cuadrada
import math
raiz = math.sqrt(169)
print(raiz) # 13.0 

#redondeo
redondeo = round(42.4)
print(redondeo) #40 

# cadena de texto 
cadena = "esto es una cadena de texto"
print (cadena)
#cade de texto multiple
cad_multiple = """ esto es cadena de texto tiene mas de una liena.En concreto,cuenta conb tres lieneas diferentes"""
print (cad_multiple)
# saber el numero de caracteres 
cad = "cadena de texto de ejemplo"
print(len(cad)) #26 
#funcion find
cad = "xyza"
print (cad.find("y")) #1

#remplazo de caracteres 
cad ="hola mundo"
res = cad.replace("hola","adios")
print(res) # adios mundo 
#eliminacion de espacios 
cad = " cade con espacios en blanco"
esp = cad.strip()
espi = cad.lstrip()
espd = cad.rsplit()
print(esp) #"cadena con espacios en blanco"
print(espi) #"cadena con espacios en blanco "
print(espd) #" cadena con espacios en blanco" 

#metodos upperd y lower 
cad = "cadena de texto"
may = cad.upper()
min = cad.lower()

print(may) # CADENA DE TEXTO"
print(min) # cadena de texto"

#metodo capitalize 
cad = "un ejemplo"
texto = cad.capitalize()

print (texto) #"Un ejemplo"

# dividir una cadena de texto
cad = "primero ;segundo;tercero valor"
print(cad.split(";")) #"primero " ;"segundo";"tercero valor"

#concatenacion
cad_concat = "hola" + "mundo"
print (cad_concat) # "hola mundo"

# el metodo format
cad2 = "mundo"
cad3 = "cadena"
print("hola" + cad2 + "otra" + cad3)
print("hola {0}, otra {1}".format(cad2,cad3)) # "hola mundo otra cadena"   
print ("hola {texto1}, otra {texto2}".format(texto1=cad2,texto2=cad3)) # "hola mundo otra cadena"
#concatenacion texto y numero 
num = 3
print ("numero: " + str(num)) # numero:3 

#operador * aplicado al string
print ("hola mundo" *4)
#operador in 
cad = "Nueva cadena de texto"
res = "x" in cad
print(res) #true 

# aceder a una caracter de una cadena de texto
cad = "cadena de texto"
print(cad[0]) # c
print(cad[5]) # a

# subcadenas
cad = "cadena de texto"
print(cad[0:6]) # cadena
print(cad[8:13]) # texto

# obtener subcadena desde un caracter hasta el final
cad = "cadena de texto"
print(cad[-3]) # t
print(cad[5:]) # texto