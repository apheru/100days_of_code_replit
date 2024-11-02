print("=== IDENTIFICADOR DE GERAÇÃO ===")
print()
year_born = int(input("Em que ano você nasceu? "))
print()
if year_born >= 2012:
    print("Ah, a \033[36mGeração Alpha\033[0m! Os primeiros a nascer completamente no século 21, crescendo com tecnologia avançada em cada etapa da vida.")
elif year_born >= 1997:
    print("\033[36mGeração Z\033[0m! Super conectada e digital desde o início. Vive entre telas, inovação e uma visão de mundo aberta.")
elif year_born >= 1981:
    print("Você é \033[36mMillennial\033[0m! Cresceu com a internet e busca equilibrar propósito e carreira. Adaptável e focado no impacto social.")
elif year_born >= 1965:
    print("\033[36mGeração X\033[0m! Conhecida pela independência e atitude prática. Foi a ponte entre o mundo analógico e a revolução digital.")
elif year_born >= 1946:
    print("\033[36mBaby Boomer\033[0m! A época da reconstrução e do crescimento econômico. Cresceu junto com a expansão da liberade e da cultura pop.")
elif year_born >= 1928:
    print("Ah, \033[36mGeração Silenciosa\033[0m! Discreta e trabalhadora, cresceu com valores fortes e sempre soube enfrentar a vida com sabedoria.")
elif year_born >= 1901:
    print("Você faz parte da \033[36mMaior Geração\033[0m! Superou a Grande Depressão e lutou na Segunda Guerra. Resiliência é seu sobrenome.")

elif year_born >= 1883:
    print("Ah, você é da \033[36mGeração Perdida\033[0m! Viveu os tempos desafiadores da Primeira Guerra e soube valorizar as pequenas alegrias da vida.")
else:
    print("Hmmm... parece que você veio de um tempo distante, ainda não catalogado! Uma geração misteriosa e única!")