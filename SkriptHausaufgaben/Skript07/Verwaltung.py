from tkinter import *
from time import *
import tkinter
import tkinter.scrolledtext
def des():
    main.destroy()

def ende():
    buecher=open("Buch.txt","w")
    for i in range(len(buch)):
        buecher.write(buch[i][0]+";"+buch[i][1]+"\n")

    benutz=open("Benutzer.txt","w")
    for i in range(len(benutzer)):
        benutz.write(benutzer[i][0]+";"+benutzer[i][1]+";"+benutzer[i][2]+"\n")

    ausleih=open("Ausgeliehen.txt","w")
    for i in range(len(ausgeliehen)):
        ausleih.write(ausgeliehen[i][0]+";"+ausgeliehen[i][1]+";"+ausgeliehen[i][2]+";"+ausgeliehen[i][3]+";"+ausgeliehen[i][4]+"\n")
    
def load():
    fehler=0
    p=""
    try:
        buecher=open("Buch.txt","r")
        for lesen in buecher.readlines():
            split = lesen.rstrip().split(";")
            buch.append((split[0],split[1]))
        buecher.close()
    except:
        fehler=1
    try:
        benutz=open("Benutzer.txt","r")
        for lesen in benutz.readlines():
            split = lesen.rstrip().split(";")
            benutzer.append((split[0],split[1],split[2]))
        benutz.close()
    except:
        fehler=1    
    try:
        ausleih=open("Ausgeliehen.txt","r")
        for lesen in ausleih.readlines():
            split = lesen.rstrip().split(";")
            ausgeliehen.append((split[0],split[1],split[2],split[3],split[4]))
        ausleih.close()
    except:
        fehler=1

def auswahlbu():
    ausgabe1["text"]="Auswahl: "+buchlist.get("active")

def buchloeschen():
    z=ausgabe1["text"]
    pos=0
    try:
        for i in range(len(buch)):
            idx=int(i)-pos
            if z == "Auswahl: "+buch[i][0]+", "+buch[i][1]:
                buch.remove(buch[i])
                buchlist.delete(idx,idx)
                pos+=1
                ausgabe1["text"]=""
                ende()
    except:
        fehler=1

def newbuch():
    try:
        z=text1.get()
        split=z.split(",")
        buch.append((split[0],split[1]))
        buchlist.insert("end",split[0]+", "+split[1])
        text1.delete(0,"end")
        ende()
    except:
        fehler=1
        
def auswahlbe():
    ausgabe2["text"]="Auswahl: "+benutzerlist.get("active")

def beloeschen():
    z=ausgabe2["text"]
    pos=0
    for i in range(len(benutzer)):
        idx=int(i)-pos
        if z == "Auswahl: "+benutzer[i][1]+", "+benutzer[i][2]:
            benutzer.remove(benutzer[i])
            benutzerlist.delete(idx,idx)
            pos+=1
            ende()
    
def newbe():
    try:
        z=text2.get()
        split=z.split(",") 
        x=len(benutzer)+1
        x=str(x)
        benutzer.append((x,split[0],split[1]))#HIER FEHLT NOCH WAS!!!!! KANN NICHT BENUTZT WERDEN
        benutzerlist.insert("end",split[0]+", "+split[1])
        text2.delete(0,"end")
        ende()
    except:
        fehler=1
        
def auswahlaus():
    ausgabe3["text"]="Auswahl: "+ausleihlist.get("active")

def ausleihe():
    try:    
        lt=localtime()
        jahr,monat,tag=lt[0:3]
        tag=str(tag)
        monat=str(monat)
        jahr=str(jahr)
           
        
        x=ausgabe1["text"]
        z=ausgabe2["text"]
        for i in range(len(buch)):
            if x == "Auswahl: "+buch[i][0]+", "+buch[i][1]:
                x=buch[i][0]+", "+buch[i][1]  
                
        for i in range(len(benutzer)):
            if z == "Auswahl: "+benutzer[i][1]+", "+benutzer[i][2]: 
                z=benutzer[i][0]    
                z=x+", "+z+", "+tag+"."+monat+"."+jahr+", "+"noch ausgeliehen"
        split=z.split(", ")
        ausleihlist.insert("end",z)
        ausgeliehen.append((split[0],split[1],split[2],split[3],split[4]))
        ausgabe2["text"]=""
        buchloeschen()
    except:
        fehler=1
        
def ruek():
    pos=0
    for i in range(len(ausgeliehen)):
        z=ausgabe3["text"]
        idx=int(i)-pos
        if z=="Auswahl: "+ausgeliehen[i][0]+", "+ausgeliehen[i][1]+", "+ausgeliehen[i][2]+", "+ausgeliehen[i][3]+", "+ausgeliehen[i][4]:
            x=ausgeliehen[i][0]+", "+ausgeliehen[i][1]
            y=ausgeliehen[i][0],ausgeliehen[i][1]
            print(x)
            ausleihlist.delete(idx,idx)
            ausgeliehen.remove(ausgeliehen[i])
            buchlist.insert("end",x)
            buch.append(y)
            pos+=1
    ende()
            
#Programmstart

buch=[]
benutzer=[]
ausgeliehen=[]

load()
main = tkinter.Tk()
main.title("Verwaltung")

scrollbar = Scrollbar(main, orient=VERTICAL)


buchlist=Listbox(main,width=60,height=5,xscrollcommand=scrollbar.set)

for i in range(len(buch)):
    buchlist.insert("end",buch[i][0]+", "+buch[i][1])
buchlist.grid(row=0, column=1,columnspan=5,sticky=W+E+N+S)

neubu=tkinter.Button(main,text="Neues Buch",command=newbuch)
neubu.grid(row=3,column=2,sticky=W+E+N+S)

loeschbu=tkinter.Button(main, text="Buch Löschen",command=buchloeschen)
loeschbu.grid(row=3,column=3,sticky=W+E+N+S)

auswahlbu=tkinter.Button(main,text="Auswählen", command=auswahlbu)
auswahlbu.grid(row=2,column=2,columnspan=2,sticky=W+E+N+S)

ausgabe1=Label(main)
ausgabe1.grid(row=1,column=1,columnspan=3,sticky=W+E+N+S)

text1=Entry(main)
text1.grid(row=4,column=2,columnspan=2,sticky=W+E+N+S)


benutzerlist=Listbox(main,width=60,height=5,xscrollcommand=scrollbar.set)
for i in range(len(benutzer)):
    benutzerlist.insert("end",benutzer[i][1]+", "+benutzer[i][2])
benutzerlist.grid(row=0,column=6,columnspan=5,sticky=W+E+N+S)

neube=tkinter.Button(main,text="Neuer Benutzer",command=newbe)
neube.grid(row=3,column=7,sticky=W+E+N+S)

loeschbe=tkinter.Button(main, text="Benutzer Löschen",command=beloeschen)
loeschbe.grid(row=3,column=8,sticky=W+E+N+S)

auswahlbe=tkinter.Button(main,text="Auswählen", command=auswahlbe)
auswahlbe.grid(row=2,column=7,columnspan=2,sticky=W+E+N+S)

ausgabe2=Label(main)
ausgabe2.grid(row=1,column=7,columnspan=2,sticky=W+E+N+S)

text2=Entry(main)
text2.grid(row=4,column=7,columnspan=2,sticky=W+E+N+S)

ausleihlist=Listbox(main,width=60,height=5,xscrollcommand=scrollbar.set)
for i in range(len(ausgeliehen)):
    ausleihlist.insert("end",ausgeliehen[i][0]+", "+ausgeliehen[i][1]+", "+ausgeliehen[i][2]+", "+ausgeliehen[i][3]+", "+ausgeliehen[i][4])
ausleihlist.grid(row=0,column=11,columnspan=5,sticky=W+E+N+S)

auslen=tkinter.Button(main,text="Ausleihen",command=ausleihe)
auslen.grid(row=3,column=12,sticky=W+E+N+S)

ruekgabe=tkinter.Button(main,text="Rueckgabe",command=ruek)
ruekgabe.grid(row=3,column=13,sticky=W+E+N+S)

knopf=tkinter.Button(main, text="Ende",command=des)
knopf.grid(row=8,column=1,columnspan=16,sticky=W+E+N+S)

auswahlau=tkinter.Button(main,text="Auswählen", command=auswahlaus)
auswahlau.grid(row=2,column=12,columnspan=2,sticky=W+E+N+S)

ausgabe3=Label(main)
ausgabe3.grid(row=1,column=12,columnspan=2,sticky=W+E+N+S)



main.mainloop()
