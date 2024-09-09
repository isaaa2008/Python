contador = 0 
numero = int(input("digite o valor da tabuada: "))

while (numero<=10):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
    