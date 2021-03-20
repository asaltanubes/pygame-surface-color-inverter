from pygame import Surface
from pygame.mask import Mask
from pygame.math import Vector2
from pygame.locals import BLEND_RGB_SUB, BLEND_RGB_MIN, BLEND_RGB_MAX

flag = {'sub': BLEND_RGB_SUB, 'min': BLEND_RGB_MIN, 'max': BLEND_RGB_MAX}

def invert_color(surface, mask = None, rel_pos = (0, 0), color = (255, 255, 255)):
    if mask == None:
        new_surf = Surface(surface.get_size())
        new_surf.fill(color)
        new_surf.blit(surface, (0, 0), special_flags =  flag['sub'])
        return new_surf
    mask = mask.copy()
    surf_size = surface.get_size()
    black_surf = Surface(surf_size)


    not_inverted_surf = Surface(surf_size)
    not_inverted_surf.fill((255, 255, 255))
    not_inverted_surf.blit(mask, rel_pos, special_flags = flag['sub'])

    if color != (255, 255, 255):
        colored_surf = Surface(mask.get_size())
        colored_surf.fill(color)
        mask.blit(colored_surf, (0, 0), special_flags = flag['min'])

    black_surf.blit(mask, rel_pos)

    not_inverted_surf.blit(surface, (0, 0), special_flags = flag['min'])
    black_surf.blit(surface, (0, 0), special_flags = flag['sub'])

    black_surf.blit(not_inverted_surf, (0, 0), special_flags =  flag['max'])
    return black_surf
