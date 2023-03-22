from tkinter import *



class outilcanvas:
    def __init__(self,window ,canvas):
        self.canvas = canvas
        self.ancien = self.canvas.create_text(0, 0)
        self.actif = False
        self.markerList = []
        self.coo_marker = []
        self.couleur_marker = ["red","blue","green","ivory","pink","purple","grey","white","black"]
        self.position_couleur = 0
        self.fen = window
        self.fen.bind("<Return>",self.switch)




    def coo_souris(self, event):
        self.canvas.delete(self.ancien)
        x, y = event.x, event.y
        txt = "X : " + str(x) + " Y :" + str(y)
        self.ancien = self.canvas.create_text(x+50, y, text=txt)
        #print("Position de la souris dans le canvas : x = {}, y = {}".format(x, y))

    def switch(self,event):
        print("ok")
        if self.actif != True:
            self.canvas.bind("<Motion>", self.coo_souris)
            self.canvas.bind("<Button-1>", self.place_marker)
            self.canvas.bind("<Button-2>", self.delete_marker)
            self.actif = True
        elif self.actif == True:
            self.canvas.unbind("<Motion>")
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<Button-2>")
            self.canvas.itemconfig(self.ancien,text="")
            self.actif = False
    def place_marker(self,event):
        x,y = event.x,event.y
        self.markerList.append(((self.canvas.create_oval(x-2,y-2,x+2,y+2,fill=self.couleur_marker[self.position_couleur])),(self.canvas.create_text(x+20,y-20,text=(str(len(self.markerList)+1)+"(" +str(x)+","+str(y)+")")))))
        self.coo_marker.append((x,y))
        print(str(len(self.markerList))+ " : "+ str(x)+","+str(y))
        self.position_couleur += 1
        if self.position_couleur == 8:
            self.position_couleur = 0

    def delete_marker(self,event):
        print("ok")
        """x_clique,y_clique = event.x,event.y
        for i in range(len(self.markerList)):
            norme = sqrt((x_clique-self.coo_marker[i][0])**2 + (y_clique-self.coo_marker[i][1])**2)
            if norme < 10:
                self.canvas.delete(markerList[i][0])
                self.canvas.delete(markerList[i][1])
                markerList.pop(i)


        print(norme)"""
