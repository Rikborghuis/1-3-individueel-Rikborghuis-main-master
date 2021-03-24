#tkinter benodigt heden
import datetime
import tkinter as tk
window = tk.Tk()
window.title("berken je leeftijd")

#frames
frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()

#functies
def handle_submit(event):
    try:
        leeftijd = 2021 - int(geboorte.get())
        print(leeftijd)
        resultaat["text"] = "Je word dit jaar " + str(leeftijd) + "."
    except:
        resultaat["text"] = "vul een jaartal in AUB"

def handle_clear(event):
    print("verwijer input")
    geboorte.delete(0, "end")








#content
#tekst
greet = tk.Label(master=frame_a,
    text="Welkom in de rik borghuis GUI experience, Wat is je geboorte datum?",
    background="green",
    padx="100",
    pady="75",
)

resultaat = tk.Label(master=frame_b,
    text="Uw resultaat komt als u Uw geboorte datum hier onder invult en op de gele knop drukt",
    background="yellow",
    pady="50",
    padx="50",

)

#leeftijd
geboorte = tk.Entry(master=frame_c,
    background="green",
    foreground="black",
)
#buttons
submit= tk.Button(master=window,
    text="click hier",
    padx="35",
    background="yellow",
)
clear= tk.Button(master=window,
    text="wis",           
    padx="50",
    background="green",
    )



#button connectie
submit.bind("<Button-1>", handle_submit)
clear.bind("<Button-1>", handle_clear)
#packs
frame_a.pack()
frame_b.pack()
frame_c.pack()
greet.pack()
resultaat.pack()
geboorte.pack()
submit.pack()
clear.pack()
