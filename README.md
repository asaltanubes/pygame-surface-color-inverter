#Pygame surface color inverter
This module includes 1 functions that inverts the color of a given surface.

```python
invert_color(surface, mask = None, rel_pos = (0, 0), color = (255, 255, 255)) -> pygame.Surface
```
surface : the surface we want to inverts

mask : this mask (or surface) contains the pixels that will be changed (in case of the surface the changed pixels will be white while the non changed will be black) if no mask is passed the whole image will be inverted

rel_pos : the position of the mask relative to the Surface

color : the "anticolor" that will be used
