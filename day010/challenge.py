print("=== Calculadora de Gorjetas ===")
print()
bill = float(input("Qual foi o valor total da conta? "))
print()
tip = int(input("Qual porcentagem você deseja pagar de gorjeta? "))
tip_percentage = tip / 100
print()
peoples = int(input("Quantas pessoas possui no seu grupo? "))
division_bill = bill / peoples
my_bill = division_bill + (division_bill * tip_percentage)
print()
print(f"Cada um de vocês deve pagar R$: {round(my_bill, 2)}")
