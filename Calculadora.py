print("***** CALCULADORA *****\n")

opcao = int(input("Selecione uma operação: \n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n"))

a = float(input("Inisra o primeiro número: "))
b = float(input("Inisra o segundo número: "))

if opcao == 1:
  print(f"Soma = {a+b}")
elif opcao == 2:
  print(f"Subtração = {a-b}")
elif opcao == 3:
  print(f"Divisão = {a/b}")
elif opcao == 4:
  print(f"Multiplicação = {a*b}")
else:
  print("Opção Inválida")

