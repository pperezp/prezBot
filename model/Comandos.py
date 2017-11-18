from model.Comando import Comando

class Comandos:
    @staticmethod
    def init():
        Comandos.add(Comando("cmd1", "def1", "men1"))
        Comandos.add(Comando("cmd2", "def2", "men2"))
        Comandos.add(Comando("cmd3", "def3", "men3"))

    @staticmethod
    def add(comando):
        try:
            Comandos.lista.append(comando)
        except:
            # si cae en esta excepcion es porque no esta creada
            Comandos.lista = list()
            Comandos.lista.append(comando)

    @staticmethod
    def get(nombreComando):
        for c in Comandos.lista:
            if(c.nombre == nombreComando.lower()):
                return c

        return None

    @staticmethod
    def print():
        str = "Lista de comandos disponibles\n\n"
        for c in Comandos.lista:
            print(c)
            str += c.nombre + " - "+ c.descripcion + "\n"

        return str