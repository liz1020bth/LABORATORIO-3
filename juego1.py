
import random


class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.vidasIniciales = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1

        if self.numeroDeVidas > 0:
            return True
        else:
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("\n================================")
        print("     JUEGO: ADIVINA EL NUMERO")
        print("================================")
        print("Adivina un numero entre 0 y 10")
        print("Tienes", self.numeroDeVidas, "vidas")
        print()

        while self.numeroDeVidas > 0:
            try:
                numero = int(input("Introduce un numero: "))
            except ValueError:
                print("Error: introduce un numero entero.")
                continue

            if numero < 0 or numero > 10:
                print("El numero debe estar entre 0 y 10.")
                continue

            if numero == self.numeroAAdivinar:
                print("\nAcertaste!!")
                self.actualizaRecord()
                print("Partida terminada.")
                return

            self.quitaVida()

            if self.numeroAAdivinar > numero:
                print("El numero a adivinar es mayor.")
            else:
                print("El numero a adivinar es menor.")

            if self.numeroDeVidas > 0:
                print("Te quedan", self.numeroDeVidas, "vidas.")
                print("Intenta de nuevo.\n")

        print("\nYa no te quedan vidas.")
        print("El numero era:", self.numeroAAdivinar)


class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()


if __name__ == "__main__":
    Aplicacion.main()
