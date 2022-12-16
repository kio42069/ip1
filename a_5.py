def fact(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

def convert(n):                                 #Function to convert degres to radians
    return n*3.14/180

def sine(n):                                    #Function to calculate sin, takes input in degrees
    s = 0
    n = convert(n)
    for i in range(1,171,2):
        s += -((-1)**((i+1)/2))*(n**i)/fact(i)
    return abs(s)

def cosine(n):                                  #Function to calculate cos, takes input in degrees
    s = 0
    n = convert(n)
    for i in range(0,171,2):
        s += ((-1)**((i)/2))*(n**i)/fact(i)
    return abs(s)

def tangent(n):                                 #Fucntion to calculate tan, takes input in degrees
    return (sine(n))/(cosine(n))

angle = int(input("Enter angle: "))
base = float(input("Enter base length: "))
height = tangent(angle) * base                  #Calculating height of pole using trigonometry
hypotenuse = (base**2 + height**2)**0.5         #Calcluating hypotenuse using Pythagoras Theorem

print(f"Height of the pole is {height} and distance of the person from the top of the pole is {hypotenuse}")
