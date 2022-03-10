#Momentum

import tkinter as tk
import time 
import numpy as np

root=tk.Tk()

canvas=tk.Canvas(root,width=1500,height=850,bg="black")
global T
T=1
#velocity of square a
a_v=10
canvas.grid(row=0,column=0)
#width and height of square a
#properties of square a
a_m=10
a_w=50
a_h=50
a_pos_x=100
a_pos_y=100
a_dir=1

#properties of square b
b_m=10
b_v=10
b_w=50
b_h=50
b_pos_x=500
b_pos_y=100
b_dir=-1
dir_change=1
while True:
    canvas.delete("all")
    a_loc_x=a_pos_x+a_v*T*a_dir
    b_loc_x=b_pos_x+b_v*T*b_dir
    #check if collide
    if a_loc_x+a_w>=b_loc_x:
        dir_change=-1
        T-=1
        a_loc_x=a_pos_x+a_v*T*a_dir
        b_loc_x=b_pos_x+b_v*T*b_dir
    a = canvas.create_rectangle(a_loc_x, a_pos_y, a_loc_x+a_w, a_pos_y+a_h, fill="white")
    b=canvas.create_rectangle(b_loc_x,b_pos_y, b_loc_x+b_w,b_pos_y+b_h,fill="white")
   # txt=canvas.create_text(0,0,fill="white",font="Arial",text="Momentum of A is "+a_m*a_v)
    canvas.pack()
    if dir_change==1:
        T+=1
    elif dir_change==-1:
        T-=1
    time.sleep(1)
    canvas.update()
    if T==55 or T==0:
        break

tk.mainloop()

