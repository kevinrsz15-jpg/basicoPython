#Loop

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:", i)
    
resultado = 0
for i in mi_lista:
    resultado += i

print(f"El resultado de la suma de mi lista es: {resultado}")

for i in range(2,9):
    print(i)

mi_lista_2 = ["Lunes", "Martes","Miercoles", "Jueves", "Viernes"]

for i in mi_lista_2:
    if i !="Lunes":
        print(f"Feliz{i}!")

# While loop
i = 0

while 1 < 5:
    i += 1
    if i ==3:
       continue
    print(i)
    if i ==4:
        break

else:
    print("i es ahora mayor o igual a 5")

#Prectica 2
# Dada la lista mi_lista2 = ["lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#Imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
#Pista: Usa los dos tipos de loop while y for en el mismo programa para lograrlo
#Resultado: 
#martes
#miercoles
#jueves
#Viernes
#martes
#miercoles
#jueves
#Viernes
#martes
#miercoles
#jueves
#
print("=====RESULTADO DE INTENTO====")
veces = 3
limite = 4
mi_lista_2 = ["Lunes", "Martes","Miercoles", "Jueves", "Viernes"]
for veces in mi_lista_2:
     if i !="Lunes":
        print(f"Feliz{i}!")
        break

print("Ya se a generado")