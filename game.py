import pygame
from PIL import Image


pygame.init()

bgcolour = 0, 0, 0
linecolour = 255, 255, 255
x = y = 0
screen = pygame.display.set_mode((640, 480))



def get_canvas(fname):
    running = True
    current_pos = (0, 0)
    button_down = False
    should_be_drawing = False
    screen.fill(bgcolour)

    while running:
        event = pygame.event.poll()
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

    pygame.image.save(screen, fname)

def draw():
    # Draw the head
    print("head!")
    get_canvas("head")

    # Then the body
    print("body!")
    get_canvas("body")


    get_canvas("legs")


def stitch():
    list_im = ['head','body','legs']
    new_im = Image.new('RGB', (640,480 * 3)) #creates a new empty image, RGB mode, and size 444 by 95

    for i, elem in enumerate(list_im):
        im=Image.open(elem)
        new_im.paste(im, (0, 480 * i))
    new_im.save('test.jpg')


draw()
stitch()
im = Image.open("test.jpg")
im.show()
