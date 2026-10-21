
class CriaturaMarina:
    def metodo1(self):
        print("criatura 1")

    def metodo2(self):
        print("criatura 2")

    def __str__(self):
        return "habita en el oceano"


class Mamifero(CriaturaMarina):
    def metodo1(self):
        print("sangre caliente")


class Delfin(Mamifero):
    def metodo1(self):
        print("sopla burbujas")

    def __str__(self):
        return "delfin"


class Calamar(CriaturaMarina):
    def metodo2(self):
        print("tentáculos")

    def __str__(self):
        return "calamar"


class Ballena(Mamifero):
    def metodo1(self):
        print("canta canciones")

    def __str__(self):
        return "ballena"

    def nadar(self):
        print("nada profundamente")


elementos = [
    Calamar(),
    Delfin(),
    Mamifero(),
    CriaturaMarina(),
    Ballena()
]

for i in range(len(elementos)):
    print(elementos[i])
    elementos[i].metodo1()
    elementos[i].metodo2()
    print()
