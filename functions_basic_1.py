#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
"""prediccion: 5; solucion:5"""

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
"""prediccion: 5 ; solucion:devuelve un error porque nuber_of_days no tiene valor definido"""

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
"""prediccion: 5,10 ; solucion: 5 porque solo se retorna el primer valor y la funcion termina de ejecutarse"""

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
"""prediccion: 5; solucion:5 (la funcion termina en el primer valor de retorno)"""

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
"""prediccion: 5; solucion:5,none (porque la funcion no retorna ningun valor)"""

6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
"""prediccion: 8 ; solucion:3, 5 , TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType' (no funciona porque no hay valor de retorno)"""


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
"""prediccion: 25 ; solucion:25 (esta sumando los numeros como si fuesen cadenas)"""


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
"""prediccion: 100, 10 ; solucion:100,10"""


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""prediccion: 7, 14,7-14-21 ; solucion:7,14,21 (pense que los valores de retorno se iban a mostrar en la consola y no solo el resultado)"""


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
"""prediccion: 8 ; solucion:8"""


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
"""prediccion: 500, 500,none,500 ; solucion:500,500,300,500 (pense que al no haber valor de retorno no se imprimiria nada en la consola)"""


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
"""prediccion: 500,500,300,300,500 ; solucion:500,500,300,500 (pense que se imprimiria b dentro de la funcion)"""


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
"""prediccion: 500,500,300,300 ; solucion:500,500,300,300"""


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
"""prediccion: 1,3,2 ; solucion:1,3,2"""


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
"""prediccion: 10 ; solucion:1,3,5,10 (crei que solo se retornaria el valor de retono de la funcion foo)"""
