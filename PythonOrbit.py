import math
import numpy as np
import tkinter as tk

DELAY = 100
CIRCULAR_PATH_INCR = 10

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))

class Celestial(object):
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)
    m=10
    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def bounds(self):
        return (self.x + self.radius*self.COS_0,   self.y + self.radius*self.SIN_270,
                self.x + self.radius*self.COS_180, self.y + self.radius*self.SIN_90)

def circular_path(x, y, radius, delta_ang, start_ang=0):
    ang = start_ang % 360
    while True:
        yield x + radius*cos(ang), y + radius*sin(ang)
        ang = (ang+delta_ang) % 360

def update_position(canvas, id, celestial_obj, path_iter):
    celestial_obj.x, celestial_obj.y = next(path_iter)  
    x0, y0, x1, y1 = canvas.coords(id) 
    oldx, oldy = (x0+x1) // 2, (y0+y1) // 2  
    dx, dy = celestial_obj.x - oldx, celestial_obj.y - oldy  
    canvas.move(id, dx, dy) 
    canvas.after(DELAY, update_position, canvas, id, celestial_obj, path_iter)

def inc_m():
    print("mass increased!")
    for i in range(NumBod):
        Planets[i].mass+=5

#a is star; b is planet - goes both for calcvel and calcfor
def CalcVel(a,b):
    a_pos=[a.x,a.y]
    b_pos=[b.x,b.y]
    radius=math.dist(a_pos,b_pos)
    return sqrt(np.G*a.m/radius)

def CalcFor(a,b):
    a_pos=[a.x,a.y]
    b_pos=[b.x,b.y]
    radius=math.dist(a_pos,b_pos)
    G=np.G
    return G*a.m*b.m/((radius)*(radius))

root = tk.Tk()
root.title("Orbit")

canvas = tk.Canvas(root, bg='black', height=500, width=500)
canvas.pack()
#Set num
NumBod=4
Planets=[]
Display=[]



for i in range(NumBod):
    Planets.append(Celestial(250+150+i*30,250+i*30,15))

sol_obj = Celestial(250, 250, 25)
sol = canvas.create_oval(sol_obj.bounds(), fill='yellow', width=0)
for index, Celestial in enumerate(Planets):
    Display.append(canvas.create_oval(Planets[index].bounds(),fill='blue',width=0))
#for in range(NumBod):
    
#planet1 = canvas.create_oval(planet_obj1.bounds(), fill='blue', width=0)
#planet2=canvas.create_oval(planet_obj2.bounds(),fil
for index, Celestial in enumerate(Planets):
    orbital_radius = math.hypot(sol_obj.x - Planets[index].x, sol_obj.y - Planets[index].y)
    path_iter = circular_path(sol_obj.x, sol_obj.y, orbital_radius, CIRCULAR_PATH_INCR)
    next(path_iter) 
    root.after(DELAY, update_position, canvas, Display[index], Planets[index], path_iter)
    
tk.Button(root, text="increase mass",command=inc_m()).pack()
root.mainloop()
