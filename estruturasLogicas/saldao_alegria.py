#Uma loja oferece pagamentos por boleto bancário ou por cartão de crédito. Os clientes que pagam através de boleto têm direito a 5% de desconto sobre o valor da compra, enquanto os clientes que pagam através de cartão de crédito podem escolher parcelar a compra em até 12x.
print("Saldão da alegria!")
total_compra = float(input("Por favor, informe o valor total da compra do cliente"))
forma_pagamento = int(input("Selecione a forma de pagamento: 1 - Boleto ou 2 - Cartão "))

if (forma_pagamento == 1) :
    total = total_compra - 0.05 * total_compra
    print(f"O total da compra com o desconto de 10%: {total}")
elif (forma_pagamento == 2) :
    parcelas = int(input("Informe o número de parcelas desejadas?"))
    valor_parcela = total_compra / parcelas
    print(f"O total da compra de R${total_compra:.2f} será pago em {parcelas} parcelas de R${valor_parcela:.2f} ")

else :
    print("Opção inválida")