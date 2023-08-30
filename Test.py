from pygame import *
from random import randint

print((1 + 1) / 2)

# Juego: Bloques e Interruptores
# El juego entero está hecho de bloques que alternan de muchas formas:
# 1. Con Música
# 2. Con Interruptores (Principal)
# 3. Con puntos difíclies de alcanzar

# Clases
class GeneralSprite(sprite.Sprite):
    def __init__(self, imageni, sizex, sizey, posx=0, posy=0, sy=0, sx=0, limit=False):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imageni), (sizex, sizey))
        self.rx = posx
        self.ry = posy
        self.tx = sizex
        self.ty = sizey
        self.sx = sx
        self.sy = sy
        self.lm = limit
    def reset(self):
        Vind.blit(self.image,(self.rx, self.ry))

class Main(GeneralSprite):
    def function(self):
        if self.ry < Hg - self.ty / 2:
            self.sy -= 1
        
        Key = key.get_pressed()
        if Key[K_UP] and self.lm == False: 
            if self.ry > 0:
                self.sy = 20
            self.lm = True
        elif not Key[K_UP]:
            self.lm = False
        
        if self.ry < 1:
            self.ry = 1
            self.sy = 0
        elif self.ry > Hg - self.ty / 2:
            self.ry = (Hg - self.ty / 2) - 1
            self.sy = 0
        self.ry -= self.sy

# Ventana
Wd = 800
Hg = 600
Vind = display.set_mode((Wd, Hg))
display.set_caption("Help")
Tick = time.Clock()
Vond = transform.scale(image.load("Forrest.png"),(Wd, Hg)) 

# Objetos
Qaltanín = Main("Switch.png", 40, 40, 380, 180)

# Variables
FPS = 60
Loop = True
Game = True

#Ciclo de Juego
while Game:
    Vind.blit(Vond,(0,0)) #* Debe ir primero / Must go first
    if Loop:
        Qaltanín.function()
    Qaltanín.reset()
    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    Tick.tick(FPS)