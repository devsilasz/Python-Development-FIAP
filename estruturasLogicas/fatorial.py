#for contadora in range(10, 100, 2) :
# print (contadora)
#  if contadora == 20:
#       break

numero = int(input("Por favor, informe o numero do qual deseja o fatorial "))
fat = numero

for valor in range(1, numero, 1):
    fat = fat * valor

print(f"O fatorial para o numero informado foi {fat}")