palavra = input('Digite a palavra secreta: ')
for x in range(80):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha=""
    for letra in palavra:
        if letra in acertos:
            senha += letra
        else:
            senha += "_"

    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input('\n Digite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('você errou!')
    print('X===:==\nX   :  ') 
    print('X   O  ' if erros>=1 else "X")
    linha2=""
    if erros == 2:
        linha2 = "   | "
    elif erros == 3:
        linha2 = "  /|  "
    elif erros >= 4:
        linha2 = "  /|\  "
    print("X%s" % linha2)
    linha3 = ""
    if erros ==5:
        linha3+="  / "
    elif erros >=6:
        linha3+="  / \  "
    print("X%s" % linha3)
    print("X\n============")
    if erros == 6:
        print("Enforcado. Parabéns, você morreu! X_X")
        print('A palvra secreta era: ', palavra)
        break