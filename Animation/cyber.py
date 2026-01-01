import tkinter as tk, random

w = tk.Tk()
c = tk.Canvas(w, bg="black", width=500, height=300)
c.pack()

def hud():
    c.delete("all")
    c.create_text(250,30,text="CYBER HUD",fill="cyan",font=("Arial",18,"bold"))
    stats = ["CPU","RAM","NET","GPU"]
    for i,s in enumerate(stats):
        val = random.randint(10,99)
        c.create_text(80,80+i*40,text=s,fill="lime")
        c.create_rectangle(120,70+i*40,120+val*3,90+i*40,fill="lime")
    w.after(800, hud)

hud()
w.mainloop()
