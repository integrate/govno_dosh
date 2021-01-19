import pygame
pygame.init()
game_over = pygame.font.SysFont("arial", 50, True, False)


def izmeni_kartinku(kartinka, shirina, visota, uberi_cvet, porog):
    kartinka = pygame.transform.scale(kartinka, [shirina, visota])
    kartinka = kartinka.convert()
    m1 = pygame.mask.from_threshold(kartinka, uberi_cvet, [porog, porog, porog])
    m1.invert()
    q2 = kartinka.copy()
    q2.fill([0, 0, 0, 0])
    m1.to_surface(q2, kartinka, None, None, None)
    # q2.set_colorkey([0, 0, 0])
    return q2


def narisue_bukvu(screen,color):
    # нарисуй буквы gAme over
    game_over_kartinka=game_over.render("Game Over",True,color)
    screen.blit(game_over_kartinka,[150,400])