import pygame

pygame.init()

bgcolour = 0, 0, 0
linecolour = 255, 255, 255
width, height = 640, 250

def get_canvas():
    screen = pygame.display.set_mode((width, height))
    screen.fill(bgcolour)

    running = True
    current_pos = (0, 0)
    button_down = False
    should_be_drawing = False

    while running:
        event = pygame.event.wait()
        if event.type == pygame.NOEVENT:
            continue

        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                break
            current_pos = event.pos
            pygame.draw.circle(screen, linecolour, current_pos, 5)
            button_down = True
            should_be_drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if button_down and should_be_drawing:
                pygame.draw.line(screen, linecolour, current_pos, event.pos, 5)
            current_pos = event.pos
            should_be_drawing = button_down
            #pygame.draw.circle(screen, linecolour, event.pos, 5)
        elif event.type == pygame.MOUSEBUTTONUP:
            current_pos = event.pos
            should_be_drawing = False
            button_down = False

        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break

    # pygame.image.save(screen, fname)
    return screen.copy()

def draw():
    # Draw the head
    print("head!")
    h = get_canvas()

    # Then the body
    print("body!")
    b = get_canvas()

    print("legs!")
    l = get_canvas()
    return h, b, l


def stitch(h, b, l):
    screen = pygame.display.set_mode((width, height * 3))
    screen.blit(h, (0, 0))
    screen.blit(b, (0, height))
    screen.blit(l, (0, height * 2))
    pygame.display.update()


def wait():
    while pygame.event.wait().type != pygame.QUIT:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break

h, b, l = draw()
stitch(h, b, l)
wait()
