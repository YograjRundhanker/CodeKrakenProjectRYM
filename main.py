from tkinter import *
from threading import *
from time import *
from Pumps_Calc import *
from AI_Calc import *
from AI_pump_Output import *

cnt=0
fp = open('Inputs.txt','w')
fp.close()

def Float():
    global root, bt_strt, cnt
    if cnt<50:
        cnt+=1
        sleep(0.01)
        bt_strt.place(x=scr_width/2-246/2, y=scr_height/2-100-cnt)
        Float()
    
flw_cnt=0
resp = []
def Start():
    global root, bt_strt,lb_ques,flw_cnt,resp
    i=0
    def Next(wdgt,i):
        n=int(scr_height/2-200)
        if i<n:
            wdgt.place(x=scr_width/2-wdgt.winfo_width()/2, y=i)
            wdgt.configure(image=photoimage)
            root.update()
            #sleep(0.001)
            i+=1
            Next(wdgt,i)
    
    if flw_cnt <5:
        ques = ['q1.png','q2.png','q3.png','q4.png','q5.png']
        bt_strt.destroy()
        photo = PhotoImage(file = ques[flw_cnt])
        photoimage = photo.subsample(2, 2)
        lb_ques.configure(image=photoimage)
        x=Thread(target=Next, daemon=True, args=(lb_ques,i))
        x.start()
        def Yes():
            global resp, flw_cnt, ques
            flw_cnt+=1
            resp.append(1)
            Pump_inp(root,flw_cnt)
            if flw_cnt>4:
                lb_ques.destroy()
                btn_yes.destroy()
                btn_no.destroy()
                root.update()
            Start()

        def no():
            global resp, flw_cnt, ques
            flw_cnt+=1
            resp.append(0)
            if flw_cnt>4:
                lb_ques.destroy()
                btn_yes.destroy()
                btn_no.destroy()
                root.update()
            Start()

        btn_yes.configure(command=Yes)
        btn_yes.place(x=450,y=400)
        btn_no.configure(command=no)
        btn_no.place(x=950,y=400)
        #lb_resp.configure(text=str(resp))

    if flw_cnt==5:
        def AI_Start():
            bt_strt_ai.destroy()
            root.config(bg='black')

            calc_thrd = Thread(target=ALL_Calc, daemon=True, args=(root, pic,0))
            calc_thrd.start()
            
            
        photo = PhotoImage(file = "AIClick.png")
        photoimage = photo.subsample(1, 1)
        try:
            bt_strt_ai = Button(root, command=AI_Start, bg='#252525', image = photoimage, relief=FLAT)
            bt_strt_ai.pack()
        except:
            pass
        
        

root = Tk()
root.title("Hill Irrigation Optimizer")
root.iconbitmap("icon.ico")
root.config(bg='#252525')
root.state('zoomed')

scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()

photo = PhotoImage(file = "WELCOME.png")
photoimage = photo.subsample(2, 2)

obj_yes = PhotoImage(file = "yes.png")
img_yes = obj_yes.subsample(2, 2)

obj_no = PhotoImage(file = "no.png")
img_no = obj_no.subsample(2, 2)

lb_ques = Label(root, bg='#252525',width=1950)

#lb_resp = Label(root, text=str(resp),bg="#252525",fg='white')
#lb_resp.pack(side=BOTTOM)

bt_strt = Button(root, command=Start, bg='#252525', width=246, image = photoimage, relief=FLAT, height=35)
bt_strt.place(x=scr_width/2-246/2, y=scr_height/2-100)

btn_no = Button(root, bg="#252525", image=img_no, relief=FLAT)
btn_yes = Button(root, bg="#252525", image=img_yes, relief=FLAT)
try:
    y=Thread(target=Float)
    y.start()
except:
    y.join()
finally:
    pass

pic = PhotoImage(file="output_pnl.png")

root.mainloop()
