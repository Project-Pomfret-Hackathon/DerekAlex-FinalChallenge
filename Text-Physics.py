from tkinter import *
import numpy as np
import random
import math

root = Tk()
str = "Calculate the force between charges of 5.0 x 10^5C and 1.0 x 10^7C if they are 5.0 cm apart."

root.wm_title(str) #window title

width=1500 #window sizes
height=850

canvas = Canvas(root, width=width, height=height, bg = "black") #create backround
canvas.grid(row=0, column=0)

class physics:
    def __init__(Radius, Number, Charge, Distance, Mass, Elasticity, Gravity, Force, V0, Satellite, Px0, Py0):

class CoulombsLaw(physics): #class for problem type
    def __init__(self, Radius, Number, Charge, Distance):








touched = False

Radius = 7 #radius of ball
n_Bodies = 80 #number of objects
PosNeg = 40 #relitave charges of each body
xspawn_min = Radius #spawn locations
xspawn_max =width-Radius
yspawn_min =Radius
yspawn_max =height-Radius
wall_collide = .3 #wall collission dampening
ball_colide = 1 #ball dampening
G = 5



canvas = Canvas(root, width=width, height=height, bg = "black") #creat backround
canvas.grid(row=0, column=0)


Pos_Bodies = [] #define empty lists for ball separation
Neg_Bodies = []
Total_Bodies = []


class Body:
    def __init__(self, Charge, Px, Py, V, Radius, touched): ##define variables of body
        self.Charge = Charge
        self.Px = Px
        self.Py = Py
        self.P = np.array([self.Px, self.Py], dtype=float) #set position as array of xy
        self.V = np.array(V, dtype=float) #set velocity as array
        self.R = Radius #set radius
        self.touched = touched



    def Fg(self, other, n_bodies, Pos_Bodies, Radius, touched): #function for calculating the force of gravity between two objects

        if self == other:
            self.dv = np.array([0,0], dtype=float)
        else:
            self.dist = math.sqrt((self.P[0]-other.P[0])**2 + (self.P[1]-other.P[1])**2) #get dist between both using pythag Th
            self.dv = np.array([0,0], dtype=float) #define delta v
            if self.dist == 0: #dont / 0
                self.dv = 0
            else:
                self.F = ((G * (self.Charge * other.Charge)) / self.dist**2) * (self.P - other.P) / self.dist #define force as ESF equation
                self.dv = self.F / abs(self.Charge) #define change in v as force / mass
                if self.dist < self.R*2: #if touching
                    if self.Charge != other.Charge:
                        self.touched = True
                        other.touched = True
                    else:
                        self.dv *= -ball_colide #bounce
                        # if self.Charge > 0:
                        #     Pos_Bodies.append(Body(PosNeg, random.randrange(Radius,width+Radius), random.randrange(Radius,width+Radius), [(random.randrange(-100,100)/20), (random.randrange(-100,100)/20)], Radius, touched))
                        # if self.Charge < 0:
                        #     Neg_Bodies.append(Body(-PosNeg, random.randrange(Radius,width+Radius), random.randrange(Radius,width+Radius), [(random.randrange(-100,100)/20), (random.randrange(-100,100)/20)], Radius, touched))



                self.V += self.dv #delta v to total v

        if self.P[0] < self.R*2: ##wall check
            self.V[0]*= -wall_collide
            self.P[0] += 1
        if self.P[0] > width - self.R*2:
            self.V[0]*= -wall_collide
            self.P[0] -= 1
        if self.P[1] < self.R*2:
            self.V[1]*= -wall_collide
            self.P[1] += 1
        if self.P[1] > height - self.R*2:
            self.V[1]*= -wall_collide
            self.P[1] -= 1




for i in range(n_Bodies): #define properties
    if i%2 != 0:
        Pos_Bodies.append(Body(PosNeg, random.randrange(Radius,width+Radius), random.randrange(Radius,width+Radius), [(random.randrange(-100,100)/20), (random.randrange(-100,100)/20)], Radius, touched))
    else:
        Neg_Bodies.append(Body(-PosNeg, random.randrange(Radius,width+Radius), random.randrange(Radius,width+Radius), [(random.randrange(-100,100)/20), (random.randrange(-100,100)/20)], Radius, touched))
for P in Pos_Bodies:
    Total_Bodies.append(P)
for N in Neg_Bodies:
    Total_Bodies.append(N)
random.shuffle(Total_Bodies)


T = 0 #define time itterator

while True:
    T+=1

    canvas.delete("all") #clear for new calcs

    for Body1 in Total_Bodies: #for each body ...
        for Body2 in Total_Bodies: #check against all other bodies
            Body1.Fg(Body2, n_Bodies, Pos_Bodies, Radius, touched)
        Body1.P += Body1.V

    for index, Body in enumerate(Neg_Bodies):#create shapes for + -  balls
        if Body.touched == False:
            canvas.create_oval(Body.P[0] - Body.R, Body.P[1] -Body.R, Body.P[0] + Body.R, Body.P[1] + Body.R, fill = 'black', outline = 'white') #create visible orbs from theoretical body
        else:
            canvas.create_oval(Body.P[0] - Body.R, Body.P[1] -Body.R, Body.P[0] + Body.R, Body.P[1] + Body.R, fill = 'black', outline = 'white', tags='touching') #create visible orbs from theoretical body
            Neg_Bodies.remove(Body)
            Total_Bodies.remove(Body)

    for index, Body in enumerate(Pos_Bodies):
         if Body.touched == False:
             canvas.create_oval(Body.P[0] - Body.R, Body.P[1] -Body.R, Body.P[0] + Body.R, Body.P[1] + Body.R, fill = 'white') #create visible orbs from theoretical body
         else:
             canvas.create_oval(Body.P[0] - Body.R, Body.P[1] -Body.R, Body.P[0] + Body.R, Body.P[1] + Body.R, fill = 'white', tags='touching') #create visible orbs from theoretical body
             Pos_Bodies.remove(Body)
             Total_Bodies.remove(Body)



    canvas.delete('touching')

    canvas.update() #itterate animation

mainloop()#loopsystem
