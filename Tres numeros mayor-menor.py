#ordenar tres numeros de mayor a menor 
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

num1 = min(a, b, c)
num3 = max(a, b, c)
num2 = (a + b + c) - num1 - num3

#impresion en pantalla del resultado 
print("Orden mayor a menor: ", num3, num2, num1)