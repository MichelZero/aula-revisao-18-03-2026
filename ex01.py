# 1.	Escreva um programa que verifica se 
# um número é positivo, 
# negativo ou zero e 
# imprime a mensagem correspondente.

# Entrada de dados
num1 = int(input("inf. um numero: "))

# processamento e saída
if (num1 > 0):
  print("positivo")
elif (num1 < 0):
  print("negativo")
else:
  print("é nulo ou zero")