import re

# Méthode qui va servir à chiffrer le message

def chiffrercesar():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    listalpha1 = list (a)
    listalpha2 = list (b)
    count = -1

    # On choisis le chiffre de décalage

    print("Choisissez le chiffre de décalage ! ")
    print("(Au dessus de 26, le décalage sera inutile)")

    # On vérifie que c'est un chiffre

    while True:
        try:
            chiffre = int(input("Chiffre : "))
            break
        except ValueError:
            print("Entrez un chiffre !")
    print("Chiffre de décalage confirmé : " + str(chiffre))

    # L'alphabet se décale en fonction du chiffre de décalage

    section = listalpha2[0 : int(chiffre)]

    listalpha2 = listalpha2[int(chiffre) : ]
    listalpha2 = listalpha2 + section

    print(listalpha2)

    # On choisis le message à chiffrer

    print("Quel est le message à chiffrer ?")
    message = input()
    message = "".join(re.split("[^a-zA-Z]*", message))
    listmess = list (message.upper())

    # On remplace chaque lettre du message par la lettre correspondante au nouvel alphabet

    for i in listmess:
        for j in listalpha1:
            if i == j:
                count += 1
                index = listalpha1.index(j)
                listmess[count] = listalpha2[index]
    
    messcrypt = ''.join(listmess)
    print(messcrypt)
    
# Méthode qui va servir à déchiffrer le message

def dechiffrercesar():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    listalpha1 = list (a)
    listalpha2 = list (b)
    count = -1

    # On choisis le chiffre de décalage

    print("Choisissez le chiffre de décalage ! ")
    print("(Au dessus de 26, le décalage sera inutile)")

    # On vérifie que c'est un chiffre

    while True:
        try:
            chiffre = int(input("Chiffre : "))
            break
        except ValueError:
            print("Entrez un chiffre !")
    print("Chiffre de décalage confirmé : " + str(chiffre))

    # L'alphabet se décale en fonction du chiffre de décalage

    section = listalpha2[0 : int(chiffre)]

    listalpha2 = listalpha2[int(chiffre) : ]
    listalpha2 = listalpha2 + section

    print(listalpha2)

    # On choisis le message à déchiffrer

    print("Quel est le message à déchiffrer ?")
    message = input()
    message = "".join(re.split("[^a-zA-Z]*", message))
    listmess = list (message.upper())

    # On remplace chaque lettre du message par la lettre correspondante à l'alphabet de base

    for i in listmess:
        for j in listalpha2:
            if i == j:
                count += 1
                index = listalpha2.index(j)
                listmess[count] = listalpha1[index]
            
    print(''.join(listmess))

def chiffrervigenere():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    listalpha2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    cryptlist = []
    count= -1

    listalpha1 = list (a)

    # On choisis la clef

    print("Choisissez la clef ! ")
    while True:
        try:
            clef = str(input("Clef : "))
            break
        except ValueError:
            print("Pas de chiffres !")
    clef = "".join(re.split("[^a-zA-Z]*", clef))
    listclef = list (clef.upper())
    print("Clef confirmé : " + str(clef))

    # On choisis le message à chiffrer

    print("Quel est le message à chiffrer ?")
    while True:
        try:
            message = str(input("Message : "))
            break
        except ValueError:
            print("Pas de chiffres !")
    message = "".join(re.split("[^a-zA-Z]*", message))
    listmess = list (message.upper())

    # La clef va prendre exactement la même taille que le message

    if len(listclef) < len(listmess):
        while len(listclef) < len(listmess):
            listclef += listclef

        if len(listclef) > len(listmess):
            lenlistclef = len(listclef)
            lenlistmess = len(listmess)
            x = lenlistclef - lenlistmess
            listclef = listclef[ : -x]
    
    elif len(listclef) > len(listmess):
        lenlistclef = len(listclef)
        lenlistmess = len(listmess)
        x = lenlistclef - lenlistmess
        listclef = listclef[ : -x]

    # On récupère l'index de chaque lettre de la clef

    listclef2 = []
    for i in listclef:
        for x in listalpha1:
            if i == x:
                indlistclef = listalpha1.index(x)
                listclef2.append(indlistclef)

    # On récupère l'index de chaque lettre du message            

    listmess2 = []
    for j in listmess:
        for y in listalpha1:
            if j == y:
                indlistmess = listalpha1.index(y)
                listmess2.append(indlistmess)

    # On additionne pour chaque lettre l'index du message à l'index de la clef

    finallist = [listclef2[i]+listmess2[i] for i in range(min(len(listclef2),len(listmess2)))]+max(listclef2,listmess2,key=len)[min(len(listclef2),len(listmess2)):]

    # On évite de dépasser 26 (pour les 26 lettres de l'alphabet)

    for i in finallist:
        count += 1
        if i > 26:
            finallist[count] = finallist[count] - 26
    
    # Et enfin, on fait correspondre les indices à l'alphabet traditionnel non transformé, afin d'obtenir le message chiffré

    for i in finallist:
        for j in listalpha2:
            if i == j:
                var = i
                indfinal = listalpha1[var]
                cryptlist.append(indfinal)

    messcrypt = ''.join(cryptlist)
    print(messcrypt)
    
# Méthode qui va servir à déchiffrer le message

def dechiffrervigenere():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    listalpha2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    cryptlist = []
    count= -1

    listalpha1 = list (a)

    # On choisis la clef

    print("Choisissez la clef ! ")
    while True:
        try:
            clef = str(input("Clef : "))
            break
        except ValueError:
            print("Pas de chiffres !")
    clef = "".join(re.split("[^a-zA-Z]*", clef))
    listclef = list (clef.upper())
    print("Clef confirmé : " + str(clef))

    # On choisis le message à déchiffrer

    print("Quel est le message à déchiffrer ?")
    while True:
        try:
            message = str(input("Message : "))
            break
        except ValueError:
            print("Pas de chiffres !")
    message = "".join(re.split("[^a-zA-Z]*", message))
    listmess = list (message.upper())

    # La clef va prendre exactement la même taille que le message

    if len(listclef) < len(listmess):
        while len(listclef) < len(listmess):
            listclef += listclef

        if len(listclef) > len(listmess):
            lenlistclef = len(listclef)
            lenlistmess = len(listmess)
            x = lenlistclef - lenlistmess
            listclef = listclef[ : -x]
    
    elif len(listclef) > len(listmess):
        lenlistclef = len(listclef)
        lenlistmess = len(listmess)
        x = lenlistclef - lenlistmess
        listclef = listclef[ : -x]

    # On récupère l'index de chaque lettre de la clef

    listclef2 = []
    for i in listclef:
        for x in listalpha1:
            if i == x:
                indlistclef = listalpha1.index(x)
                listclef2.append(indlistclef)

    # On récupère l'index de chaque lettre du message

    listmess2 = []
    for j in listmess:
        for y in listalpha1:
            if j == y:
                indlistmess = listalpha1.index(y)
                listmess2.append(indlistmess)

    # On soustrait pour chaque lettre l'index du message à l'index de la clef

    finallist = [listmess2[i]-listclef2[i] for i in range(min(len(listclef2),len(listmess2)))]+max(listclef2,listmess2,key=len)[min(len(listclef2),len(listmess2)):]

    # On évite de dépasser 26 (pour les 26 lettres de l'alphabet)

    for i in finallist:
        count += 1
        if i < 0:
            finallist[count] = finallist[count] + 26
    
    # Et enfin, on fait correspondre les indices à l'alphabet traditionnel non transformé, afin d'obtenir le message chiffré

    for i in finallist:
        for j in listalpha2:
            if i == j:
                var = i
                indfinal = listalpha1[var]
                cryptlist.append(indfinal)

    messcrypt = ''.join(cryptlist)
    print(messcrypt)

# Centre de commande du programme, duquel on va choisir quelle fonction lancer

choix = 0

while True :
    print("Quel méthode de chiffrement souhaitez-vous utiliser ?")
    print("-1- César")
    print("-2- Vigenère")
    print("-3- Exit")
    while True:
        try:
            choix = int(input("Choix : "))
            break
        except ValueError:
            print("Entrez un chiffre !")
    if choix == 1:
        while True :
            print("--------Code de César--------")
            print("Que souhaitez-vous faire ? Tapez le chiffre correspondant :")
            print("-1- Chiffrer")
            print("-2- Déchiffrer")
            print("-3- Retour")
            while True:
                try:
                    choix = int(input("Choix : "))
                    break
                except ValueError:
                    print("Entrez un chiffre !")

            if choix == 1:
                chiffrercesar()
            elif choix == 2:
                dechiffrercesar()
            elif  choix == 3:
                break
    elif choix == 2:
        while True :
            print("--------Vigenère--------")
            print("Que souhaitez-vous faire ? Tapez le chiffre correspondant :")
            print("-1- Chiffrer")
            print("-2- Déchiffrer")
            print("-3- Retour")
            while True:
                try:
                    choix = int(input("Choix : "))
                    break
                except ValueError:
                    print("Entrez un chiffre !")

            if choix == 1:
                chiffrervigenere()
            elif choix == 2:
                dechiffrervigenere()
            elif  choix == 3:
                break
    elif  choix == 3:
        print("A bientôt")
        break