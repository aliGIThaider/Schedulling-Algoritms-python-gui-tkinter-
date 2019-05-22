#!/usr/bin/python
from tkinter import *
import tkinter.messagebox
from operator import itemgetter
#create the window
sjf = Tk()
sjf.geometry("880x620") 
sjf.configure(background='#283747')
sjf.title("Shortest Remaining Time")

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
        if len(PAE[0]) != 0:
            for i in range(0,len(PAE)): # Copying in RET
                RECORD[i].append(PAE[i][0])
                RECORD[i].append(int(PAE[i][1]))
                RECORD[i].append(int(PAE[i][2]))
            Prs.delete(0, END)
            Ats.delete(0, END)
            Bts.delete(0, END)
            PAE.sort(key=lambda x: x[1])
            print("Proc AT ET")

            for i in range(0,len(PAE)): #PAE Printing Only
                print(PAE[i])

            print(" ")

            s=m=n=o=pre=0

                
            while n != -1:
                pre=0    
                if m <= len(PAE):
                    try:
                        if PAE[m][1] == n:
                        
                            for i in range(0,m):
                                if PAE[i][2] <= PAE[m][2] and PAE[i][2] != 0:
                                    PAE[i][2] = PAE[i][2] - 1 #If BURST time of new process is greater than the one's exsisting
                                    if PAE[i][2] == 0:
                                        PAE[i].append(n+1) #Append the Completion time
                                    pre = 1
                                    break
                            if pre != 1:
                                PAE[m][2] = PAE[m][2] - 1
                                if PAE[m][2] == 0:
                                        PAE[m].append(n+1) #Append the Completion time
                            o = o+1
                        else: #If no New process is Arrived at N secs
                            PAE[o][2] = PAE[o][2] - 1 
                            if PAE[o][2] == 0:
                                PAE[o].append(n) #Append the Completion time
                    except IndexError:
                        #When NO process will come
                        PAE.sort(key=lambda x: x[2])
                        for i in range(0,len(PAE)):
                            if PAE[i][2] == 0:    #Ignoring all those process whose Burst time = 0 or in other words Process is completed
                                s = s+1
                            else:
                                break
                else:
                    #Processing the remaing Process When All the process has arrived
                    try:
                        PAE[s][2] = PAE[s][2] - 1
                        if PAE[s][2] == 0:
                            PAE[s].append(n) #Append the Completion time
                            s = s + 1
                    except IndexError:
                        break;
                n = n + 1
                m = m + 1

            RECORD.sort(key=lambda x: x[1])
            PAE.sort(key=lambda x: x[1])

            # Copying back the actual BURST time and Replacing ZEROs
            for i in range(0,len(PAE)):
                PAE[i][2] = PAE[i][2] + RECORD[i][2]
                

            for i in range(0,len(PAE)):
                #Calculating TAT
                TAT = PAE[i][3]-PAE[i][1]
                PAE[i].append(TAT)
                #Calculating Waiting time
                WT = PAE[i][4] - PAE[i][2]
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
            tkinter.messagebox.showinfo('Error','No Data Found')
    except IndexError:
       tkinter.messagebox.showinfo('Error','No Data Found nnn')


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


Heading=Label(sjf,text="Shortest Remaining Time",bg='#283747', fg='white' ,justify=CENTER,font=("The Bold Font",25)).grid(row=0, column=0,sticky=W)


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
