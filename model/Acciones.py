

class Acciones:
    @staticmethod
    def sacarFoto():
        from model.Bot import Bot
        Bot.enviarFoto()

    @staticmethod
    def pantallazo():
        from model.Bot import Bot
        Bot.enviarCaptura()