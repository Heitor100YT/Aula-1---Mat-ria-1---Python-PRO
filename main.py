meme_dict = {
            "IA": "Inteligência Artificial",
            "HOLANDA": "Países Baixos",
            "BIELORÚSSIA": "Belarus",
            "SUAZILÂNDIA": "Essuatíni",
            "NOTEBOOK": "Computador"
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Essa palavra não existe no dicionário, tente outra!")
