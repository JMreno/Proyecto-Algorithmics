
from pygame import *
from random import randint

print((1 + 1) / 3)

# Clases
class GeneralSprite(sprite.Sprite):
    def __init__(self, imageni, sizex, sizey, posx=0, posy=0, sy=0, sx=0, limit=False, var1=0, mode=0):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(imageni), (sizex, sizey))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.tx = sizex
        self.ty = sizey
        self.sx = sx
        self.sy = sy
        self.lm = limit
        self.v1 = var1
        self.mode = mode
    def reset(self):
        Vind.blit(self.image,(self.rect.x, self.rect.y))

class Main(GeneralSprite):
    def function(self):
        global Hel
        self.sx = self.sx * 0.7
        self.collidex(self.sx * 0.1)
        self.rect.x += round(self.sx)

        Key = key.get_pressed()
        if Key[K_LEFT] and self.rect.x > 0:
            self.collidex(-5)
        elif self.rect.x < 0:
            self.rect.x = Wd - self.tx
        elif self.rect.x > Wd - self.tx:
            self.rect.x = 0
        if Key[K_RIGHT]:
            self.collidex(5)

        if self.rect.y < Hg - self.ty / 2:
            self.sy -= 1
        #self.rect.y -= self.sy

        if Key[K_UP]: 
            if self.rect.y > 0 and self.v1 < 5:
                self.sy = 15
                if self.lm == False:
                    Palí.play()
            self.lm = True
        elif not Key[K_UP]:
            self.lm = False

        self.v1 += 1

        if self.rect.y < 1:
            self.rect.y = (Hg - self.ty / 2) + 1
            if Key[K_UP]:
                self.sy = 20
        elif self.rect.y > Hg - self.ty / 2:
            self.rect.y = 1
            if self.sy < -10:
                Hel -= 1
                Ouch.play()
            self.sy = 0
        self.collidey()

    def collidey(self):
        global Score
        global Hel
        self.rect.y -= self.sy
        if self.sy < 0 or self.v1 < 1:
            self.mode = 0
        else:
            self.mode = 1
        while sprite.spritecollide(Qaltanín, Blok, False):
            if self.mode == 0:
                if sprite.spritecollide(Qaltanín, Svitt, False):
                    generatestage()
                    Score += 1
                    if Hel < 3:
                        Hel += 1
                    Selc.play()
                self.rect.y -= 1
                self.sy = 1
                self.v1 = 0
                self.lm = False
            else:
                self.rect.y += 1
                self.sy = 1
            #self.lm = False

    def collidex(self, movex):
        
        self.sx += movex 
        self.sx = self.sx * 0.7 
        self.rect.x += round(self.sx)
        if self.sx < 0:
            self.mode = 0
        elif self.sx == 0:
            self.mode = 2
        else:
            self.mode = 1      
        while sprite.spritecollide(Qaltanín, Blok, False):
            if self.mode == 0:
                self.rect.x += 1
                self.sx = 0
            elif self.mode == 1:
                self.rect.x -= 1
                self.sx = 0

    def goback(self):
        self.rect.x = 380
        self.rect.y = 180
        self.sy = 0
        self.lm = 1
        self.v2 = 99
        while sprite.spritecollide(Qaltanín, Blok, False):
            self.rect.y -= 1

class Floori(GeneralSprite):
    def update(self):
        pass

    def ono(self, re):
        if sprite.spritecollide(re, Blok, True):
            self.kill()

class Svit(GeneralSprite):
    def update(self):
        pass

class Detector(GeneralSprite):
    def checktop(self, steps, re):
        self.rect.x -= 80
        self.rect.y -= 20
        for i in range(0, 5):
            for r in range(0,40):
                self.rect.y -= 1
                if sprite.spritecollide(re, Blok, True):
                    Collide = False
                    return Collide
            self.rect.y += 40
            self.rect.x += 40
        self.kill()

class Enemigo(GeneralSprite):
    def update(self):
        pass

# Ventana, Fuentes y Sonidos
Wd = 800
Hg = 600
Vind = display.set_mode((Wd, Hg))
display.set_caption("Help")
Tick = time.Clock()
Vond = transform.scale(image.load("Forrest.png"),(Wd, Hg)) 

mixer.init()
Palí = mixer.Sound("Palí.wav")
Ouch = mixer.Sound("Hit.wav")
Selc = mixer.Sound("Checkpoint_.wav")

font.init()
Fofo = font.SysFont("Bahnschrift", 50)
Losty = font.SysFont("Bahnschrift", 20)

# Grupos
Blok = sprite.Group()
Svitt = sprite.Group()

# Objetos y Animaciones
Qaltanín = Main("Bridgey.png", 40, 40, 380, 180)
AQ = ["Bridgey.png", "Floortest.png"]
#Switch = Svit("Switch.png", 40, 40, 380, 180)

def spriteset(px, py):
    Nipel = Floori("Floortest.png", 40, 40, px, py)
    Blok.add(Nipel)
    #Nipel.ono(Nipel)

def generatestage():
    Important = False
    while not Important:
        Blok.empty()
        Svitt.empty()
        for n in range(0,6):
            Aaa = n * 40
            spriteset(280 + Aaa, 300)
        for i in range(0,5):
            Posy = randint(0,3)
            Posx = randint(1,6)
            Type = randint(1,3)
            while Posx > 2 and Posx < 6 and Posy == 2:
                Posx = randint(1,6)
            while Posy < 1 and Type == 2:
                Posy = randint(0,3)
            if Type == 1:
                for c in range(0,3):
                    spriteset((Posx * 120) - (c * 40), Posy * 120 + 100)
            elif Type == 2:
                for c in range(0,3):
                    spriteset((Posx * 120) - (c * 40), (Posy * 120 + 100) - (c * 40))
            elif Type == 3:
                for c in range(0,3):
                    spriteset((Posx * 120) - (c * 40), (Posy * 120 + 100) + (c * 40))
            else:
                Nipel = Floori("Floortest.png", 40, 40, Posx * 120, Posy * 100 + 100, 0, 0)
                Blok.add(Nipel)
            Check = Detector("Switch.png", 10, 10, Posx * 120, Posy * 120 + 60, 0, 0)
        Collide = True
        if not Important:
            Check.checktop(120, Check)
            if Collide:
                Impo = Svit("Switch.png", 40, 40, Posx * 120, Posy * 120 + 60, 0, 0)
                Blok.add(Impo)
                spriteset(Posx * 120, Posy * 120 + 100)
                Svitt.add(Impo)
                Important = True
    Qaltanín.goback()

# Variables
FPS = 60
Loop = True
Game = True
Limit = False
Score = 0
#PerHel = 1
Hel = 1

#Generador de nivel
generatestage()

#Ciclo de Juego
while Game:
    Vind.blit(Vond,(0,0)) #* Debe ir primero / Must go first
    for e in event.get():
        if e.type == QUIT:
            Game = False
    if Loop:
        Blok.draw(Vind)
        Blok.update()
        Qaltanín.function()
        if Hel < 0:
            Hel = 0
            Loop = False
        #Key = key.get_pressed()
        #if Key[K_RETURN] and not Limit:
            #generatestage()
            #Limit = True
        #elif not Key[K_RETURN]:
            #Limit = False
        Qaltanín.reset()
        Scori = Fofo.render(str(Score), True, (55, 55, 55))
        Heli = Fofo.render(str(Hel), True, (44, 209, 77))
        Vind.blit(Scori, (60, 50))
        Vind.blit(Heli, (700, 50))
    else:
        Losto = Fofo.render("Has perdido...", True, (255, 200, 150))
        Comment = Losty.render("Presione la barra espaciadora para intentar de nuevo", True, (255, 200, 150))
        Vind.blit(Losto, (160, 230))
        Vind.blit(Comment, (160, 300))
        Key = key.get_pressed()
        if Key[K_SPACE]:
            generatestage()
            Loop = True
            Hel = 1
            Score = 0
    Tick.tick(FPS)
    display.update()