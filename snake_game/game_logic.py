import assets as ast
import pygame as pg
import snake as sk
import random
mode = ast.selected_mode
clock = pg.time.Clock()
game_over = ast.intro_font.render("GAME OVER",True,(180,0,0))
score = 0
play = True
x_values = []
y_values = []
for i in range(35, 766, 35):
    x_values.append(i)
for i in range(70, 566, 35):
    y_values.append(i)
def occupied_positions(snake):
    positions = set()
    temp = snake.head
    while temp:
        positions.add((temp.x, temp.y))
        temp = temp.next
    return positions


def random_food_position(snake=None, old_position=None):
    blocked = set()

    if snake is not None:
        blocked.update(occupied_positions(snake))

    if old_position is not None:
        blocked.add(old_position)

    possible_positions = [
        (x, y)
        for x in x_values
        for y in y_values
        if (x, y) not in blocked
    ]

    return random.choice(possible_positions)

def draw_body(x,y):
    pg.draw.rect(ast.screen,(0,0,0),(x,y,35,35))
def draw_snake(snake):
    temp = snake.head 
    while temp:
        draw_body(temp.x,temp.y)
        temp = temp.next
def movement(snake):
    global play

    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and snake.last_direction != (0, 35):
                snake.direction = (0, -35)
            elif event.key == pg.K_DOWN and snake.last_direction != (0, -35):
                snake.direction = (0, 35)
            elif event.key == pg.K_RIGHT and snake.last_direction != (-35, 0):
                snake.direction = (35, 0)
            elif event.key == pg.K_LEFT and snake.last_direction != (35, 0):
                snake.direction = (-35, 0)

    if snake.direction != (0, 0):
        snake.move(snake.direction[0], snake.direction[1])

    draw_snake(snake)

class food:
    def __init__(self, snake=None):
        self.x, self.y = random_food_position(snake)

def eat(snake, food):
    head = snake.head
    global score
    if head.x == food.x and  head.y == food.y:
        score = score + 1
        snake.grow_pending = True
        food.x, food.y = random_food_position(snake, (food.x, food.y))
    

x = sk.body(35, 70, None)
y = sk.body(70, 70, x)
snake = sk.snake(y, x)
apple = food(snake)
while play:
    ast.screen.fill((0,125,0))
    scoreboard = ast.text_font.render(f"Score: {score} ", True,(255,255,255))
    ast.screen.blit(scoreboard,(10,10))    
    movement(snake)
    eat(snake,apple)
    ast.screen.blit(ast.food,(apple.x,apple.y))
    if snake.check_selfcollision():
        ast.screen.fill((0,125,0))
        ast.screen.blit(game_over,(180,250))
        ast.screen.blit(scoreboard,(220,350))
        pg.display.update()
        pg.time.delay(4000)
        play = False
    if snake.check_wallcollision(800, 600):
        ast.screen.fill((0,125,0))
        ast.screen.blit(game_over,(180,250))
        ast.screen.blit(scoreboard,(220,350)) 
        pg.display.update()
        pg.time.delay(4000)
        play = False
    if mode == "difficult":
        clock.tick(8) 
    elif mode == "regular":
        clock.tick(5)   
    pg.display.update()