# IMPORTING MODULES
from turtle import Screen
from line import Fence
from paddles import Paddle
from ball import Ball
from score import ScoreBoard
import time

# DEFINING THE SCREEN
screen = Screen()
screen.title("Ping Pong")
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.tracer(0)
      
# BORDER LINE
border = Fence()  

# SCORE
score_board = ScoreBoard()

# PADDLES
r_paddle = Paddle((390, 0))    
l_paddle = Paddle((-390, 0)) 

# BALL
ball = Ball()                  

# BUTTON CONTROLS
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


# ------------------------------------------------
game_is_on = True

def off():
    global game_is_on 
    game_is_on = False
    score_board.goto(0,0)
    score_board.write("GAME OVER", align="center", font=("Courier", 50, "normal"))
    
def restart():
    score_board.l_score = 0
    score_board.r_score = 0
    ball.reset_position()
    score_board.update_score()

screen.onkey(off, "o")
screen.onkey(restart, "r")
# ------------------------------------------------- 

# GAME MECHANICS
while game_is_on:
    time.sleep(0.05) 
    ball.move()
    screen.update()
    # DETECT COLLISION WITH THE WALL (TOP & BOTTOM)
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()
        
    # DETECT COLLISION WITH THE PADDLE (LEFT & RIGHT)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        
    # ELSE RESTART AND INCREASE THE SCORE
    if ball.xcor() > 450:
        ball.reset_position()
        score_board.r_point()
        
    
    if ball.xcor() < -450:
        ball.reset_position()
        score_board.l_point()
        

# SCREEN EXIT ON CLICK
screen.exitonclick()