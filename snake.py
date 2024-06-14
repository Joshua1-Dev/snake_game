from turtle import Turtle
segment = [(0, 0), (-20, 0), (-40,0)]
move_distace = 20

upp = 90
downn = 270
leftt = 180
rightt = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head =self.segments[0]

    def create_snake(self):
        global segment
        for position in segment:
            self.add_segments(position)
           
    def add_segments(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distace)

    def up(self):
        if self.head.heading() != downn:
            self.head.setheading(upp)

    def down(self):
        if self.head.heading() != upp:
            self.head.setheading(downn)
    def left(self):
        if self.head.heading() != rightt:
            self.head.setheading(leftt)
    def right(self):
        if self.head.heading() != leftt:
            self.head.setheading(rightt)