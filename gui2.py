from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import winsound as sound
from csv import reader, writer


master = tk.Tk()
master.title("Virtual Piano")

Audiofreq = [131,   139,    147,    156,    165,    175,    185,    196,    208,    220,    233,    247,
             262,   277,    294,    311,    330,    349,    370,    392,    415,    440,    466,    494,
             523,   554,    587,    622,    659,    698,    740,    784,    831,    880,    932,    988,]
buttonlst = ['C3',  'C#3',  'D3',   'D#3',  'E3',   'F3',   'F#3',  'G3',   'G#3',  'A3',   'A#3',  'B3',          
             'C4',  'C#4',  'D4',   'D#4',  'E4',   'F4',   'F#4',  'G4',   'G#4',  'A4',   'A#4',  'B4',
             'C5',  'C#5',  'D5',   'D#5',  'E5',   'F5',   'F#5',  'G5',   'G#5',  'A5',   'A#5',  'B5', ]

class Pianokey(tk.Button):
    boo = False
    songlist = []
    def __init__(self, text):
        self.text = text
        tk.Button.__init__(self, master=master, height=21, width=7, text=self.text,\
                           command=self.callback, bg="white")
        
    def callback(self): #will need to eventually pass 'event' as an argument
        for n,i in enumerate(buttonlst):
            if i == self.text:
                sound.Beep(Audiofreq[n],1000)                
                if Pianokey.boo:
                    Pianokey.songlist.append(i)
                    
class Blackkey(Pianokey):
    def __init__(self, text):
        self.text = text
        tk.Button.__init__(self, master=master, height=9, width=5, text=self.text,\
                           command=self.callback, bg="black", fg="white")

class otherkeys(tk.Button):
    def __init__(self,text,command):
        self.command = command
        self.text = text
        tk.Button.__init__(self, master=master,text=self.text,width=5,\
        font=("Arial",24,"bold"),command=self.command)

def filewriter():
    Pianokey.boo = False
    songlist = Pianokey.songlist
    print(songlist)
    newfile = filedialog.asksaveasfile(mode='w',filetypes=(('csv file','.csv'),))
    if not newfile:
        return None
    csvwriter= writer(newfile)
    for i in songlist:
        csvwriter.writerow([i])
    Pianokey.songlist = []

def filereader():
    filename = filedialog.askopenfilename()
    newfile = open(filename,'r')
    songlist = reader(newfile) 
    print("from reader",songlist)
    for i in songlist:
        if ''.join(i) != '':
            n = buttonlst.index(''.join(i))
            sound.Beep(Audiofreq[n],1000)
    newfile.close()

def songrecorder():
    Pianokey.boo = True

def on_closing():
    if Pianokey.boo == True:
        answer = messagebox.askyesnocancel("Quit", "You're still recording! Do you want to save?")
        if answer == None:
            return None
        if answer == True:
            filewriter()
        master.destroy()
    elif Pianokey.boo == False:
        master.destroy()

#might want to do: change the color of a key when that key is played from the recorded files

#####Start of keys#####

### Octave 3 ###
        
C3 = Pianokey(text='C3')
C3.grid(row=1, column=0)
#C3.bind('<Button-1>', Pianokey.callback('<Button-1>',C3)) #we might need these later

D3 = Pianokey(text='D3')
D3.grid(row=1, column=1)
#D3.bind('<Button-2>', Pianokey.callback('<Button-2>',D3))

E3 = Pianokey(text='E3')
E3.grid(row=1, column=2)
#E3.bind('<Button-3>', Pianokey.callback('<Button-3>',E3))

F3 = Pianokey(text='F3')
F3.grid(row=1, column=3)
#F3.bind('<Button-4>', Pianokey.callback('<Button-4>',F3))

G3 = Pianokey(text='G3')
G3.grid(row=1, column=4)
#G3.bind('<Button-5>', Pianokey.callback('<Button-5>',G3))

A3 = Pianokey(text='A3')
A3.grid(row=1, column=5)
#A3.bind('<Button-6>', Pianokey.callback('<Button-6>',A3))

B3 = Pianokey(text='B3')
B3.grid(row=1, column=6)
#B3.bind('<Button-7>', Pianokey.callback('<Button-7>',B3))

Csharp3 = Blackkey(text='C#3')
Csharp3.grid(row=1, column=0, columnspan=2, sticky="N")

Dsharp3 = Blackkey(text='D#3')
Dsharp3.grid(row=1, column=1, columnspan=2, sticky="N")

Fsharp3 = Blackkey(text='F#3')
Fsharp3.grid(row=1, column=3, columnspan=2, sticky="N")

Gsharp3 = Blackkey(text='G#3')
Gsharp3.grid(row=1, column=4, columnspan=2, sticky="N")

Asharp3 = Blackkey(text='A#3')
Asharp3.grid(row=1, column=5, columnspan=2, sticky="N")

#### Octave 4 ####

C4 = Pianokey(text='C4')
C4.grid(row=1, column=7)

D4 = Pianokey(text='D4')
D4.grid(row=1, column=8)

E4 = Pianokey(text='E4')
E4.grid(row=1, column=9)

F4 = Pianokey(text='F4')
F4.grid(row=1, column=10)

G4 = Pianokey(text='G4')
G4.grid(row=1, column=11)

A4 = Pianokey(text='A4')
A4.grid(row=1, column=12)

B4 = Pianokey(text='B4')
B4.grid(row=1, column=13)

Csharp4 = Blackkey(text='C#4')
Csharp4.grid(row=1, column=7, columnspan=2, sticky="N")

Dsharp4 = Blackkey(text='D#4')
Dsharp4.grid(row=1, column=8, columnspan=2, sticky="N")

Fsharp4 = Blackkey(text='F#4')
Fsharp4.grid(row=1, column=10, columnspan=2, sticky="N")

Gsharp4 = Blackkey(text='G#4')
Gsharp4.grid(row=1, column=11, columnspan=2, sticky="N")

Asharp4 = Blackkey(text='A#4')
Asharp4.grid(row=1, column=12, columnspan=2, sticky="N")

##### Octave 5 #####

C5 = Pianokey(text='C5')
C5.grid(row=1, column=14)

D5 = Pianokey(text='D5')
D5.grid(row=1, column=15)

E5 = Pianokey(text='E5')
E5.grid(row=1, column=16)

F5 = Pianokey(text='F5')
F5.grid(row=1, column=17)

G5 = Pianokey(text='G5')
G5.grid(row=1, column=18)

A5 = Pianokey(text='A5')
A5.grid(row=1, column=19)

B5 = Pianokey(text='B5')
B5.grid(row=1, column=20)

Csharp5 = Blackkey(text='C#5')
Csharp5.grid(row=1, column=14, columnspan=2, sticky="N")

Dsharp5 = Blackkey(text='D#5')
Dsharp5.grid(row=1, column=15, columnspan=2, sticky="N")

Fsharp5 = Blackkey(text='F#5')
Fsharp5.grid(row=1, column=17, columnspan=2, sticky="N")

Gsharp5 = Blackkey(text='G#5')
Gsharp5.grid(row=1, column=18, columnspan=2, sticky="N")

Asharp5 = Blackkey(text='A#5')
Asharp5.grid(row=1, column=19, columnspan=2, sticky="N")

######End of keys######

record = otherkeys(text='record', command=songrecorder)
record.grid(row=2, column=6, columnspan=2)

play = otherkeys(text='play', command=filereader)
play.grid(row=2, column=9, columnspan=2)

stop = otherkeys(text='stop', command=filewriter)
stop.grid(row=2, column=12, columnspan=2)

master.resizable(width=False, height=False)

master.protocol("WM_DELETE_WINDOW", on_closing)

master.mainloop()

