with open("exame.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("aprovados.txt", "a") as aprovados:
    with open("reprovados.txt", "a") as reprovados:

        for linha in linhas:
            dados = linha.strip().split(";")

            nome = dados[0]
            media_anterior = float(dados[4])

            nota_exame = float(input("Nota do exame de " + nome + ": "))

            media = (media_anterior + nota_exame) / 2

            if media >= 5:
                aprovados.write(nome + ";Aprovado após exame\n")
            else:
                reprovados.write(nome + ";Reprovado após exame\n")

with open("exame.txt", "w") as arquivo:
    arquivo.write("")