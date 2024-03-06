#Uma companhia aérea permite que seus clientes do tipo premium despachem bagagens de até 32kg sem nenhum custo adicional, enquanto os clientes do tipo gold podem levar malas de até 28kg sem nenhum custo adicional e todos os demais devem pagar por qualquer bagagem despachada.
tipo_cliente = input("Por favor, informe o tipo do cliente: PREMIUM, GOLD ou REGULAR")
peso_bagagem = float(input("Informe o peso da bagagem que o cliente deseja despachar"))

if (tipo_cliente.upper() == "PREMIUM") :
    if (peso_bagagem <= 32) :
        print("Sem custo adicional")
    else :
        print("Custo adicional")
elif (tipo_cliente.upper() == "GOLD") :
    if (peso_bagagem <= 28) :
        print("Sem custo adicional")
    else :
        print("Custo adicional")

else :
    print("Deve pagar por qualquer bagagem despachada")
