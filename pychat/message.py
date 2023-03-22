from tkinter import *



class chat_message:
    def __init__(self,data,nb,frame):
        self.data = data
        self.frame = frame 
        self.user = self.getname()
        self.final_message = self.getmessage()
        self.color = self.getcolor()
        self.time = self.getheure()
        print("nb",nb)
        self.affichermessage(nb)
        
    def getcolor(self):
        return self.data["color"]
            
    def getname(self):
        return self.data["user"]
    
    def getmessage(self):
        return self.data["message"]
    
    def getheure(self):
        return self.data["time"]
    
    def sendmessage(self):
        pass
    def affichermessage(self,nb):
        message_box = Frame(self.frame,width=950,height=50)
        #message_box.place(x=0,y=0+(50*nb),width=950,height=50)
        message_box.pack()
        label_name = Label(message_box,text=self.user,font=("calibre",10,"bold"),fg=self.color)
        label_name.place(x=10,y=5)
        label_heure = Label(message_box,text=self.time,fg=self.color)
        label_heure.place(x=7,y=25)
        canvas_barre = Canvas(message_box,width=2,height=40,bg="black")
        canvas_barre.place(x=100, y=5)
        label_message = Label(message_box,text=self.final_message,font=("calibre",10),anchor="w",fg=self.color)
        label_message.place(x=150,y=3,width=800,height=50)


class join_message:
    def __init__(self,data,nb,frame):
        self.data = data
        self.frame = frame 
        self.user = self.getname()
        print("nb",nb)
        self.color = self.getcolor()
        self.time = self.getheure()
        self.affichermessage(nb)

            
    def getname(self):
        return self.data["user"]
    
    def getcolor(self):
        return self.data["color"]
    def getheure(self):
        return self.data["time"]

    def affichermessage(self,nb):
        message_box = Frame(self.frame,width=950,height=50)
        #message_box.place(x=0,y=0+(50*nb),width=950,height=50)
        message_box.pack()
        label_name = Label(message_box,text="SERVEUR",font=("calibre",10,"bold"),fg=self.color)
        label_name.place(x=10,y=5)
        label_heure = Label(message_box,text=self.time,fg=self.color)
        label_heure.place(x=7,y=25)
        canvas_barre = Canvas(message_box,width=2,height=40,bg="black")
        canvas_barre.place(x=100, y=5)
        label_message = Label(message_box,text="UN NOUVEAU MEMBRE VIENT DE SE CONNECTER : " + self.user,font=("calibre",10),anchor="w",fg=self.color)
        label_message.place(x=150,y=3,width=800,height=50)

       
        