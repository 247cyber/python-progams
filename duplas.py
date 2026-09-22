# tuplas 
punto = (2,4,6)
print(punto[0]) # 2

# listas 
frutas = ["manzana", "banana", "cereza"]
frutas.append("durazno") # agrega un elemento al final de la lista
frutas[0] = "kiwi" # modifica un elemento de la lista
frutas.remove("banana") # elimina un elemento de la lista
print(frutas) # ['kiwi', 'cereza', 'durazno']

# taller de prueba 
temperaturas = [20, 25, 30, 35, 40,]
temperaturas.append(45) # agrega un elemento al final de la lista
temperaturas[2] = 15 # modifica un elemento de la lista
temperaturas.remove(35) # elimina un elemento de la lista

promedio = sum(temperaturas) / len(temperaturas) # calcula el promedio de las temperaturas
maximo = max(temperaturas) # obtiene el valor máximo de las temperaturas
minimo = min(temperaturas) # obtiene el valor mínimo de las temperaturas
print("El promedio de las temperaturas es: ", promedio) # El promedio de las temperaturas es
print("El valor máximo de las temperaturas es: ", maximo) # El valor máximo de las temperaturas es
print("El valor mínimo de las temperaturas es: ", minimo) # El valor mínimo de las temperaturas es  



 # DICCIONARIOS

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
 }
persona["edad"] = 31 # modifica un elemento del diccionario
persona["pais"] = "España" # agrega un elemento al diccionario          
print(persona["nombre"]) # Juan
print(persona["edad"]) # 30
print(persona["ciudad"]) # Madrid
print(persona["pais"]) # España

# taller de prueba
# Fíjate en el corchete '[' al inicio y las comas ',' entre cada diccionario
estudiantes = [
    {
        "nombre": "Ana",
        "edad": 20,
        "nota": 8.5,
        "curso": "Matemáticas",
        "aprobado": True
    }, # <-- Coma importante
    {
        "nombre": "carlos",
        "edad": 20,
        "nota": 7.0,
        "curso": "Matemáticas",
        "aprobado": False
    }, # <-- Coma importante
    {
        "nombre": "jose",
        "edad": 20,
        "nota": 5.0,
        "curso": "Matemáticas",
        "aprobado": True
    }
] # <-- Corchete de cierre importante

# Ahora sí puedes acceder por número de posición (índice)
estudiantes[0]["edad"] = 21       # Modifica la edad de Ana (posición 0)
estudiantes[0]["nota"] = 9.0       # Modifica la nota de Ana (posición 0)
estudiantes[1]["nota"] = 9.5       # Modifica la nota de carlos (posición 1) sin errores

# Para imprimir todos los estudiantes de la lista:
for estudiante in estudiantes:
    print(f"\n--- Estudiante: {estudiante['nombre']} ---")
    for clave, valor in estudiante.items():
        print(clave, ":", valor)
