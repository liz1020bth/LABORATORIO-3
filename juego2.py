
import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.vidasIniciales = numeroDeVidas
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas

    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0


class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        return 0 <= numero <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        print("\n--- ADIVINA EL NUMERO ---")

        while self.numeroDeVidas > 0:
            try:
                numero = int(input("Introduce un numero del 0 al 10: "))
            except ValueError:
                print("Debes introducir un numero entero.")
                continue

            if not self.validaNumero(numero):
                print("Error: el numero debe estar entre 0 y 10.")
                continue

            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return

            quedanVidas = self.quitaVida()

            if self.numeroAAdivinar > numero:
                print("El numero a adivinar es mayor.")
            else:
                print("El numero a adivinar es menor.")

            if quedanVidas:
                print("Te quedan", self.numeroDeVidas, "vidas.")
            else:
                print("Perdiste. El numero era", self.numeroAAdivinar)


class JuegoAdivinaPar(JuegoAdivinaNumero):
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([0, 2, 4, 6, 8, 10])
        self._juegaConPista("PAR")

    def validaNumero(self, numero):
        if numero < 0 or numero > 10:
            print("Error: el numero debe estar entre 0 y 10.")
            return False

        if numero % 2 != 0:
            print("Error: debes introducir un numero par.")
            return False

        return True

    def _juegaConPista(self, tipo):
        print("\n--- ADIVINA EL NUMERO", tipo, "---")

        while self.numeroDeVidas > 0:
            try:
                numero = int(input("Introduce un numero del 0 al 10: "))
            except ValueError:
                print("Debes introducir un numero entero.")
                continue

            if not self.validaNumero(numero):
                continue

            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return

            quedanVidas = self.quitaVida()

            if self.numeroAAdivinar > numero:
                print("El numero a adivinar es mayor.")
            else:
                print("El numero a adivinar es menor.")

            if quedanVidas:
                print("Te quedan", self.numeroDeVidas, "vidas.")
            else:
                print("Perdiste. El numero era", self.numeroAAdivinar)


class JuegoAdivinaImpar(JuegoAdivinaPar):
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([1, 3, 5, 7, 9])
        self._juegaConPista("IMPAR")

    def validaNumero(self, numero):
        if numero < 0 or numero > 10:
            print("Error: el numero debe estar entre 0 y 10.")
            return False

        if numero % 2 == 0:
            print("Error: debes introducir un numero impar.")
            return False

        return True


class Aplicacion:
    @staticmethod
    def main():
        juegoNumero = JuegoAdivinaNumero(3)
        juegoPar = JuegoAdivinaPar(3)
        juegoImpar = JuegoAdivinaImpar(3)

        juegoNumero.juega()
        juegoPar.juega()
        juegoImpar.juega()


if __name__ == "__main__":
    Aplicacion.main()
