#Algoritmo do ano bissexto
#o usuário digitará o ano e o programa informará se o ano 
# é ou não bissexto.
#regras do ano bissexto:
#-O ano deve ser mútiplo de 4
#-O ano não deve ser mútiplo de 100
#-Exceto anos mútiplos de 400


ano = int(input("digite o ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f"O ano{ano} é bissexto")
else:
   print(f"O ano {ano} não é bissexto")