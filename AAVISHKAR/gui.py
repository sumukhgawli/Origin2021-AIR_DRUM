from tkinter import *
import os 
from tkinter.filedialog import askopenfilename 
import tkinter.messagebox as prompt 


  
# Create Object  
root = Tk()  
root.title("AAVISHK<AR>-THE AUGMENTED REALITY")
# root.iconbitmap(r'C:\Users\Deepak Prasad\Desktop\AAVISHKAR-THE AUGMENTED REALITY\Images\drum-clipart-10.ico')
  
# Set geometry 
root.geometry('640x480')
root.configure(bg='#856ff8')
greet=Label(root,text='WELCOME SUMUKH GAWLI!',background='#856ff8',font=("Courier",15,"bold")).place(x=40,y=10)
def run():  
    os.system('airdrum.py')
def feature():
    prompt.showinfo('Coming Soon','This feature will be available in the next update') 
def about():
    prompt.showinfo('About Us','The application is purely created by Mast Deepak Prasad & Mast Sumukh Gawli Using Computer Vision Technology Version TCSCO21')
def rec():
    os.system("rec.py")
play=Button(root,text="Play AR Drum\n [Offline]",command=run,width=20,height=4,activeforeground = "white",activebackground="black")
stream=Button(root,text="Stream\n [Online]",command=feature,width=20,height=4,activeforeground = "white",activebackground="black").place(x=220,y=140)
record=Button(root,text="Record\n [Locally]",command=rec,width=20,height=4,activeforeground = "white",activebackground="black").place(x=400,y=140)
About=Button(root,text="About Us",command=about,width=20,height=4,activeforeground = "white",activebackground="black").place(x=220,y=240)
play.place(x=40,y=140)
  
# Execute Tkinter 
root.mainloop()