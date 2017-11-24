import telegram
import time
import wx
from telegram.ext import *
from model.Comandos import Comandos
from cv2 import *
from os import remove

class Bot:
    @staticmethod
    def init():
        Comandos.init()
        Bot.bot = telegram.Bot(token="480148406:AAEfcvXjrEbGuQpgBSy3j0w7j9_LJo2iiAE")
        Bot.bot_updater = Updater(Bot.bot.token)
        Bot.dispatcher = Bot.bot_updater.dispatcher

        start_handler = CommandHandler("start", Bot.start)
        listener_handler = MessageHandler(Filters.text, Bot.listener)
        Bot.dispatcher.add_handler(start_handler)
        Bot.dispatcher.add_handler(listener_handler)

        Bot.bot_updater.start_polling()
        print("Bot iniciado!")
        Bot.bot_updater.idle()
        print("Bot iniciado!")
    # Método que se llama cuando el usuario pone /start
    @staticmethod
    def start(bot, update, pass_chat_data=True):
        Bot.id = update.message.chat_id
        Bot.enviarMensaje(Comandos.print())

    @staticmethod
    def listener(bot, update):
        try:
            mensaje = update.message.text
            Bot.id = update.message.chat_id
            print("ID: " + str(Bot.id) + " Mensaje:" + mensaje)

            c = Comandos.get(mensaje)

            if "youtube" in mensaje or "youtu.be" in mensaje:
                Bot.enviarMp3(mensaje)
            elif c is None:
                Bot.enviarMensaje("Comando no encontrado")
                Bot.enviarMensaje(Comandos.print())
            elif c.accion is None:
                Bot.enviarMensaje(c.mensaje)
            else:
                c.accion()
        except BaseException as b:
            print(str(b))

    @staticmethod
    def enviarMensaje(mensaje):
        Bot.bot.send_chat_action(
            chat_id=Bot.id,
            action=telegram.ChatAction.TYPING
        )
        Bot.bot.sendMessage(
            chat_id=Bot.id,
            text="[" + time.strftime("%H:%M:%S") + "] " + mensaje
        )

    @staticmethod
    def enviarFoto():
        nombreFoto = "captura.jpg"
        try:
            # bot.send_photo(chat_id=id, photo='https://telegram.org/img/t_logo.png')

            # initialize the camera
            cam = VideoCapture(0)  # 0 -> index of camera
            s, img = cam.read()
            if s:  # frame captured without any errors
                imwrite(nombreFoto, img)  # save image

                Bot.bot.send_chat_action(chat_id=Bot.id, action=telegram.ChatAction.UPLOAD_PHOTO)
                Bot.bot.send_photo(chat_id=Bot.id, photo=open(nombreFoto, 'rb'))
        except BaseException as e:
            Bot.enviarMensaje("Error! lo siento " + str(e))

    @staticmethod
    def enviarCaptura():
        try:
            app = wx.App()

            screen = wx.ScreenDC()
            size = screen.GetSize()
            bmp = wx.Bitmap(size[0], size[1])
            mem = wx.MemoryDC(bmp)
            mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
            del mem
            bmp.SaveFile("pantalla.png", wx.BITMAP_TYPE_PNG)

            Bot.bot.send_chat_action(chat_id=Bot.id, action=telegram.ChatAction.UPLOAD_PHOTO)
            Bot.bot.send_photo(chat_id=Bot.id, photo=open("pantalla.png", 'rb'))
        except BaseException as e:
            Bot.enviarMensaje("Error! lo siento " + str(e))
            # self.bot.send_photo(chat_id=self.id, photo='https://telegram.org/img/t_logo.png')

    @staticmethod
    def enviarMp3(url, persistencia=True):
        from model.Youtube import Youtube

        Bot.enviarMensaje("Se esta descargando el video. Sea paciente por favor...")
        archivo = Youtube.getMp3(url)+".mp3"

        Bot.enviarMensaje("Video descargado! se esta enviando el mp3...")

        Bot.bot.send_chat_action(chat_id=Bot.id, action=telegram.ChatAction.UPLOAD_AUDIO)
        Bot.bot.send_audio(chat_id=Bot.id, audio=open(archivo, 'rb'))

        if not persistencia:
            remove(archivo)