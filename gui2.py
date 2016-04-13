import tkinter as tk

master = tk.Tk()

Audiofiles = ["A.wav", "B.wav", "C.wav", "D.wav", "E.wav", "F.wav", "G.wav"] 
buttonlst = ['A','B','C','D','E','F','G']


class Pianokey(tk.Button):
    def __init__(self, text, *args):
        self.text = text
        tk.Button.__init__(self, master=master, height= 12, width=4, text = self.text, command=self.callback,*args)
        
    def callback(self):
        for n,i in enumerate(buttonlst):
            if i == self.text:
                print(i)
                #play Audiofiles[n] 
                
C = Pianokey(text='C')
C.grid(row=0, column=0)

D = Pianokey(text='D')
D.grid(row=0, column=1)

E = Pianokey(text='E')
E.grid(row=0, column=2)

F = Pianokey(text='F')
F.grid(row=0, column=3)

G = Pianokey(text='G')
G.grid(row=0, column=4)

A = Pianokey(text='A')
A.grid(row=0, column=5)

B = Pianokey(text='B')
B.grid(row=0, column=6)

master.mainloop()
