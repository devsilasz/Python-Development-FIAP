print("Quilão do Andrezão")
preco_quilo = float(input("Informe o valor cobrado por quilo! "))
peso_prato = float(input("Informe o peso do prato do cliente (em kg) "))
preco_prato = preco_quilo * peso_prato

if (peso_prato > 1) :
    print("Como o peso do prato do cliente ultrapassou 1kg, ele deve pagar apenas o valor fixo de R$80,00")
else :
    print(f"O valor do prato é R${preco_prato:.2f}")
