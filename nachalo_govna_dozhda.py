import pygame,time,p_o_m_o_s_h

speedx = 10
speedy = 10
pop = [600, 800]
e = pygame.display.set_mode(pop)

kakashka_ubiyca = pygame.Rect(0, 800, 600, 100)
kaka_1 = pygame.Rect(450, -200, 150,150)
kaka_2 = pygame.Rect(150,-200,150, 150)
kartinka_kaki=pygame.image.load("govno_kartinke/kk.jpeg")
kartinka_kaki=p_o_m_o_s_h.izmeni_kartinku(kartinka_kaki,150,150,[255,255,255],10)
# kartinka_unitaza=pygame.image.load("govno_kartinke/ff.jpeg")
while 1 == 1:
    time.sleep(1/60)
    # управление
    u = pygame.event.get()
    for s in u:
        if s.type == pygame.QUIT:
            exit()

    # движение kaki 1
    kaka_1.y = kaka_1.y + speedy+5
    if kakashka_ubiyca.y<kaka_1.bottom:
        kaka_1.y=0
        kakashka_ubiyca.y-=10
        kakashka_ubiyca.h+=10
    # движение kaki 2
    kaka_2.y = kaka_2.y + speedy
    if kakashka_ubiyca.y<kaka_2.bottom:
        kaka_2.y = 0
        kakashka_ubiyca.y -= 10
        kakashka_ubiyca.h += 10
    # рисование
    e.blit(kartinka_kaki, kaka_1)
    e.blit(kartinka_kaki,kaka_2)
    # e.blit(kartinka_unitaza, kakashka_ubiyca)

    # pygame.draw.rect(e, [255, 155, 55], w)
    # pygame.draw.rect(e, [110,64, 21], kaka_2)

    pygame.draw.rect(e, [110,64, 21],kakashka_ubiyca)
    pygame.display.flip()
    e.fill([44,44,44])