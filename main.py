import tkinter as tk
from tkinter import ttk, messagebox
import json
import asyncio

# from appMobile.appStartHome import getInfoHgu
# from magic_ssh import control_ssh
# from appMobile import appStartHome

LARGEFONT = ("Verdana", 35)
# colors
color_0 = "#f0f3f5"  # black
color_1 = "#0055a0"  # azul
color_2 = "#6a4f9c"  # azul claro
color_3 = "#38576b"  # value
color_4 = "#ffffff"  # letters
cor_bg_all = '#D9D9D9'  # +/- cinza
roxo = '#9400D3'
branco = "#ffffff"
verde = '#008000'
preto = '#000000'


# global variables


def verify_connection(string):
    if string == 'connected':
        return Page2
    else:
        messagebox.showerror(title="Não conectado", message="Houve um erro na autenticação")
        return Page_home


class Metodos():
    def __init__(self, slid, ip, senha_hgu, rede_vivo):
        self.__slid = slid
        self.__ip = ip
        self.__senha_hgu = senha_hgu
        self.__rede_vivo = rede_vivo

    def set_slid(self, novo_slid):
        self.__slid = novo_slid

    def get_slid(self):
        return self.__slid

    def set_ip(self, new_ip):
        self.__ip = new_ip

    def get_ip(self):
        return self.__ip

    def set_senha_hgu(self, new_password):
        self.__senha_hgu = new_password

    def get_senha_hgu(self):
        return self.__senha_hgu

    def set_vivo(self, new_value):
        self.__rede_vivo = new_value

    def get_vivo(self):
        return self.__rede_vivo


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page_home, Page2, Page_requirements, Page_process, Page_config_wan, Page_config_lan,\
                Page_config_snmp, Page_config_wifi_2G, Page_config_wifi_5G, Page_config_icmp, Page_Finally_processes):
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
        self.label_1.place(x=410, y=330)

        self.entry_name = tk.Entry(self, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        self.entry_name.place(x=410, y=360)

        self.label_2 = tk.Label(self, text="Senha:", font=("", 12))
        self.label_2.place(x=410, y=400)

        self.entry_pass = tk.Entry(self, width=25, justify='left', show='*', font=("", 15), highlightthickness=1,
                                   relief='solid')
        self.entry_pass.place(x=410, y=430)

        credencials = ['t', 't']

        button1 = ttk.Button(self, text="Login", cursor='hand2', command=lambda: controller.show_frame(Page_home))
        # if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button1.place(x=520, y=490)


class Page_home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=cor_bg_all)

        # image central magic
        self.magic_img = tk.PhotoImage(file="images/Logo_Magic_CompletoCentralPequeno_resized_resized.png")
        self.magic_label_img = tk.Label(self, image=self.magic_img, width=400, height=300, bg=cor_bg_all)
        self.magic_label_img.place(x=500, y=70)

        self.choice_service = tk.Label(self, text="Serviços a ser configurado", font=('Ivy 12'), bg=cor_bg_all)
        self.choice_service.place(x=100, y=100)

        self.ip_ligth = tk.Button(self, text="IP Light", cursor='hand2', font=('Ivy 12'), width=16, height=2,
                                  bg=cor_bg_all, command=lambda: [
                controller.show_frame(Page_requirements),
            ])
        self.ip_ligth.place(x=115, y=150)

        self.label_copyrigth = tk.PhotoImage(file="images/icons8-copyright-50_resized.png")
        self.copy_label_img = tk.Label(self, image=self.label_copyrigth, bg=cor_bg_all, width=40)
        self.copy_label_img.place(x=320, y=525)

        # legend rodape
        label_copy_legend = tk.Label(self, text="Centro de Desenvolvimento de Dispositivos", font=('Ivy 12'),
                                     bg=cor_bg_all)
        label_copy_legend.place(x=354, y=525)


class Page_requirements(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg=branco)

        with open('param_iplight.json', 'r') as meu_json:
            date = json.load(meu_json)

        value_1 = date['slid']
        value_2 = date['ip']
        value_3 = date['senha_hgu']
        value_4 = date['rede']

        self.area_inputs = tk.Label(self, text='', bg=cor_bg_all, width=75, height=20).place(x=300, y=160)

        # Label auth
        self.label_auth = tk.Label(self, text="Preencha as informações abaixo", font=('Ivy 14'), fg=roxo, bg=cor_bg_all)
        self.label_auth.place(x=310, y=170)

        # img superior
        self.magic_img = tk.PhotoImage(file="images/logo_magic_180x150_resized.png")
        self.magic_label_img = tk.Label(self, image=self.magic_img, width=200, height=140, bg=branco)
        self.magic_label_img.place(x=150, y=0)

        # label nao autenticado
        # self.label_auth = tk.Label(self, text="Preencha as informações abaixo",  font=('Ivy 11'), fg=preto, bg=cor_bg_all)
        # self.label_auth.place(x=370, y=220)

        # label SLID
        self.label_auth = tk.Label(self, text="SLID : ", font=('Ivy 11'), fg=preto, bg=cor_bg_all)
        self.label_auth.place(x=455, y=225)
        self.slid = tk.Entry(self, width=25, font=('Ivy 10'), justify='center')
        self.slid.place(x=500, y=227)

        # label IP HGU
        self.label_iphgu = tk.Label(self, text="IP : ", font=('Ivy 11'), fg=preto, bg=cor_bg_all)
        self.label_iphgu.place(x=473, y=260)
        self.ip_hgu = tk.Entry(self, width=25, font=('Ivy 10'), justify='center')
        self.ip_hgu.place(x=500, y=262)
        self.ip_hgu.insert(0, value_2)

        # label Password HGU
        self.label_senha = tk.Label(self, text="Senha HGU : ", font=('Ivy 11'), fg=preto, bg=cor_bg_all)
        self.label_senha.place(x=410, y=295)
        self.senha_hgu = tk.Entry(self, width=25, font=('Ivy 10'), justify='center')
        self.senha_hgu.place(x=500, y=297)

        #radioButton
        style = ttk.Style()
        style.configure("Wild.TRadiobutton",
                        background=cor_bg_all)

        self.selected = tk.StringVar()
        self.vivo1 = ttk.Radiobutton(self, style="Wild.TRadiobutton" ,text='VIVO1',value='VIVO1', variable=self.selected)
        self.vivo1.place(x=510, y=330)
        self.vivo2 = ttk.Radiobutton(self, style="Wild.TRadiobutton", text='VIVO2', value='VIVO2', variable=self.selected)
        self.vivo2.place(x=600, y=330)

        # long-in hgu
        # status =[]
        # senha_hgu = []
        # page_rendering = []
        # conn = connect
        self.login = tk.Button(self, text='Configurar', bg=verde, cursor='hand2', fg=branco, width=9, height=1,
                               command=lambda: [
                                   controller.show_frame(Page_process),self.save_param_iplight(self.slid, self.ip_hgu, self.senha_hgu, self.selected)
                               ])  # controller.show_frame(Page_connection)]) #connect(ip_hgu=self.ip_hgu.get(), pwd_hgu=self.password_hgu.get())
        self.login.place(x=620, y=400)
        self.voltar = tk.Button(self, text='Voltar', bg=verde, fg=branco, width=9, height=1, cursor='hand2',
                                command=lambda: controller.show_frame(Page_home))
        self.voltar.place(x=500, y=400)

    def save_param_iplight(self, slid, ip_hgu, senha_hgu, selected):

        update = {"slid": slid.get(), "ip": ip_hgu.get(), "senha_hgu": senha_hgu.get(), "rede": selected.get()}

        with open('param_iplight.json', 'w') as f:
            json.dump(update, f)
        

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # "param_snmp.json", encoding='utf-8'
        with open('param_snmp.json', 'r') as meu_json:
            date = json.load(meu_json)

        value_1 = date['remote_mgtm_geral']
        value_2 = date['server_port']
        value_3 = date['server_access']
        value_4 = date['snmpv3']
        value_5 = date['secured_client_ip_address']
        value_6 = date['from_1']

        value_7 = date['from_2']
        value_8 = date['from_3']
        value_9 = date['from_4']
        value_10 = date['to_1']
        value_11 = date['to_2']
        value_12 = date['to_3']
        value_13 = date['to_4']
        value_14 = date['get_community']
        value_15 = date['set_community']
        value_16 = date['trap_community']
        value_17 = date['ipv4_trap_destination']
        value_18 = date['ipv6_trap_destination']

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

        buttom_5 = tk.Button(self, text='Voltar', font='4', cursor='hand2',
                             command=lambda: controller.show_frame(Page_home))
        buttom_5.place(x=300, y=500)
        buttom_6 = tk.Button(self, text='Configurar', font='4', cursor='hand2',
                             command=lambda: [self.snmp_configure(selected_1,
                                                                  selected_2, selected_3, radium_select_1,
                                                                  radium_select_2,
                                                                  radium_select_3, entry_1, entry_2, entry_3, entry_4,
                                                                  entry_5, entry_6, entry_7,
                                                                  entry_8, entry_9, entry_10, entry_11, entry_12,
                                                                  entry_13, entry_14, entry_15)])
        # , control_ssh('192.168.15.1', 'bmsrt5vk')]),  getInfoHgu(pwd='c9695a62', ip_addr='192.168.15.1')

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

        # text = json.dumps(date, indent=2)

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

        update = {"remote_mgtm_geral": value_1,
                           "server_port": entry_1.get(), "server_access": entry_2.get(),
                           "snmpv3": value_4, "secured_client_ip_address": value_5,
                           "from_1": entry_3.get(), "from_2": entry_4.get(),
                           "from_3": entry_5.get(), "from_4": entry_6.get(),
                           "to_1": entry_7.get(), "to_2": entry_8.get(),
                           "to_3": entry_9.get(), "to_4": entry_10.get(),
                           "get_community": entry_11.get(), "set_community": entry_12.get(),
                           "trap_community": entry_13.get(), "ipv4_trap_destination": entry_14.get(),
                           "ipv6_trap_destination": entry_15.get()}

        with open('param_snmp.json', 'w') as f:
            json.dump(update, f)


class Page_process(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text="Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Aguarde enquanto configuramos o dispositivo", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
        self.awaiting2 = tk.Label(self, text="Aguardando").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        self.awaiting3 = tk.Label(self, text="Aguardando").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
        self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300)
        self.awaiting6 = tk.Label(self, text="Aguardando").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_config_wan))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=1000, y=520)

class Page_config_wan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        self.awaiting = tk.Label(self, text="Em execução").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
        self.awaiting2 = tk.Label(self, text="Aguardando").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        self.awaiting3 = tk.Label(self, text="Aguardando").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
        self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300)
        self.awaiting6 = tk.Label(self, text="Aguardando").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_config_lan))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=1000, y=520)

class Page_config_lan(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        #self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
        self.awaiting2 = tk.Label(self, text="Em execução").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        self.awaiting3 = tk.Label(self, text="Aguardando").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
        self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300)
        self.awaiting6 = tk.Label(self, text="Aguardando").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_config_snmp))
        button_next.place(x=1000, y=520)

class Page_config_snmp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        #self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
        #self.awaiting2 = tk.Label(self, text="Em execução").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        self.awaiting3 = tk.Label(self, text="Em execução").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
        self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300)
        self.awaiting6 = tk.Label(self, text="Aguardando").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_config_wifi_2G))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=1000, y=520)


class Page_config_wifi_2G(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        #self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
        #self.awaiting2 = tk.Label(self, text="Aguardando").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        #self.awaiting3 = tk.Label(self, text="Em execução").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
        self.awaiting4 = tk.Label(self, text="Em execução").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300)
        self.awaiting6 = tk.Label(self, text="Aguardando").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_config_wifi_5G))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=1000, y=520)


class Page_config_wifi_5G(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        #self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
        #self.awaiting2 = tk.Label(self, text="Aguardando").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        #self.awaiting3 = tk.Label(self, text="Aguardando").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
        #self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        self.awaiting5 = tk.Label(self, text="Em execução").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300)
        self.awaiting6 = tk.Label(self, text="Aguardando").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_config_icmp))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=1000, y=520)

class Page_config_icmp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
        #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        #self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
       # self.awaiting2 = tk.Label(self, text="Aguardando").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        #self.awaiting3 = tk.Label(self, text="Aguardando").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
       # self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        #self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.empty}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300,)
        self.awaiting6 = tk.Label(self, text="Em execução").place(x=825, y=340)

        button_next = ttk.Button(self, text="Avançar", cursor='hand2', command=lambda : controller.show_frame(Page_Finally_processes))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=1000, y=520)


class Page_Finally_processes(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label_name_config = tk.Label(self, text=" Satus Configurações IP Ligth", font=('Ivy 12'))
        self.label_name_config.place(x=100, y=50)

        #icons state
        self.empty = 'circle_empty'
        self.checked = 'checked'
        self.circle_erro = 'circle'

        self.name_config = tk.Label(self, text="Veja o resultados das configurações IP Ligth", font=('Ivy 12'))
        self.name_config.place(x=375, y=200)

        #for page in (Function_connect_hgu, Wlan_config):
        self.text_hgu_config = tk.Label(self, text='Configuração SLID', font=('Ivy 10'))
        self.text_hgu_config.place(x=150, y=260)
        self.icon_executing = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon = tk.Label(self, image=self.icon_executing)
        self.label_icon.place(x=185, y=300)
       #self.label_execution=tk.Label(self, text="Em execução").place(x=165, y=340)

        #wan config
        self.text_wan_config = tk.Label(self, text='Cofiguração Wan', font=('Ivy 10'))
        self.text_wan_config.place(x=280, y=260)
        self.icon_executing_wan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wan = tk.Label(self, image=self.icon_executing_wan)
        self.label_icon_wan.place(x=310, y=300)
        #self.awaiting = tk.Label(self, text="Aguardando").place(x=290, y=340)

        #lan
        self.text_lan_config = tk.Label(self, text='Cofiguração Lan', font=('Ivy 10'))
        self.text_lan_config.place(x=390, y=260)
        self.icon_executing_lan = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_lan = tk.Label(self, image=self.icon_executing_lan)
        self.label_icon_lan.place(x=425, y=300)
       # self.awaiting2 = tk.Label(self, text="Aguardando").place(x=410, y=340)

        # snmp
        self.text_snmp_config = tk.Label(self, text='Cofiguração SNMP', font=('Ivy 10'))
        self.text_snmp_config.place(x=497, y=260)
        self.icon_executing_snmp = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_snmp = tk.Label(self, image=self.icon_executing_snmp)
        self.label_icon_snmp.place(x=530, y=300)
        #self.awaiting3 = tk.Label(self, text="Aguardando").place(x=510, y=340)

       
        #Rede Wi-Fi 2.4 GHz
        self.text_wifi2_config = tk.Label(self, text='WI-FI 2.4 GHz', font=('Ivy 10'))
        self.text_wifi2_config.place(x=620, y=260)
        self.icon_executing_wifi2 = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wifi2g = tk.Label(self, image=self.icon_executing_wifi2)
        self.label_icon_wifi2g.place(x=652, y=300)
       # self.awaiting4 = tk.Label(self, text="Aguardando").place(x=630, y=340)

        #Rede Wi-Fi 5 GHz
        self.text_wifi5_config = tk.Label(self, text='WI-FI 5 GHz', font=('Ivy 10'))
        self.text_wifi5_config.place(x=720, y=260)
        self.icon_executing_wifi5 = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_wifi5g = tk.Label(self, image=self.icon_executing_wifi5)
        self.label_icon_wifi5g.place(x=745, y=300)
        #self.awaiting5 = tk.Label(self, text="Aguardando").place(x=725, y=340)

        #Habilitar ICMP
        self.text_icmp_config = tk.Label(self, text='Configuração ICMP', font=('Ivy 10'))
        self.text_icmp_config.place(x=810, y=260)
        self.icon_executing_icmp = tk.PhotoImage(file=f"images/{self.checked}.png")
        self.label_icon_icmp = tk.Label(self, image=self.icon_executing_icmp)
        self.label_icon_icmp.place(x=845, y=300,)
        #self.awaiting6 = tk.Label(self, text="Em execução").place(x=825, y=340)

        button_next = ttk.Button(self, text="Finalizar", cursor='hand2', command=lambda : controller.show_frame(Page_home))
        #if credencials[0] == entry_name.get() and credencials[1] == entry_pass.get() else messagebox.showinfo('Login ou senha incorreta!')
        button_next.place(x=520, y=560)

        self.congrats = tk.Label(self, text="Parabéns", font=("Ivy 13")).place(x=520, y=500)
        self.congrats = tk.Label(self, text="Todas as cofigurações foram feitas com sucesso", font=("Ivy 10")).place(x=420, y=530)


app = tkinterApp()
app.geometry('1100x600')
app.title('MagicTool B2B')
app.resizable(False, False)
app.config(bg=cor_bg_all)
# app.attributes('-fullscreen',True)
app.mainloop()

