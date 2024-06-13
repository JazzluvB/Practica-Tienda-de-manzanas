print("******************************************************")
print("******************** Bienvenido a ********************")
print("******************** Apple Shop S ********************")
print("******************************************************")


num_manzanar = 11
num_manzanaa = 6
num_manzanav = 15

manzanas_totales = num_manzanar + num_manzanaa + num_manzanav


print("Por favor ingresa tu nombre")
nombre = input()
print("Por favor escribe tu apellido")
apellido = input()

#Solicitar al cliente la cantidad de manzanas que desea comprar
cantidad_manzanas = int("¿Cuantas manzanas desea comprar?")
input()

#Definir el costo por manzana
costo_por_manzana = 5

#Calcular el total
total = costo_por_manzana * cantidad_manzanas


print("Muy bien, enseguida le entregamos")
print("El total a pagar es: $" + str(total))

#Concatenacion
nombre_completo = nombre + " " + apellido

print("Gracias por preferirnos,", nombre_completo)

print("Actualmente contamos con:")
print("Manzanas Rojas", num_manzanar, "Manzanas Amarillas", num_manzanaa, "Manzanas Verdes", num_manzanav )
print("En total tenemos", manzanas_totales, "Manzanas")