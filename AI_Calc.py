import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle
from time import sleep  # Import sleep from the time module
from threading import *
import AI_pump_Output as AIPO

#===================================================================GIF===============================================================#
global lbl, ImageLabel, k
k=0

def AI_Optimizer(root, i=0):
    global lbl
    class ImageLabel(Label):
        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            frames = []

            try:
                for i in count(1):
                    frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass
            self.frames = cycle(frames)

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(frames) == 1:
                self.config(image=next(self.frames))
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.config(image=next(self.frames))
                self.after(self.delay, self.next_frame)


    lbl = ImageLabel(root, bg='black')
    lbl.pack()
    lbl.load('AI Button.gif')

#=========================================================Progressbar Animation=======================================================#

def Progress_Anim(root, pic, i=0):
    sleep(1)
    global progress_value, ImageLabel

    def update_progress():
        global progress_value, ImageLabel
        if progress_value < 100:
            progress_value += 1
            update_canvas()
            root.after(100, update_progress)
        if progress_value >= 100:
            transparent_window.destroy()
            disp_thrd1 = Thread(target=AIPO.Eff_Out_Disp, daemon=True, args=(root,pic,0))
            disp_thrd1.start()
            try:
                lbl.unload()
                lbl.destroy()
            except:
                pass
            disp_thrd2 = Thread(target=AIPO.Chp_Out_Disp, daemon=True, args=(root,pic,0))
            disp_thrd2.start()
            disp_thrd3 = Thread(target=AIPO.Fst_Out_Disp, daemon=True, args=(root,pic,0))
            disp_thrd3.start()

    def update_canvas():
        canvas.delete("progress_bar")
        bar_width = int((progress_value / 100) * canvas_width)
        canvas.create_rectangle(0, 0, bar_width, canvas_height, fill="blue", outline="blue", tags="progress_bar")

    canvas_width = 400
    canvas_height = 20

    # Create a transparent toplevel window
    transparent_window = Toplevel(root)
    transparent_window.overrideredirect(True)
    transparent_window.attributes('-alpha', 0.8)
    transparent_window.geometry('400x20+545+600')
    transparent_window.config(bg='black')

    # Create a canvas on the transparent window
    canvas = Canvas(transparent_window, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    progress_value = 0
    update_progress()


#=========================================================CALCULATION=======================================================#

def ALL_Calc(root, pic, i=0):

    AI_Optimizer(root,0)
    Progress_Anim(root, pic, i=0)
    
    fp = open('Inputs.txt', 'r')
    data = fp.readlines()

    sprl_height = int(data[0][:-1])
    sprl_atmprs = int(data[1][:-1])
    sprl_whldia = int(data[2][:-1])

    hdrm_height = int(data[3][:-1])
    hdrm_inflow = int(data[4][:-1])

    cplr_height = int(data[5][:-1])
    cplr_atmprs = int(data[6][:-1])

    bdgt = int(data[7][:-1])
    water_qntty = int(data[8][:-1])
    fp.close()

    # ===============Adjusted Parameters
    sprl_cost = 5000
    sprl_outflw = 30  # litre/hour

    hdrm_cost = 6000
    hdrm_outflw = 40  # litre/hour

    cplr_cost = 2000
    cplr_outflw = 10  # litre/hour

    time_min = 0.5
    time_max = 3
    # ===============Efficiency
    sprl_eff = sprl_cost / sprl_outflw
    hdrm_eff = hdrm_cost / hdrm_outflw
    cplr_eff = cplr_cost / cplr_outflw

    # ===============Classification
    eff_pmps = {sprl_eff: ['Spiral', sprl_outflw, sprl_cost], hdrm_eff: ['Hydram', hdrm_outflw, hdrm_cost],
                cplr_eff: ['Capillary', cplr_outflw, cplr_cost]}
    eff_pmps = dict(sorted(eff_pmps.items()))
    chp_pmps = {sprl_cost: 'Spiral', hdrm_cost: 'Hydram', cplr_cost: 'Capillary'}
    chp_pmps = dict(sorted(chp_pmps.items()))
    fst_pmps = {sprl_outflw: 'Spiral', hdrm_outflw: 'Hydram', cplr_outflw: 'Capillary'}
    fst_pmps = dict(sorted(fst_pmps.items()))

    '''In the budget, this is the most effective pump with this much quantity which will take this much time'''
    max_LtrPrHr = bdgt / list(eff_pmps.keys())[0]
    qty_effx = int(max_LtrPrHr/eff_pmps[list(eff_pmps.keys())[0]][1])

    #print(qty_effx,eff_pmps[list(eff_pmps.keys())[0]][0],'pumps which will cost',qty_effx*(eff_pmps[list(eff_pmps.keys())[0]][2]),'and will take',water_qntty/(qty_effx*(eff_pmps[list(eff_pmps.keys())[0]][1])),'hours')

    fp=open('Output.txt','w')
    fp.write('Pump:'+eff_pmps[list(eff_pmps.keys())[0]][0]+'\n')
    fp.write('Quantity:'+str(qty_effx)+'\n')
    fp.write('Cost:'+str(qty_effx*(eff_pmps[list(eff_pmps.keys())[0]][2]))+': INR'+'\n')
    fp.write('Time:'+str(water_qntty/(qty_effx*(eff_pmps[list(eff_pmps.keys())[0]][1])))+': hr'+'\n')
    fp.close()

    
    



##root=Tk()
####AI_Optimizer(root)
####Progress_Anim(root)
##ALL_Calc(root)
##root.mainloop()
