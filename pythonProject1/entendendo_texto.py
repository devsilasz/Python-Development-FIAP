texto = "Este texto quebra de linha aqui \n. Porém aqui temos uma \ttabulação"
print(texto)

texto = "texto em minusculas AINDA É texto"
print(texto.capitalize()) #função para transformar palavras maiusculas em minusculas, porém começando com letra maiuscula
print(texto.upper()) #função para transformar tudo em letras maiúsculas
print(texto.lower()) #função para transformar tudo em letras minusculas
print(texto.startswith("tex")) #verifica se a string texto começa com "tex", se sim, dará true, senão dará false
print(texto.endswith("!")) #Verifica se o último caractere da string texto é "!", se sim, dará true, senão, dará false
print(texto.count("e")) #Conta quantas vezes aparece determinado caractere, como por exemplo ao lado, a letra "e"
print("em" in texto) #Verifica se determinada string se localiza em texto
print(texto.replace("AINDA", "com certeza")) #Altera a string, porém não permanente
print(texto)