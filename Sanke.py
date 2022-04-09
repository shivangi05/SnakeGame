import time
from turtle import Turtle,Screen
starting_position = [(0, 0), (-20, 0), (-40, 0)]
distance = 10

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in starting_position:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(position)
            self.segment.append(new)

    def move(self):
         for seg in range(len(self.segment) - 1, 0, -1):
              newx = self.segment[seg - 1].xcor()
              newy = self.segment[seg - 1].ycor()
              self.segment[seg].goto(newx, newy)
              self.segment[0].forward(distance)

    def up(self):
        self.segment[0].setheading(90)
    def down(self):
        self.segment[0].setheading(270)
    def left(self):
        self.segment[0].setheading(0)
    def right(self):
        self.segment[0].setheading(180)






