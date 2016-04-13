import tkinter as tk

master = tk.Tk()

Audiofiles = ["A.wav", "B.wav", "C.wav", "D.wav", "E.wav", "F.wav", "G.wav"] 
buttonlst = ['A','B','C','D','E','F','G']


class Pianokey(tk.Button):
    def __init__(self, text, *args):
        self.text = text
        tk.Button.__init__(self, master=master, height=36, width=12, text=self.text,\
                           command=self.callback, bg="white", *args)
        
    def callback(self):
        for n,i in enumerate(buttonlst):
            if i == self.text:
                print(i)
                #play Audiofiles[n] 

class Blackkey(Pianokey):
    def __init__(self, text, *args):
        self.text = text
        tk.Button.__init__(self, master=master, height=15, width=8, text=self.text,\
                           command=self.callback, bg="black", *args)
    

C = Pianokey(text='C')
C.grid(row=1, column=0)

D = Pianokey(text='D')
D.grid(row=1, column=1)

E = Pianokey(text='E')
E.grid(row=1, column=2)

F = Pianokey(text='F')
F.grid(row=1, column=3)

G = Pianokey(text='G')
G.grid(row=1, column=4)

A = Pianokey(text='A')
A.grid(row=1, column=5)

B = Pianokey(text='B')
B.grid(row=1, column=6)

Csharp = Blackkey(text='C#')
Csharp.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="N")

Dsharp = Blackkey(text='D#')
Dsharp.grid(row=0, column=1, rowspan=2, columnspan=2, sticky="N")

Fsharp = Blackkey(text='F#')
Fsharp.grid(row=0, column=3, rowspan=2, columnspan=2, sticky="N")

Gsharp = Blackkey(text='G#')
Gsharp.grid(row=0, column=4, rowspan=2, columnspan=2, sticky="N")

Asharp = Blackkey(text='A#')
Asharp.grid(row=0, column=5, rowspan=2, columnspan=2, sticky="N")

master.mainloop()
