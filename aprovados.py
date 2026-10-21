with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("aprovados.txt", "w") as aprovados:
    with open("exame.txt", "w") as exame:
        with open("reprovados.txt", "w") as reprovados:

            for linha in linhas:
                dados = linha.strip().split(";")

                nome = dados[0]
                nota1 = float(dados[1])
                nota2 = float(dados[2])
                nota3 = float(dados[3])

                media = (nota1 + nota2 + nota3) / 3

                registro = nome + ";" + str(nota1) + ";" + str(nota2) + ";" + str(nota3) + ";" + str(round(media, 2)) + "\n"

                if media >= 7:
                    aprovados.write(registro)
                elif media >= 5:
                    exame.write(registro)
                else:
                    reprovados.write(registro)