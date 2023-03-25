from sensor import Sensor
from demo_mongodb_test import ConexionMongo
import datetime
from myjson import Json

class Menu:
    def __init__(self) -> None:
        pass

    def interfaze(self):
        print("╔═════════════════════════════════╗")
        print("║          Menu Principal         ║")
        print("╠═════════════════════════════════╣")
        print("║ a) Insertar Sensor              ║")
        print("║ b) Leer datos                   ║")
        print("║ c) Subir Datos                  ║")
        print("║ d) Leer Sensores                ║")
        print("║ e) Recargar Sensores            ║")
        print("║ f) LED                          ║")
        print("║ x) Salir                        ║")
        print("╚═════════════════════════════════╝")
        op = input("Elige una opcion: ")
        if op == "a":
            self.insertarSensor()
        elif op == "b":
            self.leerDatos()
        elif op == "c":
            self.subirDatos()
        elif op == "d":
            Sensor.mostrarSensores()
        elif op == "e":
            self.cargarSensores()
        elif op == "f":
            Sensor.led()
        elif op == "x":
            exit()
        else:
            print("Opcion no valida")

    def insertarSensor(self):
        id = input("Escribir id: ")
        nombre = input("Escribir nombre: ")
        tipo = self._tipoSensor()
        op = "s"
        cont = 0
        pines = []
        while op != "n":
            pines.append(int(input("Escribir el pin: ")))
            op = input("Desea agregar otro pin? s/n: ")
            cont += 1
            if cont == 2 or op != "s":
                break
        ubicacion = input("Escribir ubicacion: ")
        descripcion = input("Escribir descripcion: ")
        fecha = str(datetime.datetime.now())
        sensor = Sensor(id, nombre, tipo, ubicacion, descripcion, fecha, pines)
        conexion = ConexionMongo("Sensores", "SensoresInformacion")
        conexion.agregarCollection(sensor.__dict__)
        conexion.cerrarConexion()
        Sensor.guardarSensores()

    def _tipoSensor(self):
        print("╔════════════════════════════════════════╗")
        print("║   Elige el tipo de sensor que deseas   ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1) Corriente                           ║")
        print("║ 2) Sonido                              ║")
        print("║ 3) Flama                               ║")
        print("║ 4) Luz                                 ║")
        print("║ 5) Humo                                ║")
        print("║ 6) Presencia                           ║")
        print("║ 7) Temperatura                         ║")
        print("║ 8) Magnetico                           ║")
        print("║ 9) Ultrasonico                         ║")
        print("╚════════════════════════════════════════╝")
        op = input("Elige un tipo: ")
        if op == "1":
            return "corriente"
        elif op == "2":
            return "sonido"
        elif op == "3":
            return "flama"
        elif op == "4":
            return "luz"
        elif op == "5":
            return "humo"
        elif op == "6":
            return "presencia"
        elif op == "7":
            return "temperatura"
        elif op == "8":
            return "magnetico"
        elif op == "9":
            return "ultrasonico"
        else:
            print("Opcion no valida")
            return self._tipoSensor
        
    def leerDatos(self):
        Sensor.mandarDatos()
        Sensor.leerRaspberryPi()
    def subirDatos(self):
        Sensor.mandarDatos(15);
    def cargarSensores(self):
        json = Json('sensores.json')
        conexion = ConexionMongo("Sensores","SensoresInformacion")
        json.guardar(conexion.traerDatos())

if __name__ == '__main__':
    menu = Menu()
    while True:
        menu.interfaze()