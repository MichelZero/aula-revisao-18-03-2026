

valor_total = float(input("Digite o valor total da conta: "))

pagamento_cartao = input("O cliente pagou com cartão de crédito? (S/N): ")

if pagamento_cartao.upper() == "S":
  valor_desconto = valor_total * 0.1
  valor_com_desconto = valor_total - valor_desconto
  print(f"O valor com desconto é: {valor_com_desconto}")
else:
  print("Sem desconto")
