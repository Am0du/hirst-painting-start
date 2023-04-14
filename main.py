import turtle
from turtle import Turtle, Screen
import random


# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)


def right_turn():
    """Turn the arrow right"""
    dots.setheading(90)
    dots.forward(50)
    dots.setheading(0)
    dots.forward(50)


def left_turn():
    """Turns the arrow left"""
    dots.setheading(90)
    dots.forward(50)
    dots.setheading(180)
    dots.forward(50)


def movement():
    """Draw the dot"""
    for i in range(10):
        dot_color = random.choice(color)
        dots.dot(20, dot_color)
        dots.forward(50)


def dot_art(num):
    """Draws the number of row needed"""
    number = int(num / 2)
    for i in range(number):
        movement()
        left_turn()
        movement()
        right_turn()


color = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
         (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
         (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
         (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
         (168, 99, 102)]

dots = Turtle()
dots.shape('arrow')
turtle.colormode(255)
dots.penup()
dots.goto(-250, -200)
dots.speed('fastest')
dot_art(10)

screen = Screen()
screen.exitonclick()
