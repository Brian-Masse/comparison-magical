from numpy import disp
import pygame
import random
import math

pygame.init()

width = 500
height = 500
padding = 20

display = pygame.display.set_mode( ( width + padding, height + padding) )
running = True

scale = 1

series_data = [ 10, 50, 30, 5, 5 ]
# series = len(series_data)

def fill_background():
    for x in range(0, width + padding):
        pygame.draw.line(display, (255,255,255), (x, 0), (x, height + padding) )


def transform_series():
    returning = []
    for serie in series_data:
        data = ( serie, (serie / 100) * (360 * (width / 2)))
        returning.append(data)
    return returning

formatted_series = transform_series()

def draw_circle(scale):
    series = 0
    start_angle = 0
    color = (255, 0, 0)
    
    for i in range(0, int(360 * (width / 2) )):

        draw_line(i, color, scale)

        if (i - start_angle) > formatted_series[series][1]:
            series += 1
            start_angle = i
            color = ( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    start = 0
    for serie in formatted_series:
        draw_line(start, (0,0,0), scale, 5,)
        start += serie[1]
        # draw_line(start_angle, (0,0,0), 4)

def draw_line(angle, color, scale, thickness=2):
    scaled_index = angle / (width / 2)

    x = math.cos( (scaled_index * math.pi) / 180 ) * (width / 2)
    y = math.sin( (scaled_index * math.pi) / 180 ) * (height / 2)

    x *= scale
    y *= scale

    x += (width / 2) + (padding / 2)
    y += (height / 2) + (padding / 2)
    
    pygame.draw.line(display, color, (x, y), (width / 2, height / 2), max(1,int(thickness * scale))) 
    pygame.draw.circle(display, (0,0,0), (x + 1, y + 1),  max(1,int(2 * scale)))



fill_background()
draw_circle(1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 61:
                scale *= 2
                fill_background()
                draw_circle(scale)
            if event.key == 45:
                scale /= 2
                fill_background()
                draw_circle(scale)
                
    pygame.display.flip()    
    

pygame.quit()