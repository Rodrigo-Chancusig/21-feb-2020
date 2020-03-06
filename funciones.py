# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def message():
    print("Ingrese un valor: ")
    
message()
a=int(input())
message()
b=int(input())
message()

def hi(name):
    print("Hi,", name)
    
hi("Greg")
hi("Rod")
hi("Fab")

def hiAll(name1, name2):
    print("Hi,",name2)
    print("Hi,",name1)
    
hiAll(s, c)

def address(street, city, postalcode):
    print("Your address is:", street, "St., ")

s= input("street:")
pC=input("Postal Code:")
c = input("City: ")

address(s, c, pC)

def subtra(a, b):
    print(a-b)
subtra(5, 2) #outputs: 3
subtra(2, 5) #outputs: -3

def subtra(a, b):
    print(a-b)
subtra(a=5, b=2) #outputs: 3
subtra(a=2, b=5) #outputs: -3

def subtra(a, b):
    print(a-b)
subtra(5, b=2) #outputs: 3
subtra(2, 5) #outputs: -3

def subtra(a, b):
    print(a-b)
subtra(a=5, 2) #outputs: 3
subtra(2, 5) #outputs: -3 aqui hay errores

def multiply(a, b):
    return a*b
print(multiply(3, 4)) # outputs: 12

def multiply(a, b):
    return
print(multiply(3, 4)) # outputs: None

def wishes():
    return "Happy Birthday"
w=wishes()
print(w)  #outputs: Happy Brithday

#Ejercicio 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"
wishes()  # outputs: my Wishes

#Ejercicio 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"
print(wishes())  # outputs: my Wishes
                 #      Happy Birthday

def hiEverybody(myList):
    for name in myList:
        print("Hi,", name)
        
hiEverybody(["Adam","John","Lucy"])
hiEverybody(["Adam","John","Lucy","Rod","Fab","Chan"])

def createList(n):
    myList=[]
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))
print(createList(15))


def isPrime(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #de lo contrario devuelve Verdadero

isPrime(3)
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()



def l100kmtompg(liters):
  gallon = liters/3.785411784
  mpg = 100/1.609344 
  return(mpg/gallon)

def mpgtol100km(miles):
  km = miles * 1.609344
  return((3.785411784/km)*100)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))






    


