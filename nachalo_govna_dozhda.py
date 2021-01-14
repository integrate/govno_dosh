import pygame, time, p_o_m_o_s_h

pygame.init()
tyu = int(600 / 60)
pygame.key.set_repeat(tyu)
speedy_kaka_1 = 7
speedy_kaka_2 = 5
pop = [600, 800]

e = pygame.display.set_mode(pop)

kakashka_ubiyca = pygame.Rect(0, 800, 600, 100)
kaka_1 = pygame.Rect(450, -200, 150, 150)
kaka_2 = pygame.Rect(150, -200, 150, 150)
tualet = pygame.Rect(300, 600,200, 200)
kartinka_tualeta = pygame.image.load("govno_kartinke/ff.jpeg")
kartinka_kaki = pygame.image.load("govno_kartinke/kk.jpeg")
kartinka_kaki = p_o_m_o_s_h.izmeni_kartinku(kartinka_kaki, 150, 150, [255, 255, 255], 10)
kartinka_tualeta = p_o_m_o_s_h.izmeni_kartinku(kartinka_tualeta, 200, 200, [16, 16, 16], 20)
# kartinka_unitaza=pygame.image.load("govno_kartinke/ff.jpeg")
while 1 == 1:
    time.sleep(1 / 60)
    # управление
    u = pygame.event.get()
    for s in u:
        if s.type == pygame.QUIT:
            exit()

        if s.type == pygame.KEYDOWN and s.key == pygame.K_a:
            tualet.x = tualet.x - 10

        if s.type == pygame.KEYDOWN and s.key == pygame.K_d:
            tualet.x = tualet.x + 10
    # движение tualeta
    tualet.bottom = kakashka_ubiyca.y
    # движение kaki 1
    kaka_1.y = kaka_1.y + speedy_kaka_1
    if kakashka_ubiyca.y < kaka_1.bottom:
        kaka_1.y = 0
        kakashka_ubiyca.y -= 10
        kakashka_ubiyca.h += 10
    # движение kaki 2
    kaka_2.y = kaka_2.y + speedy_kaka_2
    if kakashka_ubiyca.y < kaka_2.bottom:
        kaka_2.y = 0
        kakashka_ubiyca.y -= 10
        kakashka_ubiyca.h += 10

    if tualet.right > 600:
        tualet.right =600

    if tualet.left < 0:
        tualet.left =0
    le = tualet.colliderect(kaka_1)
    ll=tualet.colliderect(kaka_2)
    if ll==1:
        print("Поймал левую")
    if le==1:
        print("Поймал правую")
    # рисование
    e.blit(kartinka_kaki, kaka_1)
    e.blit(kartinka_kaki, kaka_2)
    # pygame.draw.rect(e,[255,255,255],tualet)
    e.blit(kartinka_tualeta, tualet)
    pygame.draw.rect(e, [110, 64, 21], kakashka_ubiyca)
    pygame.display.flip()
    e.fill([44, 44, 44])
