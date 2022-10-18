import math 

def quadratic(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        print("D > 0")
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif D == 0:
        print("D = 0")
        x = -b/(2*a)
        print(f"x = {x}")
    elif D < 0:
        print("Нет решений")

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

quadratic(a,b,c)