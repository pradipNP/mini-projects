import tkinter as tk, math

w = tk.Tk()
c = tk.Canvas(w, bg="black", width=600, height=600)
c.pack()

def move(e):
    c.delete("all")
    for i in range(40):
        r = i*8
        x = 300 + r*math.cos(e.x/50)
        y = 300 + r*math.sin(e.y/50)
        c.create_oval(x-r,y-r,x+r,y+r,outline="cyan")

c.bind("<Motion>", move)
w.mainloop()
