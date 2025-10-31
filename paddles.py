from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.penup()
        self.setposition(position)
        self.color("white")
        self.shapesize(4,1)
    
    # KEY CONTROLS
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)    
