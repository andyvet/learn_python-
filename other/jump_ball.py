import turtle
import numpy as np

x, y, Vo, Vx, Vy, g, fi, z = 0, 0, 15, 0, 0, 2, 1.047, 1

turtle.shape('turtle')
Vy = Vo * np.sin(fi)
for t in range(0, 50):
    x += Vo * np.cos(fi)
    Vy += - g
    y += Vy - g / 2
    if y <= 0:
         Vy = Vo * np.sin(fi) - z
         z += 1
    turtle.goto(x, y)

turtle.exitonclick()