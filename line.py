from turtle import Turtle, Screen

class Fence(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.setposition(0, -345)
        self.left(90)
        self.fence()
        
    def fence(self):
        for _ in range(0, 17):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
    
    
        
