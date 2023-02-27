import tkinter as tk
from tkinter import ttk, messagebox
import json

from appMobile.appStartHome import getInfoHgu
from magic_ssh import control_ssh
from appMobile import appStartHome

LARGEFONT = ("Verdana", 35)
# colors
color_0 = "#f0f3f5" # black
color_1 = "#0055a0" # azul
color_2 = "#6a4f9c" # azul claro
color_3 = "#38576b" # value
color_4 = "#ffffff" # letters

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)


        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global img
        img = tk.PhotoImage(file='images/Logo_Magic_CompletoCentralPequeno.png')
        self.label_0 = tk.Label(self, image=img)
        self.label_0.place(x=450, y=110)


        self.label_1 = tk.Label(self, text="Nome:", font=("", 12))
        self.label_1.place(x=410, y=360)

        self.entry_name = tk.Entry(self, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        self.entry_name.place(x=410, y=400)

        self.label_2 = tk.Label(self, text="Senha:", font=("", 12))
        self.label_2.place(x=410, y=460)

        self.entry_pass = tk.Entry(self, width=25, justify='left', show='*', font=("", 15), highlightthickness=1,relief='solid')
        self.entry_pass.place(x=410, y=500)


        credencials = ['t', 't']

        button1 = ttk.Button(self, text="Login", command=lambda : controller.show_frame(Page1))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button1.place(x=520, y=600)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global img2
        img2 = tk.PhotoImage(file='images/Logo_Magic_CompletoPequeno.png')
        self.label_0 = tk.Label(self, image=img2)
        self.label_0.place(x=470, y=170)

        button_1 = tk.Button(self, text='SNMP', font=('Ivy 20'), bg=color_2, fg=color_4, justify='center', width=15, height=2, command=lambda: controller.show_frame(Page2))
        button_1.place(x=120, y=20)
        button_2 = tk.Button(self, text='WIFI', font=('Ivy 20'), bg=color_2, fg=color_4, justify='center', width=15, height=2)
        button_2.place(x=120, y=150)
        button_3 = tk.Button(self, text='DNS', font=('Ivy 20'), bg=color_2, fg=color_4, justify='center', width=15, height=2)
        button_3.place(x=120, y=280)
        button_4 = tk.Button(self, text='CONECTIVIDADE', font=('Ivy 20'), bg=color_2, fg=color_4, justify='center', width=15, height=2)
        button_4.place(x=120, y=410)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        with open("b2b.json", encoding='utf-8') as meu_json:
            date = json.load(meu_json)

        value_1 = date['snmp']['remote_mgtm_geral']
        value_2 = date['snmp']['server_port']
        value_3 = date['snmp']['server_access']
        value_4 = date['snmp']['snmpv3']
        value_5 = date['snmp']['secured_client_ip_address']
        value_6 = date['snmp']['from_1']
        value_7 = date['snmp']['from_2']
        value_8 = date['snmp']['from_3']
        value_9 = date['snmp']['from_4']
        value_10 = date['snmp']['to_1']
        value_11 = date['snmp']['to_2']
        value_12 = date['snmp']['to_3']
        value_13 = date['snmp']['to_4']
        value_14 = date['snmp']['get_community']
        value_15 = date['snmp']['set_community']
        value_16 = date['snmp']['trap_community']
        value_17 = date['snmp']['ipv4_trap_destination']
        value_18 = date['snmp']['ipv6_trap_destination']

        label_0 = tk.Label(self, text='Consultar Monitoramento por SNMP', font='4')
        label_0.grid(column=1, row=1, sticky='w', padx=10, pady=10)
        label_1 = tk.Label(self, text='Remote MGTM Geral', font='4')
        label_1.grid(column=1, row=3, sticky='w', padx=10)
        label_2 = tk.Label(self, text='SNMP', font='4')
        label_2.grid(column=1, row=4, sticky='w', padx=10)
        label_3 = tk.Label(self, text='Server Port', font='4')
        label_3.grid(column=1, row=5, sticky='w', padx=10)
        entry_1 = tk.Entry(self, font='4')
        entry_1.insert(0, value_2)
        entry_1.grid(column=3, row=5, sticky='w')
        label_4 = tk.Label(self, text='Server Access', font='4')
        label_4.grid(column=1, row=6, sticky='w', padx=10)
        entry_2 = tk.Entry(self, font='4')
        entry_2.insert(0, value_3)
        entry_2.grid(column=3, row=6, sticky='w')
        label_5 = tk.Label(self, text='SNMPv3', font='4')
        label_5.grid(column=1, row=7, sticky='w', padx=10)
        label_6 = tk.Label(self, text='Secured Client IP Address', font='4')
        label_6.grid(column=1, row=8, sticky='w', padx=10)
        label_7 = tk.Label(self, text='From', font='4')
        label_7.grid(column=3, row=9, sticky='e')
        entry_3 = tk.Entry(self, font='4')
        entry_3.grid(column=4, row=9, sticky='w', padx=10)
        entry_3.insert(0, value_6)
        label_8 = tk.Label(self, text='From', font='4')
        label_8.grid(column=3, row=10, sticky='e')
        entry_4 = tk.Entry(self, font='4')
        entry_4.grid(column=4, row=10, sticky='w', padx=10)
        entry_4.insert(0, value_7)
        label_9 = tk.Label(self, text='From', font='4')
        label_9.grid(column=3, row=11, sticky='e')
        entry_5 = tk.Entry(self, font='4')
        entry_5.grid(column=4, row=11, sticky='w', padx=10)
        entry_5.insert(0, value_8)
        label_10 = tk.Label(self, text='From', font='4')
        label_10.grid(column=3, row=12, sticky='e')
        entry_6 = tk.Entry(self, font='4')
        entry_6.grid(column=4, row=12, sticky='w', padx=10)
        entry_6.insert(0, value_9)
        label_11 = tk.Label(self, text='To', font='4')
        label_11.grid(column=5, row=9, sticky='w', padx=10)
        entry_7 = tk.Entry(self, font='4')
        entry_7.insert(0, value_10)
        entry_7.grid(column=6, row=9, sticky='w')
        label_12 = tk.Label(self, text='To', font='4')
        label_12.grid(column=5, row=10, sticky='w', padx=10)
        entry_8 = tk.Entry(self, font='4')
        entry_8.grid(column=6, row=10, sticky='w')
        entry_8.insert(0, value_11)
        label_13 = tk.Label(self, text='To', font='4')
        label_13.grid(column=5, row=11, sticky='w', padx=10)
        entry_9 = tk.Entry(self, font='4')
        entry_9.grid(column=6, row=11, sticky='w')
        entry_9.insert(0, value_12)
        label_14 = tk.Label(self, text='To', font='4')
        label_14.grid(column=5, row=12, sticky='w', padx=10)
        entry_10 = tk.Entry(self, font='4')
        entry_10.grid(column=6, row=12, sticky='w')
        entry_10.insert(0, value_13)
        label_15 = tk.Label(self, text='Get Community:', font='4')
        label_15.grid(column=1, row=13, sticky='w', padx=10)
        entry_11 = tk.Entry(self, font='4')
        entry_11.grid(column=3, row=13, sticky='w')
        entry_11.insert(0, value_14)
        label_16 = tk.Label(self, text='Set Community:', font='4')
        label_16.grid(column=1, row=14, sticky='w', padx=10)
        entry_12 = tk.Entry(self, font='4')
        entry_12.grid(column=3, row=14, sticky='w')
        entry_12.insert(0, value_15)
        label_17 = tk.Label(self, text='Trap Community:', font='4')
        label_17.grid(column=1, row=15, sticky='w', padx=10)
        entry_13 = tk.Entry(self, font='4')
        entry_13.grid(column=3, row=15, sticky='w')
        entry_13.insert(0, value_16)
        label_18 = tk.Label(self, text='IPv4 Trap Destination', font='4')
        label_18.grid(column=1, row=16, sticky='w', padx=10)
        entry_14 = tk.Entry(self, font='4')
        entry_14.grid(column=3, row=16, sticky='w')
        entry_14.insert(0, value_17)
        label_19 = tk.Label(self, text='IPv6 Trap Destination', font='4')
        label_19.grid(column=1, row=17, sticky='w', padx=10)
        entry_15 = tk.Entry(self, font='4')
        entry_15.grid(column=3, row=17, sticky='w')
        entry_15.insert(0, value_18)

        buttom_5 = tk.Button(self, text='Voltar', font='4', command = lambda: controller.show_frame(Page1))
        buttom_5.place(x=300, y=500)
        buttom_6 = tk.Button(self, text='Configurar', font='4', command = lambda: [self.snmp_configure(selected_1,
                        selected_2, selected_3, radium_select_1, radium_select_2,
                        radium_select_3, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7,
                        entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15), control_ssh('192.168.15.1', 'bmsrt5vk')]) #getInfoHgu(pwd='c9695a62', ip_addr='192.168.15.1')

        buttom_6.place(x=700, y=500)

        selected_1 = tk.IntVar()
        radium_1 = tk.Radiobutton(self, text='Rejeita', value=1, variable=selected_1)
        radium_1.grid(column=3, row=3, sticky='w')
        radium_2 = tk.Radiobutton(self, text='Aceita', value=2, variable=selected_1)
        radium_2.grid(column=4, row=3, sticky='w')
        radium_select_1 = selected_1.get()

        selected_2 = tk.IntVar()
        radium_3 = tk.Radiobutton(self, text='Enable', value=1, variable=selected_2)
        radium_3.grid(column=3, row=7, sticky='w')
        radium_4 = tk.Radiobutton(self, text='Disable', value=2, variable=selected_2)
        radium_4.grid(column=4, row=7, stick='w')
        radium_select_2 = selected_2.get()

        selected_3 = tk.IntVar()
        radium_5 = tk.Radiobutton(self, text='ALL', value=1, variable=selected_3)
        radium_5.grid(column=3, row=8, sticky='w')
        radium_select_3 = selected_3.get()

        #text = json.dumps(date, indent=2)

    def snmp_configure(self, selected_1, selected_2, selected_3, radium_select_1, radium_select_2,
                       radium_select_3, entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7,
                       entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15):
        if radium_select_1 == 1:
            value_1 = "Rejeita"
        elif radium_select_1 == 2:
            value_1 = "Aceita"
        else:
            value_1 = ""

        if radium_select_2 == 1:
            value_4 = "Enable"
        elif radium_select_2 == 2:
            value_4 = "Disable"
        else:
            value_4 = ""

        if radium_select_3 == 1:
            value_5 = "ALL"
        else:
            value_5 = ""

        update = { "snmp": { "remote_mgtm_geral": value_1,
                "server_port": entry_1.get(), "server_access": entry_2.get(),
                "snmpv3": value_4, "secured_client_ip_address": value_5,
                "from_1": entry_3.get(), "from_2": entry_4.get(),
                "from_3": entry_5.get(), "from_4": entry_6.get(),
                "to_1": entry_7.get(), "to_2": entry_8.get(),
                "to_3": entry_9.get(), "to_4": entry_10.get(),
                "get_community": entry_11.get(), "set_community": entry_12.get(),
                "trap_community": entry_13.get(), "ipv4_trap_destination": entry_14.get(),
                "ipv6_trap_destination": entry_15.get() } }

        with open('b2b.json', 'w') as f:
            json.dump(update, f)




app = tkinterApp()
app.geometry('1100x750')
# app.attributes('-fullscreen',True)
app.mainloop()