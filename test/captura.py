import wx
app = wx.App()


screen = wx.ScreenDC()
size = screen.GetSize()
bmp = wx.Bitmap(size[0], size[1])
mem = wx.MemoryDC(bmp)
mem.Blit(0,0,size[0], size[1], screen, 0, 0)
del mem
bmp.SaveFile("pantalla.png", wx.BITMAP_TYPE_PNG)
