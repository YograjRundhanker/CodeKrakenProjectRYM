from tkinter import *
from tkinter import PhotoImage


def Eff_Out_Disp(root,pic):
    # Create a canvas
    canvas_width = 460
    canvas_height = 681
    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.place(x=50,y=100)    
    canvas.create_image(0, 0, anchor="nw", image=pic)
    
    # Add text on top of the image
    text = "Hello, World!"
    canvas.create_text(200, 150, text=text, font=("Arial", 20), fill="white")

##root = Tk()
##root.title("Canvas with Image and Text")
##pic = PhotoImage(file="Output_pnl.png")
##Eff_Out_Disp(root,pic)
##root.mainloop()
