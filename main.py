# -*- coding: utf-8 -*-
"""
pip install python-telegram-bot --upgra
pip install wxPython
INSTALAR openCV para cv2    

https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#send-a-chat-action

"""

import telegram
from telegram.ext import *
from cv2 import *
import time

rutaFotos = "/home/pi/prezBot/prezBot/"
nombreFoto = "captura.jpg"

bot         = telegram.Bot(token="")
bot_updater = Updater(bot.token)
dispatcher  = bot_updater.dispatcher

def enviarMensaje(bot, id, mensaje):
    bot.send_chat_action(chat_id=id, action=telegram.ChatAction.TYPING)
    bot.sendMessage(
        chat_id=id,
        text="["+time.strftime("%H:%M:%S")+"] "+mensaje
    )

def enviarFoto(bot, id):
    #bot.send_photo(chat_id=id, photo='https://telegram.org/img/t_logo.png')

    # initialize the camera
    cam = VideoCapture(0)  # 0 -> index of camera
    s, img = cam.read()
    if s:  # frame captured without any errors

        imwrite(nombreFoto, img)  # save image

        bot.send_chat_action(chat_id=id, action=telegram.ChatAction.UPLOAD_PHOTO)
        bot.send_photo(chat_id=id, photo=open(rutaFotos+nombreFoto, 'rb'))

def enviarCaptura(bot, id):
    import wx
    app = wx.App()

    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.Bitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem
    bmp.SaveFile("pantalla.png", wx.BITMAP_TYPE_PNG)

    bot.send_chat_action(chat_id=id, action=telegram.ChatAction.UPLOAD_PHOTO)
    bot.send_photo(chat_id=id, photo=open("pantalla.png", 'rb'))


def listener(bot, update):
    mensaje = update.message.text
    id = update.message.chat_id

    print("ID: "+str(id) +" Mensaje:"+mensaje)

    if "hora" in mensaje.lower():
        enviarMensaje(bot, id, time.strftime("%H:%M:%S"))

    if "gracias" in mensaje.lower():
        enviarMensaje(bot, id, "De nada! 👍🏻")

    if "foto" in mensaje.lower():
        enviarFoto(bot, id)

    if "captura" in mensaje.lower():
        enviarCaptura(bot, id)
    
    if "temp" in mensaje.lower():
        bashCommand = "/opt/vc/bin/vcgencmd measure_temp"
        import subprocess
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        #print(output.strip().split("=")[1].split("'")[0]+" Cº")
        enviarMensaje(bot, id, output.strip().split("=")[1].split("'")[0]+" Cº")

def start(bot, update, pass_chat_data=True):
    id = update.message.chat_id
    bot.sendMessage(chat_id=id, text="Gracias por hablarme!")


start_handler = CommandHandler("hola", start)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)

bot_updater.start_polling()
bot_updater.idle()

while True:
    pass
