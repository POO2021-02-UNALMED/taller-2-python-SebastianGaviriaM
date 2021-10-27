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
        if(tipo=="gasolina" or tipo=="electrico"):
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

    
