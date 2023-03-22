import socket
from tkinter import *
from message import chat_message,join_message
from popup import popup_erreur,popup_reglage
from tkinter import ttk
import threading
import datetime
import pickle
import subprocess



host = "88.175.12.245"
localhost="localhost"
port = 55555
home_fen = ""
name = ""
msg= ""
list_name_test = []

color_theme = {"principale":"#0B162C","secondaire":"#5FC2BA","troisieme":"#3B556D", "font":"#FFFFFF"}
nb_message = -1
chat_fen = Tk()
chat_fen.title("PyChat")
chat_fen.geometry("1300x700")
chat_fen.configure(bg=color_theme["principale"])
chat_fen.withdraw()

chat_box = Canvas(chat_fen, bg=color_theme["font"],background=color_theme["troisieme"])
chat_box.place(x=310, y=110, width=950, height=500) 


scrollbar = Scrollbar(chat_fen, orient="vertical", command=chat_box.yview)
scrollbar.place(x=1260, y=110, height=500)
chat_box.configure(yscrollcommand=scrollbar.set)
frame = Frame(chat_box, bg=color_theme["troisieme"])
chat_box.create_window((0, 0), window=frame, anchor='nw')
list_name = Canvas(chat_fen, bg=color_theme["font"],background=color_theme["troisieme"])
list_name.place(x=10, y=110, width=280, height=500) 
scrollbar2 = Scrollbar(chat_fen, orient="vertical", command=list_name.yview)
scrollbar2.place(x=290, y=110, height=500)
list_name.configure(yscrollcommand=scrollbar2.set)
frame2 = Frame(list_name, bg=color_theme["troisieme"])
list_name.create_window((0, 0), window=frame2, anchor='nw')




color_user = ""
color_traduction = {"Noir":"black","Rouge":"red","Bleu":"blue","Violet":"purple","Blanc":"white","Gris":"grey","Vert":"green","Orange":"orange","Marron":"brown","Jaune":"yelow","Rose":"pink","Cyan":"cyan"}

def home_fen1():
    global home_fen,name
    home_fen = Tk()
    nom = StringVar()
    home_fen.configure(bg=color_theme["principale"])
    home_fen.title("PyChat")
    home_fen.geometry("400x400")        
    """test = Canvas(home_fen, width=400, height=400, background="white", highlightthickness=0)
    test.place(x=0, y=0)
    outilcanvas(home_fen,test)"""
    style= ttk.Style()
    style.configure("TCombobox", fieldbackground= color_theme["secondaire"], background= color_theme["secondaire"])    
    def set_color(event):
        global color_user
        color_user = value_color.get()
    label = Label(home_fen, text="Bienvenue sur PyChat",font=("calibre",24,"bold"),bg=color_theme["principale"],fg=color_theme["secondaire"]).place(x=50,y=50)
    Label(home_fen, text="Veuillez rentrer votre pseudo : ",font=("calibre",10,"bold"),bg=color_theme["principale"],fg=color_theme["font"]).place(x=30,y=145)
    Label(home_fen, text="Veuillez choisir votre couleur : ",font=("calibre",10,"bold"),bg=color_theme["principale"],fg=color_theme["font"]).place(x=30,y=200)
    value_color = ttk.Combobox(home_fen,values=list(color_traduction.keys()))
    
    value_color.place(x=220,y=200)
    value_color.current(0)
    value_color.bind('<<ComboboxSelected>>', set_color)
    nom_input = Entry(home_fen,textvariable=nom,font=("calibre",10),bg=color_theme["secondaire"])
    nom_input.place(x=220,y=145)
    def checkforlocalhost(): 
        t = nom_input.get()
        if t =="":
            popup_erreur("VEUILLEZ SAISIR UN NOM")
        else:
            subprocess.call(["python", "serverlocalhost.py"])
            connected(t,localhost)
    def checkforserveur(): 
        t = nom_input.get()
        if t =="":
            popup_erreur("VEUILLEZ SAISIR UN NOM")
        else: 
            connected(t,host)

    btn_connect = Button(home_fen,text="Connecter au serveur principal",bg=color_theme["secondaire"],width=35, command= lambda: checkforserveur()).place_configure(x=75,y=250)
    btn_connect = Button(home_fen,text="Herbegé sa conversation",bg=color_theme["secondaire"],width=35, command= lambda: checkforlocalhost()).place_configure(x=75,y=300)
    
    home_fen.mainloop()
    

def receive_messages(client_socket, frame):
    global nb_message, name, chat_box, is_running,msg,chat_fen
     
    is_running = True
    while is_running:
        try:
            donnees_recues = client_socket.recv(1024)
            if donnees_recues:
                nb_message = nb_message + 1
                donnee_dico = pickle.loads(donnees_recues)
                msg = donnee_dico
                if msg["type"] == "connexion":
                    chat_fen.after(1000, lambda: join_message(msg,nb_message,frame))
                    chat_fen.after(1000, lambda: update_list_frame(msg["user"]))
                elif msg["type"] == "message":
                    chat_fen.after(1000, lambda: chat_message(msg,nb_message,frame))
                """elif msg["type"] != "message" and msg["type"] != "connexion":
                    print("aze")
                    list_user = list(msg.keys())
                    for i in list_user:
                        chat_fen.after(1000, lambda: update_list_frame(i))"""
                print("trouvé",nb_message)
                    
                    
        except Exception as e:
            print(f'Erreur de réception de message: {e}')
            popup_erreur(f'Erreur de réception de message::\n {e}')
            is_running = False
            
def update_list_frame(name):
    global list_name_test
    list_name_test.append(name)
    btn = Button(frame2, text=name,font=("calibre",8,"bold"),width=40, bg=color_theme["secondaire"],fg=color_theme["font"])
    #list_name_frame[name] = btn
    btn.pack()
    
    
def create_popup_reglagecolorchat():
    popup_reglagecolorchat = Tk()
    popup_reglagecolorchat.title("reglage couleur du chat")
    popup_reglagecolorchat.geometry("600x300")
    def set_color(event):
        global color_user
        color_user = value_color.get()
        

    Label(popup_reglagecolorchat,text="reglage du chat",font=("calibre",20,"bold")).place(x=125,y=50)
    Label(popup_reglagecolorchat,text="Veuillez choisir votre nouvelle couleur : ",font=("calibre",8,"bold")).place(x=10,y=150)
    value_color = ttk.Combobox(popup_reglagecolorchat,values=list(color_traduction.keys()))
    value_color.place(x=220,y=200)
    value_color.bind('<<ComboboxSelected>>', set_color)
    Button(popup_reglagecolorchat,text="ok ! ",command= lambda: popup_reglagecolorchat.destroy()).place(x=550,y=250)
    popup_reglagecolorchat.mainloop()
    
def connected(n,host_chanel):
    global client_socket,name,frame
    name = n
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # connexion au serveur
        client_socket.connect((host, port))
        print('Connexion au serveur réussie !')
        heure_actuelle = datetime.datetime.now()
        heure_formatee = heure_actuelle.strftime("%H : %M : %S")
        data = {"user":name,"message":name,"color":color_traduction[color_user],"time":heure_formatee,"type":"connexion"}
        d = pickle.dumps(data)
        client_socket.send(d)
        if chat_box != "":
            threading.Thread(target=receive_messages, args=(client_socket,frame )).start()
            chat_page(client_socket,name)
    except Exception as e:
        print(f'Erreur de connexion au serveur: {e}')
        popup_erreur(f'Erreur de connexion au serveur:\n {e}')
    finally:
        client_socket.close()
        

def on_closing():
    chat_fen.destroy() # Ferme la fenêtre Tkinter
    print("Fermeture de la fenêtre")
    
    for thread in threading.enumerate():
        if thread != threading.main_thread():
            thread.join()
            quit()


    
def chat_page(client_socket,name):
    global is_running,chat_fen,chat_box,frame,list_name_frame
    def gestionchat():
        send_message(client_socket, name,chat_entry.get(),frame)
        chat_entry.delete(0, 'end')
    def gestionchat_(event):
        send_message(client_socket, name,chat_entry.get(),frame)
        chat_entry.delete(0, 'end')
 
    home_fen.destroy()
    chat_fen.deiconify()
    message = StringVar()        
    #test = Canvas(chat_fen, width=1500, height=800, background="white", highlightthickness=0)
    title = Label(chat_fen, text="PyChat",font=("calibre",40,"bold"),fg=color_theme["secondaire"],bg=color_theme["principale"])
    title.place(x=10,y=10)
    #test.place(x=0, y=0)
    Label(chat_fen,text="Connecter en tant que : " + name,fg=color_theme["font"],bg=color_theme["principale"]).place(x=310,y=90)
    is_running = True   
    def update_scrollregion(event):
        chat_box.config(scrollregion=chat_box.bbox("all"))
    def update_scrollregion_(event):
            list_name.config(scrollregion=chat_box.bbox("all"))

    frame.bind("<Configure>", update_scrollregion)
    frame2.bind("<Configure>", update_scrollregion_)
    chat_entry = Entry(chat_fen,textvariable=message,font=("calibre",10),bg=color_theme["secondaire"])
    chat_entry.place(x=310,y=610,width=800,height=50)
    Button(chat_fen,text="Reglage couleur chat",fg=color_theme["font"],bg=color_theme["troisieme"],command=create_popup_reglagecolorchat ).place(x=200,y=10,width=200,height=75)
    btn_send = Button(chat_fen,text="Envoyer !", command=  gestionchat,bg=color_theme["troisieme"])
    

    chat_entry.bind('<Return>',gestionchat_)   
    btn_send.place(x=1110,y=610,width=170,height=50)

    #o = outilcanvas(chat_fen,test)
    chat_fen.protocol("WM_DELETE_WINDOW", on_closing)
    chat_fen.mainloop()
    
    

def send_message(client_socket, name,message,frame):
    global nb_message
    heure_actuelle = datetime.datetime.now()
    heure_formatee = heure_actuelle.strftime("%H : %M : %S")
    data = {"user":name,"message":message,"color":color_traduction[color_user],"time":heure_formatee,"type":"message"}
    if data["message"]=="":
        popup_erreur("Ne pas envoyer de message vide !!")
    else:
        d = pickle.dumps(data)
        client_socket.send(d)
        print("y",nb_message)
        nb_message = nb_message + 1 
        chat_message(data,nb_message,frame)
    

    

home_fen1()