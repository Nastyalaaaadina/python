import math
a=int(input('Введите длину первого катета:'))
b = int(input('Введите длину второго катета:'))
 
print('Периметр равен:', a+b+math.sqrt(a*a+b*b))
print('Площадь равна:', a*b/2)
