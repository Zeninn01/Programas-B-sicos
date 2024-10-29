Frase = input("Digite sua frase: ")

Conta_Vogais = 0

Vogais = "aeiouAEIOU"

for Letra in Frase:
    if Letra in Vogais:
        Conta_Vogais += 1
        
print(f"Número de vogais na frase é: {Conta_Vogais}")
