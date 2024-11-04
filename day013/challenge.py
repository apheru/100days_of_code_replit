print("=== Calculadora de notas de Exame ===")
print()
exam = input("Nome do exame >> ")
print()
max_score = float(input("Pontuação Máxima do Exame >> "))
print()
my_score = float(input("Sua pontuação >> "))
print()
porcentagem = my_score / max_score
media = porcentagem * 100

score = ""
if media >= 90:
    score = "\033[32mA+\033[0m"
elif media >= 80:
    score = "\033[32mA-\033[0m"
elif media >= 70:
    score = "\033[34mB\033[0m"
elif media >= 60:
    score = "\033[33mC\033[0m"
elif media >= 50:
    score = "\033[33mD\033[0m"
else:
    score = "\033[31mF\033[0m"
    

print(f"Você obteve {media:.2f} % do exame, tirou uma nota {score}")
