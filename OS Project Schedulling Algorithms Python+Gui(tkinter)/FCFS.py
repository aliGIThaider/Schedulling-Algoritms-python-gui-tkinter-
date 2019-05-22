#!/usr/bin/python
from tkinter import *
import tkinter.messagebox
from operator import itemgetter
#create the window
sjf = Tk()
sjf.geometry("880x620") 
sjf.configure(background='#283747')
sjf.title("First Come First Serve")

pString = StringVar()
aString = StringVar()
bString = StringVar()
numString = StringVar()
numval = 0
a = 0
PAE = []
RET = []


############################################################# FUNCTIONS

def getPro():
    global PAE
    global numval
    try:
        numval = int(numString.get())
        PAE = [[] for i in range(numval)]
        tkinter.messagebox.showinfo('Information','Added Successfully.')
    except ValueError:
        tkinter.messagebox.showinfo('Error','Enter Numeric Data.')
        
def process():
    if len(PAE) != 0:
        global a
        op=1
        pval = pString.get()
        aval = aString.get()
        bval = bString.get()
        if pval != "" and aval != "" and bval != "":
            if(a<numval):
                PAE[a].append(pval)
                PAE[a].append(int(aval))
                PAE[a].append(int(bval))
                a = a+1
            else:
                tkinter.messagebox.showinfo('Information','Limit Reached.')
                return
            ProcessList.insert(END,pval)
            ArrivalList.insert(END,aval)
            BurstList.insert(END,bval)

            ptext.delete(0,END)
            atext.delete(0,END)
            btext.delete(0,END)
        else:
            tkinter.messagebox.showinfo('Empty TextBox','Opps.! Something is missing in the Textbox(s).')
    else:
        tkinter.messagebox.showinfo('Warning','Enter Number of Processes First.')
 
def Calculate():
    try:
        if len(PAE[0]) != 0:
            ProcessList.delete(0, END)
            ArrivalList.delete(0, END)
            BurstList.delete(0, END)
            TAT=0

            PAE.sort(key=lambda x: x[1])
            print("Proc AT ET")
            for i in range(0,len(PAE)):
                print(PAE[i])
            print(" ")
            et = PAE[0][2]
            PAE[0].append(0)
            for i in range(1,len(PAE)):
                PAE[i].append(et)
                et=et+PAE[i][2]

            for i in range(0,len(PAE)):
                PAE[i][3] = PAE[i][3] - PAE[i][1]
            print("Procs AT ET WT")
            for i in range(0,len(PAE)):
                print(PAE[i])        
            for i in range(0,len(PAE)):
                TAT = TAT + int(PAE[i][2])

            p="Turnaround time :"+repr(TAT)
            tkinter.messagebox.showinfo('Information',p)
                

            for i in range(0,len(PAE)):
                ProcessList.insert(END,PAE[i][0])
                ArrivalList.insert(END,PAE[i][1])
                BurstList.insert(END,PAE[i][2])
                WaitingList.insert(END,PAE[i][3])
            AVG = 0
            for i in range(0,len(PAE)):
                AVG = AVG + PAE[i][3]
            AVG = AVG/len(PAE)
            TurnAroundList.insert(END,AVG)
        else:
            tkinter.messagebox.showinfo('Error','No Data Found')
    except IndexError:
        tkinter.messagebox.showinfo('Error','No Data Found')


#############################################################
#Frames Declaration
#############################################################

topFrame = Frame(sjf,bg='#283747', width=600, height=200)
topFrame.grid(row=1,column=0, sticky="w")

secondFrame = Frame(sjf,bg='grey', width=600, height=200, pady=10)
secondFrame.grid(row=2,column=0, sticky="w")

thirdFrame = Frame(sjf,bg='#283747', width=600, height=200, pady=20)
thirdFrame.grid(row=3,column=0, sticky="w")
#############################################################


Heading=Label(sjf,text="First Come First Serve",bg='#283747', fg='white' ,justify=CENTER,font=("The Bold Font",25)).grid(row=0, column=0,sticky=W)


#############################################################
#Insert a Process #Second Frame
#############################################################
l1=Label(secondFrame,text="Process Number",bg='grey', fg='white' ,font=("Lato Light",15)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
l2=Label(secondFrame,text="Arival Time", bg='grey', fg='white',font=("Lato Light",15)).grid(row=4, column=0, padx=10, pady=5,sticky=W)
l3=Label(secondFrame,text="Burst Time", bg='grey', fg='white',font=("Lato Light",15)).grid(row=5, column=0, padx=10, pady=5,sticky=W)
ptext = Entry(secondFrame,width=40,textvariable=pString)
ptext.grid(row=3, column=0, padx=200)
atext = Entry(secondFrame,width=40,textvariable=aString)
atext.grid(row=4, column=0,padx=200)
btext = Entry(secondFrame,width=40,textvariable=bString)
btext.grid(row=5, column=0, padx=200)

#Insert Button
btnf=Button(secondFrame,text='INSERT PROCESS',command=process,relief=FLAT,width=15,
            bg='#1C2833',activebackground='#1C2833',fg='white',activeforeground='white',
            font=("Lato",12)).grid(row=6,column=0, padx=250, pady=5,sticky=W)
#############################################################



#############################################################
#number of process box #Third Frame
#############################################################

sjtext = Entry(topFrame,width=40,textvariable=numString)
sjtext.grid(row=3, column=0, padx=200)
l4=Label(topFrame,text="Number of Processes", bg='#283747', fg='white',font=("Lato Light",15)).grid(row=3, column=0, padx=10, pady=5,sticky=W)

#Process Button
btnf=Button(topFrame,text='START INPUT',command=getPro,relief=FLAT,
            width=15,bg='#1C2833',activebackground='#1C2833',fg='white',
            activeforeground='white',font=("Lato",12)).grid(row=3,column=1)
#############################################################





#############################################################
#list boxes and labels #thirdframe
#############################################################
LabelProcess = Label(thirdFrame ,text='Processes',bg='#283747', fg='white' ,font=("Lato",15)).grid(row=2, column=0,padx=30,sticky="w")
LabelArrivalTime = Label(thirdFrame ,text='Arrival Time',bg='#283747', fg='white' ,font=("Lato",15)).grid(row=2, column=0,padx=195,sticky="w")
LabelBurstTme = Label(thirdFrame ,text='Burst Time',bg='#283747', fg='white' ,font=("Lato",15)).grid(row=2, column=0,padx=370,sticky="w")
LabelWaitingTime = Label(thirdFrame ,text='Waiting Time',bg='#283747', fg='white' ,font=("Lato",15)).grid(row=2, column=0,padx=530,sticky="w")
LabelTurnAround = Label(thirdFrame ,text='Turnaround',bg='#283747', fg='white' ,font=("Lato",15)).grid(row=2, column=0,padx=705,sticky="w")

#list boxes
ProcessList = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
ProcessList.grid(row=3, column=0,columnspan=5,padx=25,sticky="w")
ArrivalList = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
ArrivalList.grid(row=3, column=0,padx=195,sticky="w")
BurstList = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
BurstList.grid(row=3, column=0,padx=365,sticky="w")
WaitingList  = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
WaitingList.grid(row=3, column=0,padx=535,sticky="w") 
TurnAroundList = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
TurnAroundList.grid(row=3, column=0,padx=705,sticky="w")


btncal=Button(thirdFrame,text='CALCULATE',command=Calculate,relief=FLAT,width=12,bg='grey',activebackground='#2C3E50',fg='white',activeforeground='white',font=("Lato",12)).grid(row=5,column=0,padx=370, pady=20,sticky="w")
#############################################################
 


sjf.mainloop()
