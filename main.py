from turtle import *
import sys
import random

screensize(canvwidth=1000, canvheight=1000)
penup()
hideturtle()

color = "black"
size = 5
factor = 30
range = 10


def random_point_in_triangle(v1, v2, v3):
    # generate random barycentric coordinates
    a, b, c = sorted([random.random(), random.random(), random.random()])
    u = b * c
    v = a * c
    w = a * b
    # calculate the point using barycentric coordinates
    x = u * v1[0] + v * v2[0] + w * v3[0]
    y = u * v1[1] + v * v2[1] + w * v3[1]
    return x, y


points = [(-range, -range), (range, -range), (0, range)]
speed(0)


def plot(x, y):
    setpos(x * factor, y * factor)
    dot(size, color)


def median_point(p1, p2):
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return (x, y)


def calculate_next_point(point):
    prev_pt = point
    corner = points[random.randint(0, 2)]
    cur_pt = median_point(prev_pt, corner)
    plot(cur_pt[0], cur_pt[1])
    return cur_pt


plot(-range, -range)
plot(range, -range)
plot(0, range)
rand_pt = random_point_in_triangle(points[0], points[1], points[2])
plot(rand_pt[0], rand_pt[1])
next_pt = calculate_next_point(rand_pt)
while True:
    next_pt = calculate_next_point(next_pt)
done()