from tkinter import *
from tkcalendar import Calendar



startCount = 0
endCount = 0

def startCal():    
    global startCal
    global startCount    
    if startCount == 1:
        startCount = 0
        startCal.place_forget()
    else:       
        startCal = Calendar(root)
        startCount = startCount + 1
        startCal.pack(pady=10)
        startCal.place(x=5, y=240)

def endCal():    
    global endCal
    global endCount
    if endCount == 1:
        endCount = 0
        endCal.place_forget()
    else:
        endCal = Calendar(root)
        endCount = endCount + 1    
        endCal.pack(pady=10)
        endCal.place(x=230, y=240)

def removeCal():
    global startCount
    global endCount
    if startCount == 1:
        startCount = 0
        startCal.place_forget()
    if endCount == 1:
        endCount = 0
        endCal.place_forget()