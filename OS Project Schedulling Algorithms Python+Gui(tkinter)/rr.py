#!/usr/bin/python
from tkinter import *
import tkinter.messagebox
from operator import itemgetter
from collections import deque
#create the window
sjf = Tk()
sjf.geometry("880x620") 
sjf.configure(background='#283747')
sjf.title("Round Robin Algorithm")

pString = StringVar()
aString = StringVar()
bString = StringVar()
sString = StringVar()
numString = StringVar()
numval = 0

process=[]

TS = 2

a = 0
Wque= deque([])
PAE = []

############################################################# FUNCTIONS

def getPro():
    global PAE
    global numval
    global a
    global RECORD
    try:
        numval = int(numString.get())
        PAE = [[] for i in range(numval)]
        RECORD = [[] for i in range(numval)]
        Prs.delete(0, END)
        Ats.delete(0, END)
        Bts.delete(0, END)
        Wts.delete(0, END)
        TATs.delete(0, END)
        a = 0
        
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
            Prs.insert(END,pval)
            Ats.insert(END,aval)
            Bts.insert(END,bval)
            
            ptext.delete(0,END)
            atext.delete(0,END)
            btext.delete(0,END)
        else:
            tkinter.messagebox.showinfo('Empty TextBox','Opps.! Something is missing in the Textbox(s).')
    else:
        tkinter.messagebox.showinfo('Warning','Enter Number of Processes First.')
    
def Calculate():
    try:
        print(1)
        if len(PAE[0]) != 0:
            #TS = .get()
            TS = 2
            print(2)
            if TS != "":
                print(3)
                #TS = int(sString.get())
                 #sorting acc. to AT
                for i in range(0,len(PAE)): # Copying in RET
                    RECORD[i].append(PAE[i][0])
                    RECORD[i].append(int(PAE[i][1]))
                    RECORD[i].append(int(PAE[i][2]))
                    print(3)
                #Prs.delete(0, END)
                #Ats.delete(0, END)
                #Bts.delete(0, END)
                PAE.sort(key=lambda x: x[1])
                n=0
                m=0
                q=0
                oldVal = 0
                length = len(Wque)
                pre=0
                count1=0
                Pq =""
                while length != -1 or RECORD[1][1]==0:
                    pre = 1
                    if m <= len(PAE):
                        for i in range(count1,n+1):
                            try:
                                if PAE[i][1] <= n:
                                    Wque.append(PAE[i][0])
                                    print("append: ",Wque)
                                    count1 = count1 + 1
                                    
                            except IndexError:
                                break
                        
                            
                    if RECORD[oldVal][1] != 0 and n !=0 and pre != 0:
                       for i in range(0,len(RECORD)):
                            if RECORD[i][0] == Pq:
                                if RECORD[i][1] != 0:
                                    Wque.append(Pq)
                                    print("append: ",Wque)
                                    break
                        

                    if len(Wque)!=0:
                        Pq = Wque[0]

                    if len(Wque)== 0:
                        length = -1
                        break
                    
                    for i in range(0,len(RECORD)):
                        if RECORD[i][0] == Pq:
                            if RECORD[i][1] > TS:
                                RECORD[i][1] = RECORD[i][1] - TS
                                oldVal = i
                            else:
                                if RECORD[i][1] == TS:
                                    RECORD[i][1] = 0
                                    PAE[i].append(n+TS)
                                else:
                                    n=n+RECORD[i][1]
                                    RECORD[i][1] = 0
                                    PAE[i].append(n)
                                    pre=0
                            break
                    
                        
                    if pre !=0 : n = n+TS
                    m = m+1
                    q = q+1
                    bb = Wque.popleft()
                    print("popping: ",bb)
                    
                for i in range(0,len(PAE)):
                    TAT = PAE[i][3]-PAE[i][1]
                    PAE[i].append(TAT)
                    WT = PAE[i][4]-PAE[i][2]
                    PAE[i].append(WT)

                for i in range(0,len(PAE)):
                    Prs.insert(END,PAE[i][0])
                    Ats.insert(END,PAE[i][1])
                    Bts.insert(END,PAE[i][2])
                    TATs.insert(END,PAE[i][4])
                    Wts.insert(END,PAE[i][5])
                AVG = 0
                for i in range(0,len(PAE)):
                    AVG = AVG + PAE[i][5]
                    AVG = AVG/len(PAE)
                tkinter.messagebox.showinfo('Average Time',AVG)            
            else:
                tkinter.messagebox.showinfo('Warning','No Time Slice Defined')
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


Heading=Label(sjf,text="Round Robin Algorithm",bg='#283747', fg='white' ,justify=CENTER,font=("The Bold Font",25)).grid(row=0, column=0,sticky=W)


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
Prs = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
Prs.grid(row=3, column=0,columnspan=5,padx=25,sticky="w")
Ats = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
Ats.grid(row=3, column=0,padx=195,sticky="w")
Bts = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
Bts.grid(row=3, column=0,padx=365,sticky="w")
Wts  = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
Wts.grid(row=3, column=0,padx=535,sticky="w") 
TATs = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
TATs.grid(row=3, column=0,padx=705,sticky="w")



btncal=Button(thirdFrame,text='CALCULATE',command=Calculate,relief=FLAT,width=12,bg='grey',activebackground='#2C3E50',fg='white',activeforeground='white',font=("Lato",12)).grid(row=5,column=0,padx=370, pady=20,sticky="w")
#############################################################
 


sjf.mainloop()
