class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self, color):
        if(color=="rojo" or color=="amarillo" or color=="verde" or color=="negro"):
            self.color=color
    

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo=tipo
        self.registro=registro


    def cambiarRegistro(self, registro):
        self.registro=registro


    def asignarTipo(self, tipo):
        if(tipo=="gasolina" or tipo=="eléctrico"):
            self.tipo = tipo








class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):

        cantidad=0
        for i in self.asientos:
            if(i==None):
                continue
            cantidad=cantidad+1
        return cantidad

    def verificarIntegridad(self):
        
        original=True

        if(self.motor.registro!=self.registro):
            original=False
        
        for i in self.asientos:
            if(i!=None):
                if(i.registro!=self.registro):
                    original=False
        
        if(original):
            return "Auto original"
        else:
            return "Las piezas no son originales"

    




# cantidadCreados es un atributo de clase
# - El método de instancia cantidadAsientos() retornara la cantidad de asientos que
# efectivamente sean objetos Asiento en la lista del objeto Auto.
# - El método verificarIntegridad(), se encargara de revisar que el atributo registro
# de Motor, Auto y Cada Asiento sean el mismo, esto para ir en contra de la
# piratería de piezas. En caso de encontrar que un Asiento, el Auto o el Motor
# tiene un registro diferente al de los demás retornara el mensaje “Las piezas no
# son originales” en caso contrario, retornara “Auto original”
