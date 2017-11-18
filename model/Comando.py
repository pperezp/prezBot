class Comando:
    # Constructor
    def __init__(self, nombre, descripcion, mensaje, accion=None):
        self.nombre = nombre
        self.mensaje = mensaje
        self.descripcion = descripcion
        self.accion = accion

    # toString();
    def __str__(self):
        return "Comando:{nombre="+self.nombre+", descripcion="+self.descripcion+", mensaje="+self.mensaje+"}"