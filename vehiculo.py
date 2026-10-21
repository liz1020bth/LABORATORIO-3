
class Sensor:
    # Atributo de clase
    tipo = "Genérico"

    def __init__(self, id):
        # Atributos de instancia
        self.id = id
        self.encendido = False

    def activar(self):
        self.encendido = True
        print(f"Sensor {self.id} activado.")

    def desactivar(self):
        self.encendido = False
        print(f"Sensor {self.id} desactivado.")


class Camara(Sensor):
    # Atributo de clase
    tipo = "Cámara"

    def __init__(self, id, resolucion):
        # Inicializar directamente la clase Sensor
        Sensor.__init__(self, id)
        self.resolucion = resolucion


class SensorLuzLaser(Sensor):
    # Atributo de clase
    tipo = "Luz Laser"

    def __init__(self, id, alcance):
        # Inicializar directamente la clase Sensor
        Sensor.__init__(self, id)
        self.alcance = alcance


class VehiculoAutonomo(Camara, SensorLuzLaser):
    # Atributo de clase
    tipo = "Vehículo Autónomo"

    def __init__(self, id, resolucion, alcance):
        # Inicializar los atributos de Sensor
        Sensor.__init__(self, id)

        # Atributos de las dos clases heredadas
        self.resolucion = resolucion
        self.alcance = alcance


# Programa principal
if __name__ == "__main__":
    vehiculo = VehiculoAutonomo("VA001", "4K", 200)

    print("=== VEHÍCULO AUTÓNOMO ===")
    print("Tipo:", vehiculo.tipo)
    print("ID:", vehiculo.id)
    print("Resolución:", vehiculo.resolucion)
    print("Alcance:", vehiculo.alcance)
    print("Encendido:", vehiculo.encendido)

    print("\n=== ACTIVAR SENSOR ===")
    vehiculo.activar()
    print("Encendido:", vehiculo.encendido)

    print("\n=== DESACTIVAR SENSOR ===")
    vehiculo.desactivar()
    print("Encendido:", vehiculo.encendido)
