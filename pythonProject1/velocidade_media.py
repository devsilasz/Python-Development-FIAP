print("Simulador de computador de bordo")
distancia = float(input("Digite a distancia percorrida: "))
tempo = float(input("Digite o tempo da viagem: "))

velocidade_media = distancia/tempo


print("A velocidade media é {:.2f} km/h".format(velocidade_media))
print(f"A velocidade media é {velocidade_media:.2f} km/h")

#:.2f significa que serão 2 numeros depois da virgula
