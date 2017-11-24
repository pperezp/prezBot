

class Acciones:
    @staticmethod
    def sacarFoto():
        from model.Bot import Bot
        Bot.enviarFoto()

    @staticmethod
    def pantallazo():
        from model.Bot import Bot
        Bot.enviarCaptura()

    @staticmethod
    def yt():
        from model.Bot import Bot
        Bot.enviarMp3("https://www.youtube.com/watch?v=9c5rDZOh4Fs")
