import tkinter as tk, random

w = tk.Tk()
c = tk.Canvas(w, bg="black", width=600, height=400)
c.pack()

drops = [random.randint(0, 400) for _ in range(80)]

def rain():
    c.delete("all")
    for i, y in enumerate(drops):
        c.create_text(i*8, y, text=random.choice("01"),
                      fill="#00ff00", font=("Consolas", 14))
        drops[i] = y + 10 if y < 400 else 0
    w.after(50, rain)

rain()
w.mainloop()
