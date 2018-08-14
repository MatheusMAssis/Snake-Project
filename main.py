import Snake as s
import Fruit as f

snake = s.Snake()
fruit = f.Fruit()
start = True

#processing option for screen
def setup():
    size(400,400)
    frameRate(20)
    
def draw():
    global snake, fruit, start
    
    #home screen
    if start == True:
        background(0)
        fill(255)
        textAlign(CENTER)
        textSize(40)
        text('SNAKE', width/2, height/2)
        textSize(14)
        text('version 1.0', width/2, height/2 + 20)
        textSize(20)
        text('CLICK TO START', width/2, height - 50)
        textSize(10)
        text('developed by: Matheus de Moncada Assis', width/2, 20)
    
    #starting the game if mouse is pressed
    if mousePressed:
        if mouseX < width and mouseY < height:
            start = False
    
    #drawing fruit and snake
    if not start:
        background(0)
        snake.draw_snake()
        snake.coordinates()
        fruit.draw_fruit()
        if [fruit.x, fruit.y] in snake.hist:
            fruit.new_pos
        
        #determine if it has eaten a fruit or not
        if snake.eat(fruit.x, fruit.y):
            fruit.new_pos()
            fruit.draw_fruit()
        
        #determine if it is dead or not
        if snake.x < 0 or snake.x > width or snake.y < 0 or snake.y > height or snake.death():
            fill(255,255,255,200)
            rect(0,0,width,height)
            textSize(40)
            fill(0)
            textAlign(CENTER)
            text('GAME OVER', width/2, height/2)
            textSize(20)
            text('LENGTH: {}'.format(snake.total),width/2, height/2 + 50)
            noLoop()
    
#changing snake directions
def keyPressed():
    if keyCode == UP and snake.dy != 1:
        snake.direction(0,-1)
    elif keyCode == DOWN and snake.dy != -1:
        snake.direction(0,1)
    elif keyCode == RIGHT and snake.dx != -1:
        snake.direction(1,0)
    elif keyCode == LEFT and snake.dx != 1:
        snake.direction(-1,0)
