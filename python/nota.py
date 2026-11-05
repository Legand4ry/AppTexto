nome = input("nome do aluno:")
idade = int(input("idade do aluno:"))
nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print()
print("=====cadastro=====")
print(f"nome: {nome}, {idade} anos")
print(f"notas: {nota1} + {nota2} + {nota3}")
print(f"media: {media: .1f}")
print(f"daqui a 10 anos: {idade + 10} anos")
