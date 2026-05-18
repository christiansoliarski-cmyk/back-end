salario = float(input("Qual é o salário do funcionário? R$ "))
if salario > 1250:
    aumento = salario * 0.10  
else:
    aumento = salario * 0.15  
novo_salario = salario + aumento
print(f"O valor do aumento é de: R$ {aumento:.2f}")
print(f"O novo salário será de: R$ {novo_salario:.2f}")
