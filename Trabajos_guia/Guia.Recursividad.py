
#Ejercicios de la guia.
#RECURSIVIDAD.
#Ejercicio 1 de la guia.
#5 + 4 + 3 + 2 + 1 = 15
#sum(n) = n + sum(n-1)    -> sum(0)= 0

def sum(num:int)->int:
    if num == 0:
        return 0
    else:
        return num + sum(num - 1)
    
print(sum(5))


#Ejercicio 3 de la guia.
#2 * 3= 2 + 2 + 2 = 6
#prod(n, m) = n+ prod(n, m-1)   -> m = 0 

def prod(n: int, m: int)->int:
    if m== 0:
        return 0
    else:
        return n + prod(n, m - 1)

print(prod(1, 3))

#Ejercicio 7 de la guia.
#h(n) = 1/n + 1/(n-1) + 1/(n-2) + ... n = 1 -> 1

def serie_h(num: int)->float:
    if num == 1:
        return 1
    else:
        return 1/num + serie_h(num - 1)
    
print(serie_h(3))

#Ejercicio 4 de la guia.
#pot(n,m)= n * n ... m veces -> pot(n, m) = n * pot(n, m-1) -> pot(n, 0) = 1
def pot(n:int, m:intr)->int:
    if m == 0:
        return 1
    else:
       return n * pot(n, m-1)
    
print (pot(3,3))

#Ejercicio 9 de la guia.
def log(n:int, b:int)->int:
    if n < b:
        return 0
    else:
        return 1 + log(n//b,b)
    
print(log(16,2))

#Ejericio 10 de la guia.
#Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contar_digitos(n:int)->int:
    if n == 0:
        return 1
    
    if n < 10: 
        return 1
    return 1 + contar_digitos(n//10)

print(contar_digitos(333333))

#Ejercicio 6 de la guia.

def invertir(cadena: str) -> str:
    if cadena == "":
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1])

print(invertir('hola'))

