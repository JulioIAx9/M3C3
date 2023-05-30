nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Julito el Hermoso",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]
# Imprimir la lista original sin modificaciones
print("Lista completa de nombres:")
for nombre in nombres:
    print(nombre)

# Vamos a crear las listas de magos y científicos
magos = ["Harry Houdini", "David Blaine", "Teller", "Julito el Hermoso"] # Lo de julito fue para probar el string y me gusto XD, se puede omitir
cientificos = ["Newton", "Hawking", "Einstein"]

# Creación la lista "otros" con los nombres que no son magos ni científicos
# otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]  Es una buena alternativa pero un poco enredada, mejor esta esta otra 
otros = list(set(nombres) - set(magos) - set(cientificos)) # se entiende mejor y me ahorro codigo!!

# Modificamos directamente la lista de magos añadiendo la frase "El gran"
for i in range(len(nombres)):
    if nombres[i] in magos:
        nombres[i] = "El gran " + nombres[i]

# Continuar con Imprimir cada una de las listas requeridas faltantes

# print("Lista completa de nombres:") ( preferí subirla e imprimirla antes de la modificacion de la lista, economía es riqueza)
# for nombre in nombres:
#    print(nombre)

print("\nNombres de los magos grandiosos:")
for mago in magos:
    print("El gran " + mago)

print("\nNombres de los científicos:")
for cientifico in cientificos:
    print(cientifico)

print("\nLista de otros nombres:")
for otro in otros:
    print(otro)
