import os, shutil, webbrowser
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Bestanden sorteerder - Gemaakt door Noah")
window.geometry("800x470")
window.resizable(False, False)

def srcCode():
    webbrowser.open("https://github.com/bijenmanlol/filesorter")

navBar = tk.Frame(width = 800, height= 20)
navBar.pack(anchor = "w")

tk.Label(navBar, bg = "#dedede", text = f"Bestanden sorteerder - Gemaakt door Noah{' ' * 135}").grid(row = 0)
tk.Button(navBar, bg = "#dedede", text = "Broncode bekijken", command = srcCode).grid(row = 0, column = 1)
tk.Button(navBar, bg = "#dedede", text = "Sluiten", command = window.destroy).grid(row = 0, column = 2)

v = tk.Scrollbar(orient = "vertical")
v.pack(side = "right", fill = "y")

mainFrame = tk.Canvas(yscrollcommand = v.set, width = 800, height = 450, highlightthickness = 0)
mainFrame.pack(padx = 100)
mainFrame.configure(scrollregion = (0, 0, 800, 450))

def on_mousewheel(event):
    mainFrame.yview_scroll(int(-1*(event.delta/120)), "units")

mainFrame.bind_all("<MouseWheel>", on_mousewheel)

v.config(command = mainFrame.yview)

appFrame = tk.Frame(mainFrame)
appFrame.pack()

mainFrame.create_window((300, 0), window = appFrame, anchor = "n")

class App:
    def __init__(self):

        self.famount = 1
        
        f1 = tk.Frame(appFrame, bg = "#dedede")
        f1.pack(pady = (20, 0), padx = 100)
        f2 = tk.Frame(appFrame, bg = "#dedede")
        f2.pack(pady = (20, 0), padx = 20)


        tk.Label(f1, bg = "#dedede", text = "Selecteer de folder die je wilt sorteren").pack(pady = 5)
        self.d1 = tk.Entry(f1, width = 50)
        self.d1.pack(padx = 35, pady = 5)
        tk.Button(f1, text = "Open folder", command = lambda: self.getDir("1")).pack(pady = 5)
        
        tk.Label(f2,  bg = "#dedede", text = "Selecteer de folder naar waar je een bepaald bestandstype wil sorteren").pack(pady = 5)
        self.d2 = tk.Entry(f2, width = 50)
        self.d2.pack(padx = 20, pady = 5)
        tk.Button(f2, text = "Open folder", command = lambda: self.getDir("2")).pack(pady = 5)
        tk.Label(f2,  bg = "#dedede", text = "Welke bestandstype wil je sorteren").pack( pady = 5)
        self.t2 = tk.Entry(f2, width = 50)
        self.t2.pack(padx = 10, pady = 5)

        self.delbut = tk.Button(appFrame, text = "Voeg een bestandtype toe om te sorteren", command = self.addF)
        self.delbut.pack(pady = (20, 0))
        
        self.startbut = tk.Button(appFrame, text = "Start het sorteren", command = self.sort)
        self.startbut.pack(pady = 20)

    def addF(self):

        try:
            self.ft1.destroy()
        except:
            pass
        try:
            self.ft2.destroy()
        except:
            pass
        try:
            self.ft3.destroy()
        except:
            pass

        self.famount += 1
        ramount = self.famount + 1

        self.delbut.destroy()
        self.startbut.destroy()

        mainFrame.configure(scrollregion = (0, 0, 800, 450 + ((self.famount - 1) * 176)))

        exec(f'f{ramount} = tk.Frame(appFrame, bg = "#dedede")')
        exec(f'f{ramount}.pack(pady = (20, 0), padx = 20)')

        exec(f'tk.Label(f{ramount},  bg = "#dedede", text = "Selecteer de folder naar waar je een bepaald bestandstype wil sorteren").pack(pady = 5)')
        exec(f'self.d{ramount} = tk.Entry(f{ramount}, width = 50)')
        exec(f'self.d{ramount}.pack(padx = 20, pady = 5)')
        exec(f'tk.Button(f{ramount}, text = "Open folder", command = lambda self = self: self.getDir("{ramount}")).pack(pady = 5)')
        exec(f'tk.Label(f{ramount},  bg = "#dedede", text = "Welke bestandstype wil je sorteren").pack( pady = 5)')
        exec(f'self.t{ramount} = tk.Entry(f{ramount}, width = 50)')
        exec(f'self.t{ramount}.pack(padx = 10, pady = 5)')

        self.delbut = tk.Button(appFrame, text = "Voeg een bestandtype toe om te sorteren", command = self.addF)
        self.delbut.pack(pady = (20, 0))

        self.startbut = tk.Button(appFrame, text = "Start het sorteren", command = self.sort)
        self.startbut.pack(pady = 20)

        mainFrame.yview_moveto((self.famount - 1) * 176)

    def getDir(self, currentdir):
        
        dir = filedialog.askdirectory().replace('"', '')
        exec(f'self.d{currentdir}.delete(0, "end")')
        exec(f'self.d{currentdir}.insert(0, "{dir}")')
    def sort(self):

        try:
            self.ft1.destroy()
        except:
            pass
        try:
            self.ft2.destroy()
        except:
            pass
        try:
            self.ft3.destroy()
        except:
            pass
        try:
            self.ft4.destroy()
        except:
            pass

        try:
            cnt = 0
            for file in os.listdir(self.d1.get().replace('"', '')):
                for type in range(self.famount):
                    ftype = f".{getattr(self, f't{type + 2}').get().replace('.', '')}"
                    if file.endswith(ftype):
                        shutil.copy(self.d1.get().replace("\"", "") + "/" + file, getattr(self, f"d{type + 2}").get().replace("\"", ""))
                        cnt += 1
            if cnt == 0:
                self.ft1 = tk.Label(appFrame, text = "Geen bestanden gevonden om te sorteren, bekijk of de bestandtypes en folders correct zijn")
                self.ft1.pack(pady = 5)
            else:
                self.ft2 = tk.Label(appFrame, text = "Bestanden succesvol gesorteerd")
                self.ft2.pack(pady = 5)
                    
        except:
            self.ft3 = tk.Label(appFrame, text = "Bestanden sorteren mislukt, bekijk of de ingeven info correct is")
            self.ft3.pack(pady = 5)

App()

window.mainloop()

