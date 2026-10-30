
import random
xogador1 = input("Introduce o teu nome: ")
puntos1 = 0
secreto = random.randint(1, 4)
for secreto in range(4):
    import random
    secreto = random.randint(1, 4)
    if secreto == 1:
        print("🍇")
        puntos1 += 1
    elif secreto == 2:
        print("🍉")
        puntos1 += 2
    elif secreto == 3:
        print("🍒")
        puntos1 += 3 
    elif secreto == 4:
        print("🍋")
        puntos1 += 4
print(puntos1)

xogador2 = input("Introduce o teu nome: ")
puntos2 = 0
secreto = random.randint(1, 4)
for secreto in range(4):
    import random
    secreto = random.randint(1, 4)
    if secreto == 1:
        print("🍇")
        puntos2 += 1
    elif secreto == 2:
        print("🍉")
        puntos2 += 2
    elif secreto == 3:
        print("🍒")
        puntos2 += 3 
    elif secreto == 4:
        print("🍋")
        puntos2 += 4
print(puntos2)

if puntos1 > puntos2:
    print("O xogador " + (xogador1) + " gañou con " + str(puntos1) + " puntos")
elif puntos2 > puntos1:
    print("O xogador " + (xogador2) + " gañou con " + str(puntos2) + " puntos")
elif puntos1 == puntos2:
    print("Empate! Ambos xogadores teñen " + str(puntos1) + " puntos")