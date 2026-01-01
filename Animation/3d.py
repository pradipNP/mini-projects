import tkinter as tk
import random

w = tk.Tk()
w.title("3D Hacker Tunnel")
c = tk.Canvas(w, bg="black", width=600, height=600)
c.pack()

r = 10
def animate():
    global r
    c.delete("all")
    for i in range(25):
        size = r + i * 15
        color = f"#{random.randint(0,0xFFFFFF):06x}"
        c.create_oval(300-size,300-size,300+size,300+size,
                      outline=color, width=2)
    r = (r + 5) % 50
    w.after(60, animate)

animate()
w.mainloop()
