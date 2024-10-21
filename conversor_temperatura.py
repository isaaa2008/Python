#celsius para fahrenheit
def celsius_fahrenheit(c):
    f = c * 1.8 + 32 
    return f
#celsius para kelvin 
def celsius_kelvin(c):
    k = c + 273
    return k
#fahrnheit para celsius
def fahrnheit_celsius(f):
    c = (f - 32) /1.8
    return c
#fahrnheit para kelvin
def fahrnheit_kelvin(f):
    k =(f - 32) * 5 / 9 + 273
    return k
#kelvin para celsius
def kelvin_celsius(k):
   c = k - 273
   return c
#kelvin para fahrnheit
def kelvin_fahrnheit(k):
  f = (k - 273) * 1.8 + 32
  return f
 
#função principal 
def conversor():
    print("conversor de temperaturas")
    while True: 
        print("\n Escolha a operação: ")
        print("1- celsius para fahrenheit")
        print("2- celsius para kelvin")
        print("3- fahrenheit para celsius")
        print("4- fahrenheit para kelvin")
        print("5- kelvin para celsius")
        print("6-  kelvin para fahrenheit")
        print("0- sair")

        opcao = int(input("digite o númmero da opreração desejada: "))

        if opcao == 0:
            print("conversor enrrada.")
            break
    
        temperatura = float(input("digte o número de operação desejada"))

        if opcao == 1:
            resultado=celsius_fahrenheit(temperatura)
            print(f"{temperatura}° c é igual a {resultado} ° f")
        elif opcao == 2:
            resultado= celsius_kelvin(temperatura)
            print(f"{temperatura}° c é igual a {resultado} ° k")
        elif opcao == 3:
            resultado= fahrnheit_celsius (temperatura)
            print(f"{temperatura}° f é igual a {resultado} ° c")
        elif opcao == 4:
            resultado= fahrnheit_kelvin (temperatura)
            print(f"{temperatura}° f é igual a {resultado} ° k")
        elif opcao == 5:
            resultado= kelvin_celsius (temperatura)
            print(f"{temperatura}° k é igual a {resultado} ° c")
        elif opcao == 6:
            resultado= kelvin_fahrnheit (temperatura)
            print(f"{temperatura}° k é igual a {resultado} ° f")
        else:
            print("opção invalida")
            conversor()    
            
            
            
            
