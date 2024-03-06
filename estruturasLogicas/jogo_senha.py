resposta = ""
tentativa = 0
while resposta != "PYTHON":
    resposta = input("Digite a senha secreta!").upper()
    tentativa = tentativa + 1

print("A senha correta foi digitada")
print(f"Foi preciso usar {tentativa} tentativas para o êxito")