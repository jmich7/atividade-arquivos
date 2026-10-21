print("ALUNOS APROVADOS")

with open("aprovados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha.strip())

print("\nALUNOS REPROVADOS")

with open("reprovados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha.strip())