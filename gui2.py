from tkinter import filedialog
import tkinter as tk
import winsound as sound


master = tk.Tk()

Audiofreq = [261,293,329,349,391,440,493,279,311,369,415,466] #just add the frequencies in the order that you put the names in buttonlst
buttonlst = ['A','B','C','D','E','F','G','Csharp','Dsharp','Fsharp','Gsharp','Asharp']


class Pianokey(tk.Button):
    songlist = []
    def __init__(self, text):
        self.text = text
        tk.Button.__init__(self, master=master, height=36, width=12, text=self.text,\
                           command=self.callback, bg="white")
        
    def callback(self,boo=False): #will need to eventually pass 'event' as an argument
        for n,i in enumerate(buttonlst):
            if i == self.text:
                sound.Beep(Audiofreq[n],1000)                
                if boo:
                    Pianokey.songlist.append(i)
        
def filewriter():
    songlist = Pianokey.songlist
    newfile = filedialog.asksaveasfilename()
    newfile = open(newfile,'w')
    newfile.write(str(songlist))

def filereader():
    songlist = Pianokey.songlist
    filename = filedialog.askopenfilename()
    newfile = open(filename,'r')
    songlist = newfile.read()
    return songlist

def songplayer():
    songlist = filereader()
    for i in songlist:
        n = buttonlst.index(i)
        sound.Beep(Audiofreq[n],1000)

class Blackkey(Pianokey):
    def __init__(self, text):
        self.text = text
        tk.Button.__init__(self, master=master, height=15, width=8, text=self.text,\
                           command=self.callback, bg="black", fg="white")

class otherkeys(tk.Button):
    def __init__(self,text):
        self.text = text
        tk.Button.__init__(self, master=master,text=self.text,width=5,\
        font=("Arial",24,"bold"))

C = Pianokey(text='C')
C.grid(row=1, column=0)
#C.bind('<Button-1>', Pianokey.callback('<Button-1>',C)) #we might need these later

D = Pianokey(text='D')
D.grid(row=1, column=1)
#D.bind('<Button-2>', Pianokey.callback('<Button-2>',D))

E = Pianokey(text='E')
E.grid(row=1, column=2)
#E.bind('<Button-3>', Pianokey.callback('<Button-3>',E))

F = Pianokey(text='F')
F.grid(row=1, column=3)
#F.bind('<Button-4>', Pianokey.callback('<Button-4>',F))

G = Pianokey(text='G')
G.grid(row=1, column=4)
#G.bind('<Button-5>', Pianokey.callback('<Button-5>',G))

A = Pianokey(text='A')
A.grid(row=1, column=5)
#A.bind('<Button-6>', Pianokey.callback('<Button-6>',A))

B = Pianokey(text='B')
B.grid(row=1, column=6)
#B.bind('<Button-7>', Pianokey.callback('<Button-7>',B))

Csharp = Blackkey(text='Csharp')
Csharp.grid(row=1, column=0, columnspan=2, sticky="N")

Dsharp = Blackkey(text='Dsharp')
Dsharp.grid(row=1, column=1, columnspan=2, sticky="N")

Fsharp = Blackkey(text='Fsharp')
Fsharp.grid(row=1, column=3, columnspan=2, sticky="N")

Gsharp = Blackkey(text='Gsharp')
Gsharp.grid(row=1, column=4, columnspan=2, sticky="N")

Asharp = Blackkey(text='Asharp')
Asharp.grid(row=1, column=5, columnspan=2, sticky="N")

record = otherkeys(text='record')
record.command=Pianokey.callback(record,True)
record.grid(row=2,columnspan=2)

play = otherkeys(text='play')
play.command=filereader
play.grid(row=2,column=3,columnspan=2)

stop = otherkeys(text='stop')
stop.command=filewriter
stop.grid(row=2,column=5,columnspan=2)

master.resizable(width=False, height=False)

master.mainloop()