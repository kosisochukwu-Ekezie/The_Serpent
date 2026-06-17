import assets as ast
import pygame as pg
intro_texts = [
    ("WELCOME",(100,100)),
    ("TO", (290,200)),
    ("THE SERPENT",(250,301))
    ]
menu_texts = [
 ("LEVEL/MODE", (250,80)),
 ("REGULAR", (200,200)),
 ("DIFFICULT", (580,200))
    ]
additional_texts = [ 
    ('press "R" to Regular',(150,280) )  ,
    ('press "D" for difficult', (500,280))
]
pg.display.set_icon(ast.logo)
pg.display.set_caption("The Serpent")
start_time = pg.time.get_ticks()
state = ""
running = True 
ast.music()
while running:
    ast.screen.fill((0,125,0))
    current_time = pg.time.get_ticks()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and current_time - start_time >= 4000:
            if event.key == pg.K_r:
                ast.selected_mode = "regular"
                import game_logic as gl
                running = False
            if event.key == pg.K_d:
                ast.selected_mode = "difficult"
                import game_logic as gl
                running = False

    if current_time - start_time < 4000:
        ast.screen.blit(ast.snake,(125,300))
        ast.txt_render(intro_texts,ast.intro_font)
    else:
        ast.txt_render(menu_texts,ast.menu_font)
        ast.txt_render(additional_texts,ast.text_font)
        ast.screen.blit(ast.snake,(400,350))
    
 
    pg.display.update()