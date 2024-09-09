#calculadora de fatorial
numero = int(input("digite um numero: "))
fatorial = 1
contador = 1

while(contador <= numero):
    fatorial *= contador
    contador += 1

    print(f"o fatorial de {numero} é {fatorial}")