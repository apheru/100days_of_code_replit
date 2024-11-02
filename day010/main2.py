my_bill = float(input("Qual o valor da conta? "))
friends_number = int(input("São quantas pessoas? "))
bill = my_bill / friends_number
print(f"O valor para cada uma das {friends_number} pessoas pagar é de R$: {round(bill, 2)}")