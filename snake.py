class Snake:
    
    def __init__(self):
        self.x = 200
        self.y = 200
        self.dx = 1
        self.dy = 0
        self.total = 1
        self.hist = []
        self.hist.append([self.x,self.y])
    
    #determine if it has touched itself
    def death(self):
        if self.total > 2:
            historic = self.hist[0:len(self.hist)-2]
            if self.hist[len(self.hist)-1] in historic:
                return True
    
    #growing by one as you eat one fruit
    def eat(self,x,y):
        distance = dist(self.x,self.y,x,y)
        if distance <= 1:
            self.total += 1
            self.hist.append([])
            for n in range(len(self.hist)-1):
                self.hist[n-1] = self.hist[n]
            return True
        else:
            return False
    
    #determine all the squares that form its body
    def coordinates(self):
        self.x += self.dx * 10
        self.y += self.dy * 10
        for n in range(len(self.hist)-1):
            for k in range(self.total):
                self.hist[n-k] = self.hist[n-1-k]
        self.hist[len(self.hist)-1] = [self.x, self.y]
    
    #drawing snake in repeat
    def draw_snake(self):
        fill(255)
        #print(self.x, self.y, self.hist, self.total)
        for i in range(len(self.hist)):
            rect(self.hist[i][0], self.hist[i][1], 10, 10)
    
    #changing snake direction as you press arrow keys
    def direction(self,x,y):
        self.dx = x
        self.dy = y
