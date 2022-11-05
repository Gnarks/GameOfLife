import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors

def step(param):
    array = np.zeros((mx,my))
    for x in range(len(array)):
        for y  in range(len(array[x])):
            sum = 0
            for nx,ny in neighbourhood:
                if x + nx >=0 and nx+x < mx and y+ny >=0 and ny+y < my:
                    if param[nx+x,ny+y] == ALIVE:
                        sum+=1
            if param[x,y] == DEAD and sum == 3: array[x,y] = ALIVE
            elif param[x,y] == ALIVE:
                if sum != 2 and sum != 3:
                    array[x,y] = DEAD
                else:
                    array[x,y] = ALIVE
            else:
                array[x,y] = param[x,y]
    return array
        
        
neighbourhood = ((-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1,1))
colors_list = ["white","black"]
cmap = colors.ListedColormap(colors_list)
bounds = [0,1]
norm = colors.BoundaryNorm(bounds, cmap.N)
DEAD,ALIVE = 0,1

mx,my = 20,20
X = np.zeros((mx,my))
fig, ax = plt.subplots()
im = plt.imshow(X,cmap,norm=norm)
cur_pos,start,end = (0,0),(0,0),(0,0)

def key_pressed(event):
    update.X = step(update.X)

def onclick(event):
    if event.inaxes:
        update.X[round(event.ydata), round(event.xdata)] = ALIVE if  update.X[round(event.ydata), round(event.xdata)] == DEAD else DEAD
        

key_cid = fig.canvas.mpl_connect("key_press_event",key_pressed)
pressed_cid = fig.canvas.mpl_connect('button_press_event', onclick)

def update(i):
    im.set_data(update.X)
    
update.X = X

delay = 1
anim = animation.FuncAnimation(fig,update,interval=delay,frames= 5)

plt.show()