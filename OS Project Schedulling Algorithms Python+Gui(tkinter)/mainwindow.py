#!/usr/bin/python
from tkinter import *
import tkinter.messagebox
import sys
import os


def ljf():
    menu.destroy()
    os.system('ljf.py')

def fcfs():
    menu.destroy()
    os.system('fcfs.py')

def srt():
    menu.destroy()
    os.system('srt.py')

def rr():
    menu.destroy()
    os.system('rr.py')
    



if __name__ == '__main__':
    
    menu = Tk()
    menu.geometry("900x700")
    menu.configure(background='#283747')
    menu.title("Main Menu")

    lheading = Label(menu,text="CHOOSE AN ALGORTIHM",bg='#283747',fg='white',font=("Open Sans Bold",25))
    lheading.grid(row=0,column=0,padx=250,pady=50)
    
    btnfcfs = Button(menu,text='FIRST COME FIRST SERVE',command=fcfs,cursor="hand2",width=30, height=3, relief=FLAT,bg='#85929E',activebackground='#117864',fg='white',activeforeground='white',font=("Arial",15))
    btnfcfs.grid(row=6,column=0,pady=10)
    
    btnljf = Button(menu,text='LONGEST JOB FIRST',cursor="hand2",command=ljf,relief=FLAT,width=30,height=3,bg='#85929E',activebackground='#117864',fg='white',activeforeground='white',font=("Montserrat Semi Bold",15))
    btnljf.grid(row=10,column=0,pady=10)
    
    btnsrt = Button(menu,text='SHORTEST REMAINING TIME',command=srt,cursor="hand2",relief=FLAT,width=30,height=3,bg='#85929E',activebackground='#117864',fg='white',activeforeground='white',font=("Montserrat Semi Bold",15))
    btnsrt.grid(row=12,column=0,pady=10)
    
    btnrr = Button(menu,text='ROUND ROBIN',cursor="hand2",command=rr,relief=FLAT,width=30,height=3,bg='#85929E',activebackground='#117864',fg='white',activeforeground='white',font=("Montserrat Semi Bold",15))
    btnrr.grid(row=14,column=0,pady=10)

    menu.mainloop()
