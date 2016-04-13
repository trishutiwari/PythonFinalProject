import tkinter as tk

master = tk.Tk()

Audiofiles = ["A.wav"] #I'll add more sounds to this. 
buttonlst = ['A','B','C','D','E','F','G']

def callback(button):
    for n,i in enumerate(buttonlst):
        if i == button:
            print(i)
           #play Audiofiles[n] 
        
C = tk.Button(master, text='C')
C.grid(row=0,column=0)
C.bind("<Button-1>", callback('C')) 

D = tk.Button(master, text='D')
D.grid(row=0,column=1) 
C.bind("<Button-2>", callback('D')) 

E = tk.Button(master, text='E')
E.grid(row=0,column=2) 
C.bind("<Button-3>", callback('E')) 

F = tk.Button(master, text='F')
F.grid(row=0,column=3) 
C.bind("<Button-4>", callback('F')) 

G = tk.Button(master, text='G')
G.grid(row=0,column=4) 
C.bind("<Button-5>", callback('G')) 

A = tk.Button(master, text='A')
A.grid(row=0,column=5) 
C.bind("<Button-6>", callback('A')) 

B = tk.Button(master, text='B')
B.grid(row=0,column=6) 
C.bind("<Button-7>", callback('B')) 


tk.mainloop()