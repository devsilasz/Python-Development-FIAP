usuario = input("Informe o usuário que deseja acessar o sistema: ")
senha = input("Informe a senha do usuário que deseja acessar o sistema: ")
if usuario.upper() == "ADMIN" and senha == "123":
    print("Acesso autorizado! ")
else:
    print("Username ou password incorretos. Acesso negado!")