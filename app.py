altura = float(input("ALTURA: "))
peso = float(input("PESO: "))

alturaD =  altura * altura
imc = peso / float(alturaD)


print("TU IMC ES IGUAL A: ", imc)

if imc > 24.9:
    print("TIENE SOBREPESO")
elif imc < 18.5:
    print("ESTA CON BAJO PESO")
else:
    print("SU PESO ES NORMAL")
