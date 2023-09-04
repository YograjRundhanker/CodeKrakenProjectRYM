from tkinter import *
from tkinter import PhotoImage


def Eff_Out_Disp(root,pic,i=0):

    fp=open('Output.txt','r')
    data=fp.readlines()
    
    root.config(bg='#252525')
    canvas_width = 460
    canvas_height = 681
    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#252525', highlightthickness=0)
    canvas.place(x=50,y=100)    
    canvas.create_image(0, 0, anchor="nw", image=pic)
    
    head = "Most Effective Solution"
    canvas.create_text(210, 20, text=head, font=("Arial", 20, 'bold'), fill="white")
    for i in range(len(data)):
        canvas.create_text(10, 150+i*100, text=data[i].split(':')[0]+':', font=("Calibri", 20), fill="white", anchor='w')
        canvas.create_text(400, 165+i*100, text=data[i].split(':')[1], font=("Calibri", 20), fill="white", anchor='e')

def Chp_Out_Disp(root,pic,i=0):

    fp=open('Output.txt','r')
    data=fp.readlines()
    
    root.config(bg='#252525')
    canvas_width = 460
    canvas_height = 681
    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#252525', highlightthickness=0)
    canvas.place(x=550,y=100)    
    canvas.create_image(0, 0, anchor="nw", image=pic)
    
    head = "Cheapest Solution"
    canvas.create_text(210, 20, text=head, font=("Arial", 20, 'bold'), fill="white")
    for i in range(len(data)):
        canvas.create_text(10, 150+i*100, text=data[i].split(':')[0]+':', font=("Calibri", 20), fill="white", anchor='w')
        canvas.create_text(400, 165+i*100, text='---', font=("Calibri", 20), fill="white", anchor='e')

def Fst_Out_Disp(root,pic,i=0):

    fp=open('Output.txt','r')
    data=fp.readlines()
    
    root.config(bg='#252525')
    canvas_width = 460
    canvas_height = 681
    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='#252525', highlightthickness=0)
    canvas.place(x=1050,y=100)    
    canvas.create_image(0, 0, anchor="nw", image=pic)
    
    head = "Fastest Solution"
    canvas.create_text(210, 20, text=head, font=("Arial", 20, 'bold'), fill="white")
    for i in range(len(data)):
        canvas.create_text(10, 150+i*100, text=data[i].split(':')[0]+':', font=("Calibri", 20), fill="white", anchor='w')
        canvas.create_text(400, 165+i*100, text='---', font=("Calibri", 20), fill="white", anchor='e')

###==================Unit Testing Code
##root = Tk()
##root.config(bg='#252525')
##root.wm_attributes("-transparentcolor", 'grey')
##pic = PhotoImage(file="output_pnl.png")
##Eff_Out_Disp(root,pic)
##Chp_Out_Disp(root,pic)
##Fst_Out_Disp(root,pic)
##root.mainloop()
