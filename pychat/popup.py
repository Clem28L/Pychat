from tkinter import *
from tkinter import ttk

class popup_erreur:
    def __init__(self,erreur):
        self.erreur = erreur
        self.create_popup()
    def create_popup(self):
        erreur_fen = Tk()
        erreur_fen.title("Erreur !")
        erreur_fen.geometry("600x300")
        Label(erreur_fen,text="Erreur: ",fg="red",font=("calibre",20,"bold")).place(x=125,y=50)
        Label(erreur_fen,text=self.erreur,font=("calibre",8,"bold"),fg="red").place(x=10,y=150)
        Button(erreur_fen,text="ok ! ",command=lambda :self.crash(erreur_fen)).place(x=550,y=250)
        erreur_fen.mainloop()
        
    def crash(self,frame):
        frame.destroy()
        
class popup_reglage:
    def __init__(self):
        print("qsdfqszd")
        self.color_traduction = {"Noir":"black","Rouge":"red","Bleu":"blue","Violet":"purple","Blanc":"white","Gris":"grey","Vert":"green","Orange":"orange","Marron":"brown","Jaune":"yelow"}
        self.create_popup_reglagecolorchat()
        
    def create_popup_reglagecolorchat(self):
        popup_reglagecolorchat = Tk()
        popup_reglagecolorchat.title("reglage couleur du chat")
        popup_reglagecolorchat.geometry("600x300")
        color_user = ""
        def set_color(event):
            global color_user
            color_user = value_color.get()
            
        
        Label(popup_reglagecolorchat,text="reglage du chat",font=("calibre",20,"bold")).place(x=125,y=50)
        Label(popup_reglagecolorchat,text="Veuillez choisir votre nouvelle couleur : ",font=("calibre",8,"bold")).place(x=10,y=150)
        value_color = ttk.Combobox(popup_reglagecolorchat,values=list(self.color_traduction.keys()))
        value_color.place(x=220,y=200)
        value_color.bind('<<ComboboxSelected>>', set_color)
        Button(popup_reglagecolorchat,text="ok ! ",command= lambda: popup_reglagecolorchat.destroy()).place(x=550,y=250)
        print("dfg",color_user)
        popup_reglagecolorchat.mainloop()
        