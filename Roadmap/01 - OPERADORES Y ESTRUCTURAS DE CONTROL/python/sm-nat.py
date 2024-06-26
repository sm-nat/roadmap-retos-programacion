# OPERADORES ARITMETICOS

suma = 2 + 2
print(suma)

resta = 5 - 2
print(resta)

multiplicacion = 5 * 5
print(multiplicacion)

division = 10 / 2
print(division)

division_entera = 32 // 4 # devuelve el numero entero del cociente
print(division_entera)

modulo = 5 % 3 # Devuelve el resto de la división del primer operando por el segundo
print(modulo)

exponencial = 5 ** 2
print(exponencial)

#OPERADORES DE COMPARACIÓN

x = 5
y = 10

#igual
print(x == y) #falso
print(x == 5) #verdadero

#distinto
print(x != y) #verdadero
print(x != 5) #falso

#mayor que
print(x > y) #falso
print(x > 4) #verdadero

#menor que
print(x < y) #verdadero
print(x < 4) #falso

#mayor o igual que
print(x >= y) #falso
print(x >= 4) #verdadero, es mayor

#menor o igual
print(x <= y) #verdadero, es menor
print(x <= 4) #falso, es mayor

#OPERADORES DE ASIGNACIÓN

#asiganción
n = 33 
print(n)

#asignacion suma
n += 5 
print(n) 

#asignacion resta
n -= 5
print(n) 

#asignacion multiplicacion
n *= 5
print(n)

#asignacion division
n /= 5
print(n)

#asignacion division entera
n //= 5
print(n)

#asignacion exponencial
n **= 5
print(n)

#asignacion modulo
n %= 5
print(n)

#OPERADORES LÓGICOS

#and
print(True and True) #verdadero
print(True and False) #falso

#or
print(True or True) #verdadero
print(True or False) #verdadero

# not
print(not True) #falso
print(not False) #verdadero

#OPERADORES DE BIT

# Definición de variables
a = 5  # 0101 en binario
b = 3  # 0011 en binario

# AND a nivel de bits
resultado_and = a & b
print("a & b =", resultado_and)  # 0101 & 0011 = 0001 (1 en decimal)

# OR a nivel de bits
resultado_or = a | b
print("a | b =", resultado_or)  # 0101 | 0011 = 0111 (7 en decimal)

# XOR a nivel de bits
resultado_xor = a ^ b
print("a ^ b =", resultado_xor)  # 0101 ^ 0011 = 0110 (6 en decimal)

# NOT a nivel de bits
resultado_not = ~a
print("~a =", resultado_not)  # ~0101 = 1010 (en complemento a dos, esto representa -6)

# Desplazamiento a la izquierda
resultado_shift_left = a << 1
print("a << 1 =", resultado_shift_left)  # 0101 << 1 = 1010 (10 en decimal)

# Desplazamiento a la derecha
resultado_shift_right = a >> 1
print("a >> 1 =", resultado_shift_right)  # 0101 >> 1 = 0010 (2 en decimal)

#OPERADORES DE IDENTIDAD

# Definiendo variables
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# Usando is
print("a is b:", a is b)  # True, porque b es el mismo objeto que a
print("a is c:", a is c)  # False, porque aunque a y c tienen el mismo contenido, son diferentes objetos

# Usando is not
print("a is not b:", a is not b)  # False, porque b es el mismo objeto que a
print("a is not c:", a is not c)  # True, porque a y c no son el mismo objeto

#OPERADORES DE PERTENENCIA

cadena = "Hola, mundo!"

# Usando in
print("Hola" in cadena)  # Devuelve True
print("adiós" in cadena)  # Devuelve False

# Usando not in
print("Hola" not in cadena)  # Devuelve False
print("adiós" not in cadena)  # Devuelve True

#ESTRUCTURAS DE CONTROL

#condicionales (if,elif.else)
a = 10
b = 20

if a + b > 25:
    print("La suma de a y b es mayor que 25")
elif a + b == 25:
    print("La suma de a y b es exactamente 25")
else:
    print("La suma de a y b es menor que 25")

#bucles(for,while)
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"El número es: {num}")

contador = 0
while contador < 5:
    print(f"Contador es: {contador}")
    contador += 1

#bucles con control de flujo(break,continue)
for num in range(10):
    if num == 5:
        break
    print(f"Número: {num}")

for num in range(10):
    if num % 2 == 0:
        continue
    print(f"Número impar: {num}")

#manejo de exepciones(try,except,else,finally)
try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Entrada no válida, se esperaba un número")
else:
    print(f"El resultado de la división es: {resultado}")
finally:
    print("Fin del bloque try-except")



#EJERCICIO DE DIFICULTAD EXTRA
"""Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for numeros in range(10,56):
    if numeros % 2 == 0 and numeros != 16 and numeros % 3 !=0:
        print(numeros) 