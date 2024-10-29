print("MINI QUIZ - ONE PIECE")
print()
print("================================")
print()
like_one_piece = input("Você gosta de One Piece? ")
if like_one_piece == "sim":
    favorite_mugiwara = input("Qual seu mugiwara favorito? ")
    if favorite_mugiwara == "luffy":
        job_ship_luffy = input("Escolheu bem! Luffy é um líder destemido que sonha em ser o Rei dos Piratas! Sabe qual é o papel dele no bando? ")
        if job_ship_luffy == "capitão" or job_ship_luffy == "capitao":
            print("Acertou! Luffy é o capitão do bando, liderando todos com coragem! 👒")
        else:
            print("Quase! Mas esse não é o papel de Luffy! 🥴")
    elif favorite_mugiwara == "zoro":
        job_ship_zoro = input("Zoro, o guerreiro que segue seu próprio caminho! Uma escolha poderosa! Mas sabe qual é a função dele na tripulação? ")
        if job_ship_zoro == "espadachim":
            print("Isso mesmo! Zoro é o espadachim da tripulação! ⚔")
        else:
            print("Não exatamente... esse não é o papel de Zoro")
    elif favorite_mugiwara == "sanji":
        job_ship_sanji = input("Sanji, o elegante e habilidoso! Um verdadeiro estilo dentro e fora das lutas! Sabe qual é a função dele no bando? ")
        if job_ship_sanji == "cozinheiro":
            print("Perfeito! Sanji é o cozinheiro da tripulação! 🥗")
        else:
            print("Quase, mas Sanji exerce outra função. Tente novamente")
    elif favorite_mugiwara == "usopp":
        job_ship_usopp = input("Usopp, o 'corajoso' e criativo! Ele sempre traz algo inesperado! Qual será o papel dele na tripulação? ")
        if job_ship_usopp == "atirador":
            print("Usopp, o corajoso e criativo! Ele sempre traz algo inesperado! Qual será o papel dele na tripulação? 🔫")
        elif job_ship_usopp == "capitão" or job_ship_usopp == "capitao":
            print("Ha ha ha, então você acredita nas histórias do próprio Usopp, hein? Ele até se acha o 'Capitão Usopp' de vez em quando! Mas, na realidade, o nosso bravo guerreiro do mar ainda não ocupa esse cargo! 😅")
        else:
            print("Não foi dessa vez. Tente de novo com outro papel para Usopp. 😮")
    elif favorite_mugiwara == "nami":
        job_ship_nami = input("Nami, sempre brilhante e estrategista! Uma ótima escolha! Você sabe qual função ela exerce no bando? ")
        if job_ship_nami == "navegadora":
            print("Acertou em cheio! Nami é a navegadora do bando! 🗺🍊")
        else:
            print("Errou... essa função não é da Nami. 😪")
    elif favorite_mugiwara == "chopper":
        job_ship_chopper = input("Chopper! A adorável rena que sempre ajuda a todos no bando! Consegue dizer qual é o papel dele no bando? Além de roubar nossos corações com tamanha fofura! 😍😍 ")
        if job_ship_chopper == "médico" or job_ship_chopper == "medico":
            print("Isso mesmo! Além de ser super fofo, o Chopper é o médico do grupo! 🩺")
        else:
            print("Não exatamente... esse não é o papel do nosso pequenino Chopper. 😫")
    elif favorite_mugiwara == "nico robin" or favorite_mugiwara == "robin":
        job_ship_robin = input("Robin, a sábia e enigmática! Ela traz muito conhecimento ao grupo. Você sabe qual é a função dela na tripulação? 📚📚")
        if job_ship_robin == "arqueóloga" or job_ship_robin == "arqueologa":
            print("Correto! Robin é a arqueóloga da tripulação. 🏛")
        else:
            print("Não foi dessa vez. Robin tem outra função no bando. 🤗")
    elif favorite_mugiwara == "franky":
        job_ship_franky = input("Franky, sempre trazendo estilo e invenções únicas para o bando! Mas qual é a função dele no grupo? 🥤")
        if job_ship_franky == "engenheiro" or job_ship_franky == "mecanico" or job_ship_franky == "mecânico":
            print("Acertou! Franky é o engenheiro da tripulação! ⚙")
        else:
            print("Não é isso... Franky desempenha outro papel. 😶")
    elif favorite_mugiwara == "brook":
        job_ship_brook = input("Brook, o animado e inusitado! Ele sempre traz alegria ao grupo! Sabe qual é o papel dele na tripulação? 💀")
        if job_ship_brook == "músico" or job_ship_brook == "musico":
            print("Perfeito! Brook é o músico do bando! 🎻")
        else:
            print("Quase, mas essa não é a função de Brook. 💀")
    elif favorite_mugiwara == "jinbe":
        job_ship_jinbe = input("Jinbe, o forte e experiente! Ele traz muita sabedoria ao grupo. Qual será a função dele no bando?")
        if job_ship_jinbe == "timoneiro":
            print("Correto! Jinbe é o timoneiro do bando! ⛵")
        else:
            print("Correto! Jinbe é o timoneiro do bando! 😅")
    else:
        print("Agora cê viajou na maionese mano! Esse não é um Mugiwara!")
else:
    print("Como assim, você não gosta de ONE PIECE? Manooo.. você tem demência? 🙄")