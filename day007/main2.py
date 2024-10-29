favorite_anime = input("Qual o seu anime favorito? ")
print()
if favorite_anime == "naruto":
    print("Que nostalgia! Naruto fez a infância de muita gente!")
    like_akatsuki = input("Cê curte a Akastuki? ")
    if like_akatsuki == "sim":
        print("Que foda mano! Era simplesmente a melhor organização criminosa dos animes!")
    else:
        print("Como assim você não gosta da Akatsuki? VACILÃO!")
elif favorite_anime == "one piece":
    print("Você tem bom gosto cara! One Piece é foda demais!")
    favorite_mugiwara = input("Qual o seu mugiwara favorito do trio monstro? ")
    if favorite_mugiwara == "luffy":
        print("\033[31mGOMU GOMU NOOO.. MENINO LUFFY É FODA MANO!\033[0m")
    elif favorite_mugiwara == "zoro":
        print("\033[32mBrabo demais! Até porque o ZORO SOLA!\033[0m")
    elif favorite_mugiwara == "sanji":
        print("\033[33mNosso querido GADO KKKK, menino Sanji é brabo irmão! DIABLE JAMBEE\033[0m")
    else:
        print(f"Cê tá viajando brow! {favorite_mugiwara}, não faz parte do trio monstro!")
else:
    print("Massa irmão! Vou adicionar na minha lista de animes para ver mais tarde!")