n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
soma = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2

print(type(n1)) #isso mostra qual é o tipo da variável lida.
print(soma)
#ou
print("O resultado da soma foi:  {}".format(soma))
#ou podemos utilizar o F-String, veja abaixo:
print(f"O resultado da soma foi: {soma}")
print(f"O resultado da subtração foi: {sub}")
print("O resultado da divisão foi: {}".format(soma))
print(f"O resultado da multiplicação foi {mult}")