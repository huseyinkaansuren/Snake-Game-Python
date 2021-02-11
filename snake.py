import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # tuple//and constants
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head=self.snake_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake_temp = t.Turtle(shape="square")
        snake_temp.penup()
        snake_temp.color("white")
        snake_temp.goto(position)
        self.snake_list.append(snake_temp)

    def extend(self):
        #adding new snakebox to our snake
        self.add_segment(self.snake_list[-1].position())
    def move(self):
        # here is cokomelli
        for snake_num in range(len(self.snake_list) - 1, 0, -1):  # we starting from snake's tail
            new_x = self.snake_list[snake_num - 1].xcor()
            new_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)  # snake last one = middle one ->middle one = first one
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)