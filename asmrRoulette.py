import pygame
import random as r
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60

NUMBER_OF_CLIPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = myfont.render('Welcome to ASMR Roulette!',False,(WHITE))
textunder = myfont.render('Press space and try your luck!',False,(WHITE))

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('testing your luck...')
                song = r.randint(1,NUMBER_OF_CLIPS)
                pygame.mixer.music.load(str(song)+'.mp3')
                pygame.mixer.music.play(0)

    screen.fill((255,0,230))
    screen.blit(textsurface,(100,100))
    screen.blit(textunder,(100,150))
    pygame.display.update()
