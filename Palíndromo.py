P = str(input("Digite a palavra: "))

if (P == P[::-1]): #[::-1] inverte a palavra string (str)
    print("Sua palavra é Palíndroma")
    
else:
    print("Sua palavra não é Palíndroma")

#(Outra versão, sem restrições de letras Maiusculas)

# def verificar_palindromo(texto):

#     Remover espaços e transformar para minúsculas
#     texto = texto.replace(" ", "").lower()

#     Comparar o texto com a versão invertida
#     if texto == texto[::-1]:
#         return "É um palíndromo!"
#     else:
#         return "Não é um palíndromo."

# frase = input("Digite uma palavra ou frase: ")
# print(verificar_palindromo(frase))
