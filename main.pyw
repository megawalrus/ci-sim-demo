import os
import pygame
from Tkinter import *

os.chdir(sys.path[0])
win = Tk()
win.title("Cochlear Implant Simulation: Pop Quiz")
f = Frame(win)
bHeight = 8
bWidth = 30
pygame.mixer.init()

# Define each button and set callback functions to play each sound file


def b1_aud():
    pygame.mixer.music.load('sounds/Hello_CI.wav')
    pygame.mixer.music.play()
b1 = Button(f, height=bHeight, width=bWidth, text="Pop - play with simulation", command=b1_aud, bg='HotPink1')


def b2_aud():
    pygame.mixer.music.load('sounds/TeenSpirit_CI.wav')
    pygame.mixer.music.play()
b2 = Button(f, height=bHeight, width=bWidth, text="Rock - play with simulation", command=b2_aud, bg='DarkOrange1')


def b3_aud():
    pygame.mixer.music.load('sounds/StillDRE_CI.wav')
    pygame.mixer.music.play()
b3 = Button(f, height=bHeight, width=bWidth, text="Hip hop - play with simulation", command=b3_aud, bg='DarkOliveGreen2')


def b4_aud():
    pygame.mixer.music.load('sounds/TakeFive_CI.wav')
    pygame.mixer.music.play()
b4 = Button(f, height=bHeight, width=bWidth, text="Jazz - play with simulation", command=b4_aud, bg='SteelBlue1')


def b5_aud():
    pygame.mixer.music.load('sounds/Symphony9_CI.wav')
    pygame.mixer.music.play()
b5 = Button(f, height=bHeight, width=bWidth, text="Classical - play with simulation", command=b5_aud, bg='MediumPurple2')


def b6_aud():
    pygame.mixer.music.load('sounds/Hello.wav')
    pygame.mixer.music.play()
b6 = Button(f, height=bHeight, width=bWidth, text="Pop - reveal original", command=b6_aud, bg='grey10', fg='HotPink1')


def b7_aud():
    pygame.mixer.music.load('sounds/TeenSpirit.wav')
    pygame.mixer.music.play()
b7 = Button(f, height=bHeight, width=bWidth, text="Rock - reveal original", command=b7_aud, bg='grey10', fg='DarkOrange1')


def b8_aud():
    pygame.mixer.music.load('sounds/StillDRE.wav')
    pygame.mixer.music.play()
b8 = Button(f, height=bHeight, width=bWidth, text="Hip hop - reveal original", command=b8_aud, bg='grey10', fg='DarkOliveGreen2')


def b9_aud():
    pygame.mixer.music.load('sounds/TakeFive.wav')
    pygame.mixer.music.play()
b9 = Button(f, height=bHeight, width=bWidth, text="Jazz - reveal original", command=b9_aud, bg='grey10', fg='SteelBlue1')


def b10_aud():
    pygame.mixer.music.load('sounds/Symphony9.wav')
    pygame.mixer.music.play()
b10 = Button(f, height=bHeight, width=bWidth, text="Classical - reveal original", command=b10_aud, bg='grey10', fg='MediumPurple2')

# Define button positions
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)
b4.grid(row=0, column=4)
b5.grid(row=0, column=5)
b6.grid(row=1, column=1)
b7.grid(row=1, column=2)
b8.grid(row=1, column=3)
b9.grid(row=1, column=4)
b10.grid(row=1, column=5)

l = Label(win, text="Click the buttons to hear a short piece of music from each musical genre. Can you identify each piece?")
l.pack()
f.pack()

# Place the window roughly centre-screen and open it
win.update_idletasks()
width = win.winfo_width()
height = win.winfo_height()
x = (win.winfo_screenwidth() // 2) - (width // 2)
y = (win.winfo_screenheight() // 2) - (height // 2) - 100
win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

win.iconbitmap(default='resources/note.ico')
win.mainloop()
