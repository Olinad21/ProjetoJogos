import pygame
from pygame.locals import *
import random

class Recs(object):
    def __init__(self, numeroInicial):
        self.lista = []
        for x in range (numeroInicial):
            leftrandom = random.randrange(2, 560)
            toprandom = random.randrange(-580, -10)
            width = random.randrange(10,30,)
            height = random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))
                            
			
    def mover(self):
        for retangulo in self.lista:
            retangulo.move_ip(0,2)
                    
    def cor(self,superficie):
        for retangulo in self.lista:
            pygame.draw.rect(superficie, (165,214,254),retangulo)
                    
    def recriar(self):
        for x in range(len(self.lista)):
            if self.lista[x].top > 481:
                score = score + 1
                leftrandom = random.randrange(2, 560)
                toprandom = random.randrange(-580, -10)
                width = random.randrange(10,30,)
                height = random.randrange(15,30)
                self.lista[x] = (pygame.Rect(leftrandom,toprandom,width,height))
    
	
class Player(pygame.sprite.Sprite):
    
        
                    
    def __init__(self,img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.top,self.rect.left = (300,200)
                            
                            
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
                            
    def update(self,superficie):
        superficie.blit(self.img,self.rect)
                            
			
def colisao(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
        return False
	
def main():
    import pygame
    pygame.init()		
    tela = pygame.display.set_mode((480,300))
    sair = False
    relogio = pygame.time.Clock()
    img_nav = pygame.image.load("img/brick.png").convert_alpha()
    jogador = Player(img_nav)
	
    img_fundo = pygame.image.load("img/alien1.png").convert_alpha()
    img_explosao = pygame.image.load("img/explosion1.gif").convert_alpha()
	
    pygame.mixer.music.load("sounds/punch.wav")
    pygame.mixer.music.play(3)
	
    som_explosao = pygame.mixer.Sound("sounds/boom.wav")
    som_mov = pygame.mixer.Sound("sounds/punch.wav")
	
    vx,vy =0,0
    velocidade = 10
    leftpress,rightpress, uppress, downpress = False,False,False,False
    texto = pygame.font.SysFont("Arial",15,True,False)
	
    score = 0
    ret = Recs(30)
    colidiu = False
	
    while sair !=True:
      for event in pygame.event.get():
        if  event.type == QUIT:
            sair  = True            
            pygame.quit()
        if colidiu == False:
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    leftpress = True
                    vx = - velocidade
                        
                    if event.key ==pygame.K_RIGHT:
                        rightpress = True
                        vx = velocidade
                        
                    if event.key ==pygame.K_UP:
                        uppress = True
                        vy = -velocidade
                        
                    if event.key ==pygame.K_UP:
                        uppress = True
                        vy = -velocidade
                        som_mov.play()
                                        
                    if event.key ==pygame.K_DOWN:
                        downpress = True
                        vy = velocidade
                                        
                    if event.type == pygame.KEYUP:
                        downpress = False
                        if uppress: vx = - velocidade
                        vy= 0

            if colisao(jogador, ret):

                colidiu = True
                jogador.img = img_explosao
                pygame.mixer.music.stop()
                som_explosao.play()
                    
            if colidiu == False:
                ret.mover()
                jogador.mover(vx,vy)
                    
                tela.blit(img_fundo,(0,0))
                seg = pygame.time.get_ticks()/1000
                seg = str(seg)
                contador = texto.render("Pontuação:{}".format(seg),0,(255,255,255))
                tela.blit(contador,  (320,10))
                    
            relogio.tick(20)
            ret.cor(tela)
            ret.recriar()
            jogador.update(tela)

            pygame.display.update()
                    
        pygame.quit()
main()
