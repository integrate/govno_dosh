import pygame, time, p_o_m_o_s_h

pygame.init()
tyu = int(600 / 60)
pygame.key.set_repeat(tyu)
speedy_kaka_1 = 10
speedy_kaka_2 = 7
pop = [600, 800]
proigral=0
e = pygame.display.set_mode(pop)

kakashka_ubiyca = pygame.Rect(0, 800, 600, 100)
kaka_1 = pygame.Rect(450, -200, 100, 100)
kaka_2 = pygame.Rect(150, -200, 100, 100)
tualet = pygame.Rect(300, 600, 200, 200)
kartinka_tualeta = pygame.image.load("govno_kartinke/ff.jpeg")
kartinka_kaki = pygame.image.load("govno_kartinke/kk.jpeg")
kartinka_kaki = p_o_m_o_s_h.izmeni_kartinku(kartinka_kaki, 100, 100, [255, 255, 255], 10)
kartinka_tualeta = p_o_m_o_s_h.izmeni_kartinku(kartinka_tualeta, 200, 200, [16, 16, 16], 20)
# kartinka_unitaza=pygame.image.load("govno_kartinke/ff.jpeg")
nomer = pygame.event.custom_type()
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
        if s.type == nomer:
            exit()
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

    if kakashka_ubiyca.h > 800:
        kakashka_ubiyca.h = 0
        kakashka_ubiyca.y = 800
        proigral=1
        speedy_kaka_1 = 0
        speedy_kaka_2 = 0
        pygame.time.set_timer(nomer, 5000, True)



    if tualet.right > 600:
        tualet.right = 600

    if tualet.left < 0:
        tualet.left = 0

    ll = tualet.colliderect(kaka_1)
    le = tualet.colliderect(kaka_2)
    if ll == 1:
        print("Поймал левую")
        kaka_1.y = -200
    if le == 1:
        print("Поймал правую")
        kaka_2.y = -200
    if ll>0:
        e.blit(schet_ochkov_poymaneh_kakashek_kartinka,[0,0])

        schet_ochkov_poymaneh_kakashek_kartinka = p_o_m_o_s_h.schet_ochkov_poymaneh_kakashek.render("1 РАУНД: 0 ПОЙМАНЫЕ_КАКАШКИ",True,[56,66,66])


    # рисование
    e.blit(kartinka_kaki, kaka_1)
    e.blit(kartinka_kaki, kaka_2)
    # pygame.draw.rect(e,[255,255,255],tualet)
    e.blit(kartinka_tualeta, tualet)
    pygame.draw.rect(e, [110, 64, 21], kakashka_ubiyca)
    if proigral!=0:
        p_o_m_o_s_h.narisue_bukvu(e, [0, 0, 0, 0])
    p_o_m_o_s_h.schet_ochkov(e, [255,55,77])

    pygame.display.flip()
    e.fill([44, 44, 44])
