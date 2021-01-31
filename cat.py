from tkinter.constants import ANCHOR, NW
import pyautogui
import random
import tkinter as tk
import os
import sys
x = 1400
cycle = 0
check = 1
idle_num =[1,2]
sleep_num = [3,4,5,6,7]
event_number = random.randrange(1,7,1)
impath = os.path.dirname(__file__)

#window configuration
t = tk.Tk()
t.title("Mishookoo")
frame = tk.Frame(t, highlightthickness=-2,borderwidth=-2)
frame.pack()
t.overrideredirect(True)
screen_width = t.winfo_screenwidth()-240
screen_height = t.winfo_screenheight()-32-240
screen_resolution = '+'+str(screen_width)+'+'+str(screen_height)
t.geometry(screen_resolution)
t.wm_attributes("-transparentcolor", "red",'-topmost', True)
t.lift()
canvas = tk.Canvas(frame,width=240,height=240,bd=-2)

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

label1_text=tk.StringVar()
label1_text.set("Mishookoo")
label1=tk.Label(t, textvariable=label1_text)
label1.pack()
# attach popup to frame
label1.bind("<Button-3>", do_popup)

L = tk.Label(t, text="Right-click to display menu", width=40, height=20)
# L.pack()
m = tk.Menu(t, tearoff=0)
m.add_command(label="Exit", command=exit)
frame.bind("<Button-3>", do_popup) 


frameCnt = 12
frames = [tk.PhotoImage(file='./sleeping12.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    t.after(250, update, ind)
    
label = tk.Label(t,borderwidth=0)
label.pack()

frameCntSleep = 12
framesSleep = [tk.PhotoImage(file='./sleeping12.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def showSleep(ind):
    frame = framesSleep[ind]
    ind += 1
    if ind == frameCntSleep:
        ind = 0
    label.configure(image=frame)
    t.after(250, showSleep, ind)

frameCntIdle = 32
framesIdle = [tk.PhotoImage(file='./idle32.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def showIdle(ind):
    frame = framesIdle[ind]
    ind += 1
    if ind == frameCntIdle:
        ind = 0
    label.configure(image=frame)
    t.after(250, showIdle, ind)

frameCntI2S = 24
framesIdle2Sleep = [tk.PhotoImage(file='./transitionIdle2Sleep24.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def showIdle2Sleep(ind):
    frame = framesIdle2Sleep[ind]
    ind += 1
    if ind == frameCntI2S:
        ind = 0
    label.configure(image=frame)
    t.after(250, showIdle2Sleep, ind)

frameCntS2I = 24
framesSleep2Idle = [tk.PhotoImage(file='./transitionSleep2Idle24.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def showSleep2Idle(ind):
    frame = framesSleep2Idle[ind]
    ind += 1
    if ind == frameCntS2I:
        ind = 0
    label.configure(image=frame)
    t.after(250, showSleep, ind)

t.after(0, update, 0)

tk.mainloop()


# #transfer random no. to event
# def event(cycle,check,event_number,x):
#     if event_number in idle_num:
#         check = 0
#         print('idle')
#         window.after(400,update,cycle,check,event_number,x) #no. 1,2,3,4 = idle
#     else:
#         check  = 1
#         print('sleep')
#         window.after(1000,update,cycle,check,event_number,x)#no. 10,11,12,13,15 = sleep
# #making gif work 
# def gif_work(cycle,frames,event_number,first_num,last_num):
#     print('giffing')
#     if cycle < len(frames) -1:
#         cycle+=1
#     else:
#         cycle = 0
#         event_number = random.randrange(first_num,last_num+1,1)
#     return cycle,event_number
# def update(cycle,check,event_number,x):
#     print('updating')
#     print(check)
#     #idle
#     if check ==0:
#         frame = idle[cycle]
#         cycle ,event_number = gif_work(cycle,idle,event_number,0,7)
# #sleep
#     elif check == 1:
#         frame = sleep[cycle]
#         cycle ,event_number = gif_work(cycle,sleep,event_number,0,7)
#     window.geometry('100x100+'+str(x)+'+1050')
#     label.configure(image=frame)
#     window.after(1,event,cycle,check,event_number,x)

# window = tk.Tk()
# #call buddy's action gif
# idle = [tk.PhotoImage(file=impath+'\\idle.gif' ,format = 'gif -index %i' %(i)) for i in range(10)]#idle gif
# sleep = [tk.PhotoImage(file=impath+'\\sleep.gif',format = 'gif -index %i' %(i)) for i in range(7)]#sleep gif

# #window configuration
# window.config(highlightbackground='white')
# label = tk.Label(window,bd=0,bg='white')
# window.overrideredirect(True)
# window.wm_attributes('-transparentcolor','white')
# label.pack()
# #loop the program
# window.after(1,update,cycle,check,event_number,x)
# window.mainloop()