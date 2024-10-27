print("\033[36m=== MY LOGIN SYSTEM ===\033[0m")
print("=======================")
print()
username = input("\033[32mUsername >>\033[0m ")
password = input("\033[32mPassword >>\033[0m ")

if username == "Apheru" and password == "4ph3ru":
    print(f"Bom dia, \033[34m{username}\033[0m! O sol nasceu para novas conquistas, e o mundo é seu para explorar! Que seu dia seja repleto de realização e bons momentos.")
elif username == "Naillath" and password == "N41ll4th":
    print(f"Olá, \033[35m{username}\033[0m! Que esta manhã traga a energia de que você precisa para alcançar seus objetivos. Comece o dia com determinação, e o sucesso virá!")
elif username == "Khalled" and password == "Kh4ll3d":
    print(f"Bom dia, \033[33m{username}\033[0m! Que hoje seja um capítulo memorável na sua jornada. A cada passo, você se aproxima dos seus sonhos. Aproveite cada momento.")
else:
    print("Bom dia! Não encontramos seu usuário no sistema. Verifique suas credenciais ou cadastre-se para começar uma nova jornada conosco!")