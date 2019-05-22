#!/usr/bin/python
from tkinter import *
import tkinter.messagebox
from operator import itemgetter

sjf = Tk()
sjf.geometry("880x620") 
sjf.configure(background='#283747')
sjf.title("Longest Job First")

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
    global RET
    try:
        numval = int(numString.get())
        PAE = [[] for i in range(numval)]
        RET = [[] for i in range(numval)]
        Prs.delete(0, END)
        Ats.delete(0, END)
        Bts.delete(0, END)
        Wts.delete(0, END)
        AWs.delete(0, END)
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
            Prs.delete(0, END)
            Ats.delete(0, END)
            Bts.delete(0, END)
            TAT=0
            wt=[0]
            PAE.sort(key=lambda x: x[1])
            print("Proc AT ET")
            for i in range(0,len(PAE)):
                print(PAE[i])
            print(" ")
            et = PAE[0][2]
            print(PAE[0][2])
            RET[0].append(PAE[0][0])
            RET[0].append(PAE[0][1])
            RET[0].append(PAE[0][2])
            v = 1
            i = 1
            k = i
            while i < (len(PAE)+1):
                try:
                    if PAE[i][1] <= et:
                        
                        if i == k:
                            RET[i].append(PAE[i][0])
                            RET[i].append(PAE[i][1])
                            RET[i].append(PAE[i][2])
                            
                            k = k + 1
                    else:
                        
                        RET[v:i] = sorted(RET[v:i], key=itemgetter(2),reverse = True)
                        et = et + RET[v][1]
                        print(RET)
                        k = i
                        v = v + 1
                        i = v
                        i = i - 1
                        if v > len(PAE):
                            break
                except IndexError:
                    RET[v:i] = sorted(RET[v:i], key=itemgetter(2),reverse = True)
                    et = et + RET[v][1]
                    v = v + 1
                    if v > len(PAE):
                        break
                i = i + 1
            temp = RET[0][2]
            RET[0].append(0)
            #for waiting time
            for i in range(1,len(RET)):
                RET[i].append(temp - RET [i][1])
                temp = temp + RET[i][2]
            #for turnaround time
            tmp = 0
            for i in range(0,len(RET)):
                tmp = tmp + RET[i][2]
                RET[i].append(tmp - RET [i][1])
                
                
            print("Procs AT ET WT TAT")
            for i in range(0,len(RET)):
                print(RET[i])        
            
            for i in range(0,len(RET)):
                Prs.insert(END,RET[i][0])
                Ats.insert(END,RET[i][1])
                Bts.insert(END,RET[i][2])
                Wts.insert(END,RET[i][3])
                AWs.insert(END,RET[i][4])
            AVG = 0
            for i in range(0,len(PAE)):
                AVG = AVG + RET[i][3]
            AVG = AVG/len(RET)
            tkinter.messagebox.showinfo('Information','Average Waitng Time: '+repr(AVG))
            
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


Heading=Label(sjf,text="Longest Job First",bg='#283747', fg='white' ,justify=CENTER,font=("The Bold Font",25)).grid(row=0, column=0,sticky=W)


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
AWs = Listbox(thirdFrame , height=8,width=9,bg='#17202A', fg='white' ,font=("Lato Light",16))
AWs.grid(row=3, column=0,padx=705,sticky="w")



btncal=Button(thirdFrame,text='CALCULATE',command=Calculate,relief=FLAT,width=12,bg='grey',activebackground='#2C3E50',fg='white',activeforeground='white',font=("Lato",12)).grid(row=5,column=0,padx=370, pady=20,sticky="w")
#############################################################
 


sjf.mainloop()
