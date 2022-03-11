from tkinter import *
import numpy as np
import random
import math

root = Tk()
Bodies = []

Number = 2
Distance = 10
Mass = [15, 15]
V0 = [np.array([0,0], dtype=float), np.array([0,0], dtype=float)]
Elasticity = 1
Problem = "Momentum"




root.wm_title("Ph_Sim") #window title

width=800 #window sizes
height=800

canvas = Canvas(root, width=width, height=height, bg = "black") #create backround
canvas.grid(row=0, column=0)



class physics: #perent class that defs vars for all future classes
    def __init__(self, Mass, Elasticity, Gravity, V0):
        self.Charge = Charge
        self.Mass = Mass
        self.Elasticity = Elasticity
        self.Gravity = Gravity
        self.Force = Force
        self.Velocity = np.array(V0, dtype=float)
        self.Satellite = Satellite





class Momentum(physics):
    def __init__(self, Mass, V0, Elasticity, PositionX, PossitonY):
        self.Width = 10+Mass
        self.PositionX = PositionX #position will be calced in IF block
        self.PositionY = PositionY
        self.Position = np.array([self.PositionX, self.PositionY], dtype=float)
        self.Velocity = np.array(V0, dtype=float)
        self.Mass = Mass
        self.Elasticity = Elasticity


    def Function(self, other):##apply function to bodies #built for checking self against other
        if self == other:
            self.dv = np.array([0,0], dtype=float)

        else:
            ##calc dist between two objects
            self.dist = math.sqrt((self.Position[0]-other.Position[0])**2 + (self.Position[1]-other.Position[1])**2)
            #start with 0 change in v
            self.dv = np.array([0,0], dtype=float)
            if self.dist == 0: #safety to not div by 0
                self.dv = 0
            else:
                if self.dist<=((self.Width/2)+(other.Width/2)): #if touching
                    self.Force = (self.Elasticity*((self.Mass*self.Velocity)-(other.Mass*other.Velocity)))
                    self.dv =  self.Force / self.Mass

            self.Velocity += self.dv

        if self.Position[0] < self.Width/2: #wall collision
            self.Velocity[0] *= -Elasticity
            self.Position[0] += 1

        if self.Position[0] > width - (self.Width/2):
            self.Velocity[0] *= -Elasticity
            self.Position[0] -= 1

        if self.Position[1] < self.Width/2:
            self.Velocity[1] *= -Elasticity
            self.Position[1] += 1

        if self.Position[1] < height - (self.Width/2):
            self.Velocity[1] *= -Elasticity
            self.Position[1] -= 1



class Orbit(physics):
    def __init__(self, Mass, V0, Elasticity, Distance, PositionX, PossitonY):
        super().__init__(Mass, V0, Elasticity, Distance) #calls def on all of these
        self.Width = Mass*2
        self.PositionX = PositionX #position will be calced in IF block
        self.PositionY = PositionY
        self.Position = np.array([self.PositionX, self.PositionY], dtype=float)

    def Function(self, other):##apply function to bodies #built for checking self against other
        if self == other:
            self.dv = np.array([0,0], dtype=float)

        else:
            ##calc dist between two objects
            self.dist = math.sqrt((self.Position[0]-other.Position[0])**2 + (self.Position[1]-other.Position[1])**2)
            #start with 0 change in v
            self.dv = np.array([0,0], dtype=float)
            if self.dist == 0: #safety to not div by 0
                self.dv = 0
            else:
                if self.dist<=((self.width/2)+(other.width/2)): #if touching
                    self.Force = (self.Elasticity*((self.Mass*self.Velocity)-(other.Mass*other.Velocity)))
                    self.dv =  self.Force / self.Mass

            self.V += self.dv

        if self.Position[0] < self.Width/2: #wall collision
            self.Velocity[0] *= -Elasticity
            self.Position[0] += 1

        if self.Position[0] > width - (self.Width/2):
            self.Velocity[0] *= -Elasticity
            self.Position[0] -= 1

        if self.Position[1] < self.Width/2:
            self.Velocity[1] *= -Elasticity
            self.Position[1] += 1

        if self.Position[1] < height - (self.Width/2):
            self.Velocity[1] *= -Elasticity
            self.Position[1] -= 1



class Electrostatic(physics):
    def __init__(self, Mass, V0, Elasticity, Distance, PositionX, PossitonY):
        super().__init__(Mass, V0, Elasticity, Distance) #calls def on all of these
        self.Width = Mass*10
        self.PositionX = PositionX #position will be calced in IF block
        self.PositionY = PositionY
        self.Position = np.array([self.PositionX, self.PositionY], dtype=float)

    def Function(self, other):##apply function to bodies #built for checking self against other
        if self == other:
            self.dv = np.array([0,0], dtype=float)

        else:
            ##calc dist between two objects
            self.dist = math.sqrt((self.Position[0]-other.Position[0])**2 + (self.Position[1]-other.Position[1])**2)
            #start with 0 change in v
            self.dv = np.array([0,0], dtype=float)
            if self.dist == 0: #safety to not div by 0
                self.dv = 0
            else:
                if self.dist<=((self.width/2)+(other.width/2)): #if touching
                    self.Force = (self.Elasticity*((self.Mass*self.Velocity)-(other.Mass*other.Velocity)))
                    self.dv =  self.Force / self.Mass

            self.V += self.dv

        if self.Position[0] < self.Width/2: #wall collision
            self.Velocity[0] *= -Elasticity
            self.Position[0] += 1

        if self.Position[0] > width - (self.Width/2):
            self.Velocity[0] *= -Elasticity
            self.Position[0] -= 1

        if self.Position[1] < self.Width/2:
            self.Velocity[1] *= -Elasticity
            self.Position[1] += 1

        if self.Position[1] < height - (self.Width/2):
            self.Velocity[1] *= -Elasticity
            self.Position[1] -= 1


if Problem == "Momentum":
    distance = Distance*20
    for i in range(Number):
        #calc spawn location
        if i%2 == 0:
            PositionX = round(width/2)-round(distance/2)
        else:
            PositionX = round(width/2)+round(distance/2)
        PositionY = (height/2)

        Bodies.append(Momentum(Mass[i], V0[i], Elasticity, PositionX, PositionY))#create individual bodies with correct properties


    while True:

        canvas.delete("all")

        for Body1 in Bodies:
            for Body2 in Bodies:
                Body1.Function(Body2)
            Body1.Position += Body1.Velocity

        for Body in Bodies:
            canvas.create_rectangle(Body.Position[0] - (Body.Width/2), Body.Position[1]-(Body.Width), Body.Position[0]+(Body.Width/2), Body.Position[1]+(Body.Width), fill = 'white')


        canvas.update()






mainloop()
