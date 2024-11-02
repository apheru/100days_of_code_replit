# [DESAFIO] Quantos segundos tem no ano?

# 60 segundos em 1 minuto

seconds_for_minute = 60

# 60 minutos em 1 hora

seconds_for_hour = seconds_for_minute * 60

# 24 horas em 1 dia

seconds_for_day = seconds_for_hour * 24

# 365 dias em 1 anos / 366 dias se for bissexto

seconds_for_year = seconds_for_day * 365

# De forma mais rapida

# seconds_for_year = 60 * 60 * 24 * 365

print(seconds_for_year)

print("=== CALCULADORA DE SEGUNDOS POR ANO ===")
print()
leap_year = int(input("É ano bissexto? [1 - Sim | 2 - Não] "))
if leap_year == 1:
    is_leap_year = seconds_for_year + seconds_for_day
    print(f"Um ano bissexto, possui {is_leap_year:,} segundos.")
elif leap_year == 2:
    print(f"Um ano, possui {seconds_for_year:,} segundos.")
else:
    print("Informe um dos valores corretos acima, 1 ou 2! Deixe de ser cabeçudo!")