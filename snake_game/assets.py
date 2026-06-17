import pygame as pg
pg.init()

screen = pg.display.set_mode((800,600))
selected_mode = "regular"
intro_font = pg.font.Font('font.ttf',75)
menu_font = pg.font.Font('font.ttf',45)
text_font = pg.font.Font('font.ttf',22)
snake = pg.image.load("snake logo.png")
logo = pg.image.load("main snake logo.png")
food = pg.image.load("apple.png")
def music():
    pg.mixer_music.load("background music.wav") 
    pg.mixer_music.play(-1)


def txt_render(items, font,screen = screen):
    for text, pos in items:
        screen.blit(font.render(text, True, (0,0,0)), pos)

    