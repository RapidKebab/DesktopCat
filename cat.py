from tkinter.constants import ANCHOR, NW
# import pyautogui
import random
import tkinter as tk
import os
# import sys
# import time

x = 1400
cycle = 0
check = 1
idle_num =[1,2]
sleep_num = [3,4,5,6,7]
event_number = random.randrange(1,7,1)
impath = os.path.dirname(__file__)
state = 0

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
label = tk.Label(t,borderwidth=0)
label.pack()
frameCntSleep = 12
frameCntIdle = 32
frameCntI2S = 24
frameCntS2I = 24

frameCnt = 12
frames = [tk.PhotoImage(file='./sleeping12.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def update(ind):
    if random.randrange(3) == 0:
        if state == 1:
            print('swappingtoidle')
            swaptoIdle(0)
        if state == 0:
            print('swappingtosleep')
            swaptoSleep(0)
    else:
        if state == 1:
            print('sleeping')
            showSleep(0)
            t.after(frameCntSleep*250, update, ind)
        if state == 0:
            print('idle')
            showIdle(0)
            t.after(frameCntIdle*250, update, ind)

#    selectAndSay(lineProb, numLines)
#
#    t.after(0,showSleep2Idle(0))        # the number t.after(*HERE*,showSleep2Idle(0)) needs to be changed to fit the timings of the output
#    
#    for x in range(1):
#        t.after(6000,showIdle(0))        # for example, it takes showSleep2Idle 6 seconds to complete its animation          
#
#    t.after(8000,showIdle2Sleep(0))    # the number in the parentheses is the starting frame of the animation (might not be accurate, hell knows why)
#
#    for x in range(1):
#        t.after(14000,showSleep(0))
#
#    t.after(12000, update, ind)

def swaptoIdle(ind):
    showSleep2Idle(0)
    t.after(frameCntS2I*250,showIdle(0))
    state = 0
    selectAndSay(lineProb, numLines)
    t.after(frameCntIdle*250, update, ind)

def swaptoSleep(ind):
    showIdle2Sleep(0)
    t.after(frameCntI2S*250,showSleep(0))
    state = 1
    t.after(frameCntSleep*250, update, ind)



framesSleep = [tk.PhotoImage(file='./sleeping12.gif',format = 'gif -index %i' %(i)).subsample(2,2) for i in range(12)]

def showSleep(ind):
    frame = framesSleep[ind]
    ind += 1
    if ind == frameCntSleep:
        return
    label.configure(image=frame)
    t.after(250, showSleep,ind)


framesIdle = [tk.PhotoImage(file='./idle32.gif',format = 'gif -index %i' %(i)) for i in range(32)]

def showIdle(ind):
    frame = framesIdle[ind]
    ind += 1
    if ind == frameCntIdle:
        return
    label.configure(image=frame)
    t.after(250, showIdle, ind)


framesIdle2Sleep = [tk.PhotoImage(file='./transitionIdle2Sleep24.gif',format = 'gif -index %i' %(i)) for i in range(24)]

def showIdle2Sleep(ind):
    frame = framesIdle2Sleep[ind]
    ind += 1
    if ind == frameCntI2S:
        return
    label.configure(image=frame)
    t.after(250, showIdle2Sleep, ind)


framesSleep2Idle = [tk.PhotoImage(file='./transitionSleep2Idle24.gif',format = 'gif -index %i' %(i)) for i in range(24)]

def showSleep2Idle(ind):
    frame = framesSleep2Idle[ind]
    ind += 1
    if ind == frameCntS2I:
        return
    label.configure(image=frame)
    t.after(250, showSleep2Idle, ind)

#setup for dialog
#import random
lineProb = 2 #one in every 20 idle cycles will display text
dialoglines = open('dialoglines.txt')
numLines = 0
with dialoglines as f:
    i=0
    for i, l in enumerate(f):
        pass
    numLines = i+1 #well this is technically number-1
dialoglines.close()
#print(numLines)
def selectAndSay(lineProb, numLines):
    if random.randrange(lineProb) == 0:
        print('')
        with open('dialoglines.txt') as f:
            print(f.readlines()[random.randrange(numLines)])
    else:
        print('')


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