from tkinter import*
from tkinter.font import *
from tkinter import ttk
import os
import time
def quitwin(event):
    root.destroy()
    quit()
def timeformat():
    ctime=time.localtime(time.time())
    hour=ctime.tm_hour
    minute=ctime.tm_min
    second=ctime.tm_sec
    if minute<10:
        minute="0"+str(minute)
    if second<10:
        second='0'+str(second)
    return str(hour)+':'+str(minute)+':'+str(second) 
def dateformat():
    ctime=time.localtime(time.time())
    year=ctime.tm_year
    month=ctime.tm_mon
    day=ctime.tm_wday
    weekday=ctime.tm_wday

    wdaylist=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    mlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    return wdaylist[weekday]+' '+str(day)+' '+str(mlist[month-1])+' '+str(year)
root=Tk()
root.wm_attributes('-transparentcolor','white')
root.geometry('500x210+500+500')
root.config(bg='white')
root.overrideredirect(True)
timefont=Font(size=100,family='Bahnschrift SemiBold')
datefont=Font(size=30,family='Bahnschrift SemiBold')
timeshow=Label(root,text=timeformat(),font=timefont,bg='white',fg='#FFFFFE')
dateshow=Label(root,text=dateformat(),font=datefont,bg='white',fg='#FFFFFE')
timeshow.pack()
dateshow.pack()
root.bind('<F12>',quitwin)
while True:
    timeshow.config(text=timeformat())
    timeshow.update()
    dateshow.config(text=dateformat())
    dateshow.update()
