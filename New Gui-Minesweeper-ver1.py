from cProfile import label
from tkinter import *
import tkinter.font as font
import os
from calendar import c
import math
from pickletools import string4
import sys
import random
import time

mw= Tk()

mw.title("")
num1=""
m=0
n=0
p=0.0
files = []
btn = {}
frame1 = Frame(mw)
frame2 = Frame(mw)
frame1.pack()
frame2.pack()
#frame2.pack(padx=50,pady=50)

Label(frame1, text="MINESWEEPER",fg="BLUE",bd=2,relief=RAISED,font=('Calibri Bold',50)).grid(row=1, column=3)
Label(frame1,text="Enter Number of Rows (1-30)",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',15)).grid(row=7, column=2)
Myrow=Entry(frame1,width=5,borderwidth=5)
Myrow.grid(row=7, column=3)

Label(frame1,text="Enter Number of Columns (1-30)",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',15)).grid(row=9, column=2)
Mycol=Entry(frame1,width=5,borderwidth=5)
Mycol.grid(row=9, column=3)

Label(frame1,text="Enter Difficulty Level between 0 and 10",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',15)).grid(row=11, column=2)
Mydiff=Entry(frame1,width=5,borderwidth=5)
Mydiff.grid(row=11, column=3)


def myclick(num):
    #os.system('cls')
    proceed_cnt=0  #If input values incorrect then this count will be greater than 0
    m = Myrow.get()
    
    if int(Myrow.get()) < 1 or int(Myrow.get()) >30:
        Label(frame1,text="No of rows must be between 1 and 30",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',13)).grid(row=14, column=3)
        proceed_cnt = proceed_cnt+1
    n = Mycol.get()
    if int(Mycol.get()) < 1 or int(Mycol.get()) >30:
        Label(frame1,text="No of columns must be between 1 and 30",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',13)).grid(row=14, column=3)
        proceed_cnt = proceed_cnt+1
    if int(Mydiff.get()) < 0 or int(Mydiff.get()) > 10:
        Label(frame1,text="Difficulty level must be between 0 and 10",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',13)).grid(row=14, column=3)
        proceed_cnt=proceed_cnt+1
    p1 = Mydiff.get()
    nrow = int(m)+1
    ncol=int(n)+1
    p=int(p1)/10


    #Proceed only if valid input is given i.e proceed_cnt = 0

    if proceed_cnt==0:
        #First clear the earlier labels and entry widgets
        for widget in frame1.winfo_children():
              widget.destroy()

        Label(frame1, text="MINESWEEPER",fg="BLUE",bd=2,relief=RAISED,font=('Calibri Bold',50)).grid(row=1, column=3)
        
        #files = [] #creates list to initialise button list from this list
        #btn = [] #creates list to store the buttons 
        files = [['      ' for c in range(nrow+1)] for c in range(ncol+1)] 
        btn = [['  ' for c in range(nrow+1)] for c in range(ncol+1)] 

        '''for i in range(1,nrow): 
            print(" Rows : "+str(nrow)+" Columns : "+str(ncol))
            for j in range(1,ncol):
                print(" i = "+str(i)+" j = "+str(j))
                files[i][j] = "    "  
        i=i+1'''
        
        # Variables declaration
        ucol = 0
        urow = 0
        string=[]
        sol=[]
        userboard=[]
        ms=[]
        mines=[]
        counter=0
        firsttime=0

        #Initialise all lists
        #string = [['-' for c in range(n+2)] for c in range(m+2)]
        sol = [[0 for c in range(ncol+1)] for c in range(nrow+1)]
        userboard = [['-' for c in range(ncol+1)] for c in range(nrow+1)]
        ms = [['-' for c in range(ncol+1)] for c in range(nrow+1)]
        mines = [['-' for c in range(ncol+1)] for c in range(nrow+1)]              
        EmptyCells =0 
        #game grid is [1..m][1..n], border is used to handle boundary cases
        #Populating the mines array 
        for i in range(1,nrow):
            for j in range(1,ncol):
                 y=random.random() 
                 #print("y ="+str(y)+" p = "+str(p))
                 if (y < p):
                    mines[i][j] = "*"
                 else:
                    mines[i][j] = "-"
            j=j+1
        i=i+1


       # sol[i][j] = # mines adjacent to cell (i, j)
       # Populating an array with N o. of mines in the cells adjacent to mines
        for i in range(1,nrow):
           for j in range(1,ncol):
                #(ii, jj) indexes to check the neighbouring cells
                for ii in range(i-1,i+2):#Moving across rows
                    for jj in range(j-1,j+2):#Moving across columns
                        if (mines[ii][jj] == "*"):
                            sol[i][j]=sol[i][j]+1
                    jj= jj+1
                ii=ii+1
           j=j+1
        i=i+1

        #Populating all cells with mines and No. of  mines . This is the solution array
        vvv=""
        for i in range(1,nrow):
            for j in range(1,ncol):
                 if (mines[i][j] == "*"):                
                     ms[i][j] = "*"
                     
                 else: 
                     ms[i][j] =str(sol[i][j])
                 #vvv=ms[i][j]
                 #print(" vvv = "+vvv)
            j=j+1
        i=i+1   
        
        # Function to check if user has completed the board: Returns the count of cells without mines.
        def ChkBoardComplete(uboard,ms1, row , column):
               EmptyCellCount=0
               MineCount =0

               for i in range(1,row):
                   for j in range(1,column): 
                       if (uboard[i][j] =="-"):       
                           EmptyCellCount=EmptyCellCount+1
                       if(ms1[i][j]=="*"):
                           MineCount=MineCount+1
               i=i+1
               if(EmptyCellCount==MineCount):
                       EmptyCellCount =  0
               return EmptyCellCount  

        #Function to pause the screen for a while
        def WaitScreen ():
            n=0
            while True:
                n=n+1
                if (n >= 1000):
                    break
     
        # Function which is executed when button is clicked
        def myclick1(rw, col):
                Button_click=True
                #print("In click function : row = "+str(rw)+ "  col = "+str(col))
                
                btn[rw][col].configure(text=ms[rw][col])
                userboard[rw][col] = ms[rw][col]
                if ms[rw][col]=="*":
                    Label(frame1,text="SORRY !!! YOU HAVE HIT A MINE, BETTER LUCK NEXT TIME",fg="RED",anchor='w',bd=1,relief=RAISED,font=('Calibri',15)).grid(row=rw+20, column=col+10)
                    #time.sleep(1)
                    for widget in frame2.winfo_children():
                        widget.destroy()
                else :
                    EmptyCells = 0
                    EmptyCells = ChkBoardComplete (userboard,ms,nrow,ncol)       
                    if (EmptyCells == 0):       #If all cells are filled 
                        Label(frame1,text="CONGRATS !!!! YOU HAVE WON").grid(row=rw+20,column=col+10)
                        for widget in frame2.winfo_children():
                             widget.destroy()
             
                
        # Display the buttons  
        myFont = font.Font(family='Helvetica', size=15, weight='bold')     
        for i in range(1,nrow):
            for j in range(1,ncol):
                btn[i][j]=Button(frame2, font=myFont, fg='dark green',text=files[i][j],command=lambda  r=i, c=j: myclick1(r,c))  #lambda c=i,d=j: print(btn[c][d].cget("text")))
                btn[i][j].grid(row=i+10,column=j+10)
            j=j+1
        i=i+1

        
                
    
    return 1
    

bt1 = Button(frame1, text = "CONFIRM", fg="GREEN",relief=RAISED,font=('Calibri',15),command = lambda : myclick(0)).grid(row=20,column=3)



#Put the code in loop
mw.mainloop()
