import pygame,time

speedx = 10
speedy = 10
pop = [600, 800]
e = pygame.display.set_mode(pop)

kakashka_ubiyca = pygame.Rect(0,700,600,100)
w = pygame.Rect(200, -200, 200, 200)
while 1 == 1:
    time.sleep(1/60)
    # управление
    u = pygame.event.get()
    for s in u:
        if s.type == pygame.QUIT:
            exit()

    # движение
    w.y = w.y + speedy
    if w.bottom > 800:
        w.y=900


    # рисование
    pygame.draw.rect(e, [255, 155, 55], w)
    pygame.draw.rect(e, [110,64, 21], kakashka_ubiyca)
    pygame.display.flip()
    e.fill([44,44,44])
