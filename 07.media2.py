print("Olá! vamos ver qual será sua média")

nota1 = float (input("digite sua primeira nota: "))
nota2 = float(input("digite sua primeira nota: "))
nota3 = float(input("digite sua primeira nota: "))
nota4 = float(input("digite sua primeira nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(" media final obtida: ",media)

if(media >= 80):
    print("Aluno aprovado!!!")
else:
    print("Aluno reprovado!!!")