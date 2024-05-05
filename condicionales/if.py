salario = int(input("Cual es tu salario: "))
print(salario)

if salario < 1000:
    print("No paga impuestos")
elif salario > 3000:
    print("Paga impuestos triples")
elif salario > 2000:
    print("Paga impuestos dobles")
else:
    print("Paga Impuestos")