import pygame, math, os
from colorinverter import invert_color
pygame.init()
img = 'images\\poro.jpg'
imgname = img.split('\\')[-1]
image = pygame.image.load(img)
# Create the window with the same size of the image
window = pygame.display.set_mode((image.get_size()))

#This will give us a circular surface of a given radious
def circle_surface(radius, color = (255, 255, 255)):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

# makes an inverted image and saves it
inverted_image = invert_color(image)
pygame.image.save(inverted_image, os.path.join('images', 'anti' + imgname))

# Some examples of other "anticolors"
inverted_image = invert_color(image, color = (0, 0, 255))
pygame.image.save(inverted_image, os.path.join('images', 'antiblue' + imgname))

inverted_image = invert_color(image, color = (0, 255, 0))
pygame.image.save(inverted_image, os.path.join('images', 'antigreen' + imgname))

inverted_image = invert_color(image, color = (255, 0, 0))
pygame.image.save(inverted_image, os.path.join('images', 'antired' + imgname))

inverted_image = invert_color(image, color = (0, 255, 255))
pygame.image.save(inverted_image, os.path.join('images', 'anticyan' + imgname))

inverted_image = invert_color(image, color = (255, 255, 0))
pygame.image.save(inverted_image, os.path.join('images', 'antiyellow' + imgname))

inverted_image = invert_color(image, color = (255, 0, 255))
pygame.image.save(inverted_image, os.path.join('images', 'antipink' + imgname))

# Radious (in pixels) of the circle
radius = 25

while True:
    events = pygame.event.get()
    window.fill((0, 0, 0))

    # Invert the image color using a circle with the center controlled by the mouse
    mx, my = pygame.mouse.get_pos()
    circle = circle_surface(radius)
    surf = invert_color(image, circle, (mx - radius, my - radius))


    window.blit(surf, (0, 0))


    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
