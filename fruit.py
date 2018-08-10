class Fruit:
    
    def __init__(self):
        self.x = floor(random(400)/10)
        self.y = floor(random(400)/10)
        self.x *= 10
        self.y *= 10
    
    #drawing fruit at its coordinates
    def draw_fruit(self):
        fill(255,0,0)
        rect(self.x, self.y, 10, 10)
    
    #redefining position as it is eaten by the snake
    def new_pos(self):
        self.x = floor(random(400)/10)
        self.y = floor(random(400)/10)
        self.x *= 10
        self.y *= 10
