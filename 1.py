with open("notas.txt", "w") as arquivo:
    quantidade = int(input("Quantidade de alunos: "))

    for i in range(quantidade):
        nome = input("Nome: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        arquivo.write(nome + ";" + str(nota1) + ";" + str(nota2) + ";" + str(nota3) + "\n")