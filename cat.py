from tkinter.constants import ANCHOR, NW
# import pyautogui
import random
import tkinter as tk
import os
import sys
import time

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
screen_height = t.winfo_screenheight()-46-240
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
label1_text.set("Mishookoo\n ~your personal desk cat~")
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
time.sleep(5)

def update(ind):
    if random.randrange(4) == 0:
        if ind == 0:
            showIdle2Sleep(0)
            ind = 1
            t.after(frameCntI2S*250, update,ind)
        elif ind == 1:
            showSleep2Idle(0)
            ind = 0
            t.after(frameCntS2I*250, update,ind)
    else:
        if ind == 1:
            showSleep(0)
            t.after(frameCntSleep*250, update,ind)
        elif ind == 0:
            selectAndSay(lineProb, numLines)
            showIdle(0)
            t.after(frameCntIdle*250, update,ind)

def swaptoIdle(ind):
    showSleep2Idle(0)
    t.after(frameCntS2I*250,showIdle(0))
    selectAndSay(lineProb, numLines)
    t.after(frameCntIdle*250, update(0))

def swaptoSleep(ind):
    showIdle2Sleep(0)
    t.after(frameCntI2S*250,showSleep(0))
    t.after(frameCntSleep*250, update(1))



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
            label1_text.set(f.readlines()[random.randrange(numLines)])
    else:
        print('')


t.after(0, update, 0)

tk.mainloop()