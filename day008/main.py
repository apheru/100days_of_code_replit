print("=== InspiraMais Express ===")
print()
name = input("Olá! 👋 Como você se chama? ")
print()
dream = input("Qual o seu grande sonho ou objetivo? ")
print()
feeling = int(input("Em uma escala de 1 - 10. Como você está se sentindo hoje? (1: 😥, 10: 😁) "))
print()
if feeling == 1:
    print(f"\033[36m{name}\033[0m, sei que talvez as coisas pareçam difíceis agora, mas lembre-se de que você é mais forte do que imagina. O seu sonho de \033[36m{dream}\033[0m está mais perto do que você pensa. Cada passo conta, mesmo os mais pequenos!")
elif feeling == 2:
    print(f"Ei, \033[36m{name}\033[0m! Só de ter clareza sobre seu sonho de \033[36m{dream}\033[0m já é um grande avanço. Respire fundo e acredite, um dia de cada vez, e logo verá o progresso.")
elif feeling == 3:
    print(f"Lembre-se, \033[36m{name}\033[0m, dias difíceis fazem parte da jornada, mas nunca apagam o brilho do seu sonho de \033[36m{dream}\033[0m. Confie em sia mesmo e siga em frente, mesmo que devagar.")
elif feeling == 4:
    print(f"\033[36m{name}\033[0m, você está no caminho certo para realizar seu sonho de \033[36m{dream}\033[0m. Continue se movendo com firmeza e lembre-se de que as dificuldades sempre ensinam algo valioso.")
elif feeling == 5:
    print(f"\033[36m{name}\033[0m, as coisas talvez ainda não estejam como você quer, mas você está cada vez mais perto do seu objetivo de \033[36m{dream}\033[0m. Acredite no seu potencial e continue em frente!")
elif feeling == 6:
    print(f"Persistência é a chave, \033[36m{name}\033[0m. Todo esforço vale a pena, e o seu sonho de \033[36m{dream}\033[0m merece ser alcançado. Continue caminhando e verá o pogresso!")
elif feeling == 7:
    print(f"\033[36m{name}\033[0m, você já está alcançando grandes coisas! O seu sonho de \033[36m{dream}\033[0m está cada vez mais perto. Continue assim, sua determinação é inspiradora!")
elif feeling == 8:
    print(f"\033[36m{name}\033[0m, sua energia está incrível! Continue nessa jornada para alcançar \033[36m{dream}\033[0m e saiba que você é capaz de superar qualquer desafio que apareça.")
elif feeling == 9:
    print(f"Cada passo está levando você ao seu sonho de \033[36m{dream}\033[0m, \033[36m{name}\033[0m! Confie nesse caminho e celebre cada pequena vitória. Você está indo muito bem!")
elif feeling == 10:
    print(f"\033[36m{name}\033[0m, você está voando! O seu objetivo de \033[36m{dream}\033[0m está quase ao alcance. Matenha essa energia incrível e aproveite cada passo dessa jornada.")