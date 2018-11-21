import sys
palabra = input("Elija la palabra a adivinar: ")
print("Tiene 6 oportunidades")
cont = 6
sinadivinar = 1
while(sinadivinar and cont > 0):
	letra = input("Elija una letra")
	
	for i in palabra:
		print(palabra[i])
	sinadivinar = 0