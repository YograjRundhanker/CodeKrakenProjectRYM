from tkinter import *
from customtkinter import *
import win32gui
import win32con



def Pump_inp(root,ques):
    top_win = Toplevel(root)
    hwnd = top_win.winfo_id()
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 240, win32con.LWA_ALPHA)
    top_win.attributes("-alpha", 1)

    set_default_color_theme("dark-blue")
    fp = open('Inputs.txt','a')

#================================================================River============================================================#

    def River():
        pnl = Frame(top_win, bg='#202020')
        pnl.pack(pady=50)        
        lb_sprl_inp1 = CTkLabel(pnl,text_color ='white', text='Height-river',font =('Calibri',18))
        tx_sprl_inp1 = CTkEntry(pnl,font =('Calibri',18),placeholder_text='metre')
        lb_sprl_inp2 = CTkLabel(pnl,text_color ='white', text='Atm Pressure',font =('Calibri',18))
        tx_sprl_inp2 = CTkEntry(pnl,font =('Calibri',18), placeholder_text='n pascal')
        lb_sprl_inp3 = CTkLabel(pnl,text_color ='white', text='Wheel Diameter',font =('Calibri',18))
        tx_sprl_inp3 = CTkEntry(pnl,font =('Calibri',18), placeholder_text='n feet')
        
        lb_sprl_inp1.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        tx_sprl_inp1.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        lb_sprl_inp2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        tx_sprl_inp2.grid(row=2, column=2, padx=10, pady=10, sticky='w')
        lb_sprl_inp3.grid(row=3, column=1, padx=10, pady=10, sticky='w')
        tx_sprl_inp3.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        def RiverInput():
            height = tx_sprl_inp1.get()
            atm_prs = tx_sprl_inp2.get()
            whl_diam = tx_sprl_inp3.get()
            fp.writelines([height,'\n',atm_prs,'\n',whl_diam,'\n'])
            fp.close()
            top_win.destroy()
        
        btn_submit = CTkButton(top_win, font =('Calibri',18), text = "SUBMIT", command = RiverInput)
        btn_submit.pack(side="bottom")

#================================================================Hydram============================================================#

    def Hydram():
        pnl = Frame(top_win, bg='#202020')
        pnl.pack(pady=50)        
        lb_hydrm_inp1 = CTkLabel(pnl,text_color ='white', text='Waterfall Height',font =('Calibri',18))
        tx_hydrm_inp1 = CTkEntry(pnl,font =('Calibri',18),placeholder_text='less than 30m')
        lb_hydrm_inp2 = CTkLabel(pnl,text_color ='white', text='Water In-Flow Rate',font =('Calibri',18))
        tx_hydrm_inp2 = CTkEntry(pnl,font =('Calibri',18), placeholder_text='Lt/Hr')
        
        lb_hydrm_inp1.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        tx_hydrm_inp1.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        lb_hydrm_inp2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        tx_hydrm_inp2.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        def HydramInput():
            elev = tx_hydrm_inp1.get()
            inflw = tx_hydrm_inp2.get()
            fp.writelines([elev,'\n',inflw,'\n'])
            fp.close()
            top_win.destroy()
        
        btn_submit = CTkButton(top_win, font =('Calibri',18), text = "SUBMIT", command = HydramInput)
        btn_submit.pack(side="bottom")

#================================================================Capillary============================================================#

    def Capillary():
        pnl = Frame(top_win, bg='#202020')
        pnl.pack(pady=50)        
        lb_cplry_inp1 = CTkLabel(pnl,text_color ='white', text='Site Elevation',font =('Calibri',18))
        tx_cplry_inp1 = CTkEntry(pnl,font =('Calibri',18),placeholder_text='less than 200m')
        lb_cplry_inp2 = CTkLabel(pnl,text_color ='white', text='Atmospheric Pressure',font =('Calibri',18))
        tx_cplry_inp2 = CTkEntry(pnl,font =('Calibri',18), placeholder_text='PSI')
        
        lb_cplry_inp1.grid(row=1, column=1, padx=10, pady=10, sticky='w')
        tx_cplry_inp1.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        lb_cplry_inp2.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        tx_cplry_inp2.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        def CapInput():
            height = tx_cplry_inp1.get()
            atm_prs = tx_cplry_inp2.get()
            fp.writelines([height,'\n',atm_prs,'\n'])
            fp.close()
            top_win.destroy()
        
        btn_submit = CTkButton(top_win, font =('Calibri',18), text = "SUBMIT", command = CapInput)
        btn_submit.pack(side="bottom")

#================================================================Water============================================================#

    def Water():
        pnl = Frame(top_win, bg='#202020')
        pnl.pack(pady=50)        
        lb_h2o_inp1 = CTkLabel(pnl,text_color ='white', text='Required Water Quantity',font =('Calibri',18))
        tx_h2o_inp1 = CTkEntry(pnl,font =('Calibri',18),placeholder_text='Litres')
        
        lb_h2o_inp1.pack(pady=10)
        tx_h2o_inp1.pack(pady=10)

        def HydroInput():
            water_qty = tx_h2o_inp1.get()
            fp.writelines([water_qty,'\n'])
            fp.close()
            top_win.destroy()
        
        btn_submit = CTkButton(top_win, font =('Calibri',18), text = "SUBMIT", command = HydroInput)
        btn_submit.pack(side="bottom")

#================================================================BUDGET============================================================#

    def Budget():
        pnl = Frame(top_win, bg='#202020')
        pnl.pack(pady=50)        
        lb_bdgt_inp1 = CTkLabel(pnl,text_color ='white', text='Budget Limit',font =('Calibri',18))
        tx_bdgt_inp1 = CTkEntry(pnl,font =('Calibri',18),placeholder_text='Rupees')
        
        lb_bdgt_inp1.pack(pady=40)
        tx_bdgt_inp1.pack(pady=10)

        def INRinp():
            bdgt = tx_bdgt_inp1.get()
            fp.writelines([bdgt,'\n'])
            fp.close()
            top_win.destroy()
        
        btn_submit = CTkButton(top_win, font =('Calibri',18), text = "SUBMIT", command = INRinp)
        btn_submit.pack(side="bottom")

#=====================================================================================================================================#
    
    top_win.title("Child Window")
    top_win.overrideredirect(True)
    top_win.config(bg='#202020')

    top_win.geometry('950x450+290+200')
    
    pump = ['RIVER PUMP',"HYDRAM","CAPILLARY","BUDGET DETAILS","IRRIGATION QUANTITY"]
    
    
    lb_head = Label(top_win, fg='white', bg='#252525', text=pump[ques-1], font=["Times New Roman",26])
    lb_head.pack()

    if ques==1:
        River()

    if ques==2:
        Hydram()

    if ques==3:
        Capillary()

    if ques==4:
        Budget()

    if ques==5:
        Water()

    top_win.grab_set()

