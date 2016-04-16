from tkinter import filedialog
import tkinter as tk
import winsound as sound
from csv import reader


master = tk.Tk()

Audiofreq = [261,293,329,349,391,440,493,279,311,369,415,466] #just add the frequencies in the order that you put the names in buttonlst
buttonlst = ['A','B','C','D','E','F','G','Csharp','Dsharp','Fsharp','Gsharp','Asharp']


# Each row represents 1 octave - rounded each freq to the nearest whole number; source: http://www.seventhstring.com/resources/notefrequencies.html
# 9 octaves total; pianos typically go from freq ~28 to 4186

#            C       C#      D       D#      E       F       F#      G       G#      A       A#      B 
#Audiofreq= [16,     17,     18,     19,     21,     22,     23,     24,     26,     28,     29,     31,\
#            33,     35,     37,     39,     41,     44,     46,     49,     52,     55,     58,     62,\
#            65,     69,     73,     78,     82,     87,     92,     98,     104,    110,    116,    124,\
#            131,    139,    147,    156,    165,    175,    185,    196,    208,    220,    233,    247,\
#            262,    277,    294,    311,    330,    349,    370,    392,    415,    440,    466,    494,\
#            523,    554,    587,    622,    659,    698,    740,    784,    831,    880,    932,    988,\
#            1047,   1109,   1175,   1245,   1319,   1397,   1480,   1568,   1661,   1760,   1865,   1976,\
#            2093,   2217,   2349,   2489,   2637,   2794,   2960,   3136,   3322,   3520,   3729,   3951,\
#            4186,   4435,   4699,   4978,   5274,   5588,   5920,   6272,   6645,   7040,   7459,   7902]

#buttonlst=['C0', 'Csharp0', 'D0', 'Dsharp0', 'E0', 'F0', 'Fsharp0', 'G0', 'Gsharp0', 'A0', 'Asharp0', 'B0',\
#           'C1', 'Csharp1', 'D1', 'Dsharp1', 'E1', 'F1', 'Fsharp1', 'G1', 'Gsharp1', 'A1', 'Asharp1', 'B1',\
#           'C2', 'Csharp2', 'D2', 'Dsharp2', 'E2', 'F2', 'Fsharp2', 'G2', 'Gsharp2', 'A2', 'Asharp2', 'B2',\
#           'C3', 'Csharp3', 'D3', 'Dsharp3', 'E3', 'F3', 'Fsharp3', 'G3', 'Gsharp3', 'A3', 'Asharp3', 'B3',\
#           'C4', 'Csharp4', 'D4', 'Dsharp4', 'E4', 'F4', 'Fsharp4', 'G4', 'Gsharp4', 'A4', 'Asharp4', 'B4',\
#           'C5', 'Csharp5', 'D5', 'Dsharp5', 'E5', 'F5', 'Fsharp5', 'G5', 'Gsharp5', 'A5', 'Asharp5', 'B5',\
#           'C6', 'Csharp6', 'D6', 'Dsharp6', 'E6', 'F6', 'Fsharp6', 'G6', 'Gsharp6', 'A6', 'Asharp6', 'B6',\
#           'C7', 'Csharp7', 'D7', 'Dsharp7', 'E7', 'F7', 'Fsharp7', 'G7', 'Gsharp7', 'A7', 'Asharp7', 'B7',\
#           'C8', 'Csharp8', 'D8', 'Dsharp8', 'E8', 'F8', 'Fsharp8', 'G8', 'Gsharp8', 'A8', 'Asharp8', 'B8']


#for i in range(len(Audiofreq)):
#    globals()[(str(buttonlst[i])+'{}').format(octave) = Pianokey(text=buttonlst[i])

class Pianokey(tk.Button):
    boo = False
    songlist = ""
    def __init__(self, text):
        self.text = text
        tk.Button.__init__(self, master=master, height=36, width=12, text=self.text,\
                           command=self.callback, bg="white")
        
    def callback(self): #will need to eventually pass 'event' as an argument
        for n,i in enumerate(buttonlst):
            if i == self.text:
                sound.Beep(Audiofreq[n],1000)                
                if Pianokey.boo:
                    Pianokey.songlist += i + " "
        
def filewriter():
    Pianokey.boo = False
    songlist = Pianokey.songlist
    newfile = filedialog.asksaveasfile(mode='w',filetypes=(('text files','.txt'),))
    if not newfile:
        return None
    newfile.write(str(songlist[1:-1]))
    Pianokey.songlist = ""

def filereader():
    filename = filedialog.askopenfilename()
    newfile = open(filename,'r')
    songlist = reader(newfile, delimiter=' ') #I don't know the representation of the datatype the reader returns
    print(songlist)
    for i in songlist:
        n = buttonlst.index(i)
        sound.Beep(Audiofreq[n],1000)
    newfile.close()


def songrecorder():
    Pianokey.boo = True

class Blackkey(Pianokey):
    def __init__(self, text):
        self.text = text
        tk.Button.__init__(self, master=master, height=15, width=8, text=self.text,\
                           command=self.callback, bg="black", fg="white")

class otherkeys(tk.Button):
    def __init__(self,text,command):
        self.command = command
        self.text = text
        tk.Button.__init__(self, master=master,text=self.text,width=5,\
        font=("Arial",24,"bold"),command=self.command)

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

record = otherkeys(text='record', command=songrecorder)
record.grid(row=2,columnspan=2)

play = otherkeys(text='play', command=filereader)
play.grid(row=2,column=3,columnspan=2)

stop = otherkeys(text='stop', command=filewriter)
stop.grid(row=2,column=5,columnspan=2)

master.resizable(width=False, height=False)

master.mainloop()

