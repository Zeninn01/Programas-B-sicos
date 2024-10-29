chamada = []

presentes = int(input("Quantos alunos vieram hoje? "))

for _ in range(presentes):
    Nome = input("Digite o nome do aluno presente: ")
    chamada.append(Nome)
    
print("Lista de Presença:", chamada)
