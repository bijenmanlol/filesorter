# File sorter/Bestanden Sorteerder V1.3.3 - https://github.com/bijenmanlol/filesorter

import os
import shutil
import webbrowser
import urllib.request
import json
import tkinter as tk
from tkinter import filedialog, messagebox

window = tk.Tk()
window.title("Bestanden sorteerder")
window.geometry("800x470")
window.resizable(False, False)
currentversion = "File sorter V1.3.3"

def srcCode():
    webbrowser.open("https://github.com/bijenmanlol/filesorter")

def issues():
    webbrowser.open("https://github.com/bijenmanlol/filesorter/issues")

navBar = tk.Frame(width = 800, height= 20)
navBar.pack(anchor = "w")

tk.Label(navBar, bg = "#dedede", text = f"Bestanden sorteerder - Versie 1.3.3{' ' * 110}").grid(row = 0)
tk.Button(navBar, bg = "#dedede", text = "Broncode bekijken", command = srcCode).grid(row = 0, column = 1)
tk.Button(navBar, bg = "#dedede", text = "Probleem rapporteren", command = issues).grid(row = 0, column = 2)
tk.Button(navBar, bg = "#dedede", text = "Sluiten", command = window.destroy).grid(row = 0, column = 3)

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

        self.fl = ["f2"]
        self.posfts = ["Selecteer folder om te sorteren voor bestandstypes te laden"]

        self.famount = 0
        self.ramount = 2
        
        self.f1 = tk.Frame(appFrame, bg = "#dedede")
        self.f1.pack(pady = (20, 0), padx = 100)
        self.f2 = tk.Frame(appFrame, bg = "#dedede")
        self.f2.pack(pady = (20, 0), padx = 20)

        self.dr1 = tk.StringVar() 
        self.dr1.trace_add("write", self.updaterposfts) 

        tk.Label(self.f1, bg = "#dedede", text = "Selecteer de folder die je wilt sorteren").pack(pady = 5)
        self.d1 = tk.Entry(self.f1, textvariable = self.dr1, width = 50)
        self.d1.pack(padx = 35, pady = 5)
        tk.Button(self.f1, text = "Open folder", command = lambda: self.getDir("1")).pack(pady = 5)
        
        tk.Label(self.f2,  bg = "#dedede", text = "Selecteer de folder naar waar je een bepaald bestandstype wil sorteren").pack(pady = 5)
        self.d2 = tk.Entry(self.f2, width = 50)
        self.d2.pack(padx = 20, pady = 5)
        tk.Button(self.f2, text = "Open folder", command = lambda: self.getDir("2")).pack(pady = 5)
        tk.Label(self.f2,  bg = "#dedede", text = "Welke bestandstype wil je sorteren").pack( pady = 5)

        self.t2 = tk.StringVar()
        self.t2.set("Bestandstype")
        self.dr2 = tk.OptionMenu(self.f2, self.t2, *self.posfts)
        self.dr2.pack(padx = 10, pady = 5)

        self.delbut = tk.Button(appFrame, text = "Voeg een bestandtype toe om te sorteren", command = self.addF)
        self.delbut.pack(pady = (20, 0))
        
        self.startbut = tk.Button(appFrame, text = "Start het sorteren", command = self.sort)
        self.startbut.pack(pady = 20)

        try:
            with urllib.request.urlopen("https://api.github.com/repos/bijenmanlol/filesorter/releases/latest") as url:
                name = json.load(url)["name"]
                if name != currentversion:
                    messagebox.showinfo("Verouderde versie", "Er is een nieuwe versie van dit programma beschikbaar. U wordt naar de download pagina van de recentste versie doorgestuurd.")
                    webbrowser.open("https://github.com/bijenmanlol/filesorter/releases/latest")
        except:
            pass

    def getDir(self, currentdir):
        
        dir = filedialog.askdirectory().replace('"', '')
        exec(f'self.d{currentdir}.delete(0, "end")')
        exec(f'self.d{currentdir}.insert(0, "{dir}")')

    def updaterposfts(self, *_):
        if self.d1.get().replace('"', '') != "":
            self.posfts.clear()
            for typer in self.fl:
                type = typer.replace("f", "")
                exec(f"menu = self.dr{type}['menu']")
                exec("menu.delete(0, 'end')")
                templist = []
                for file in os.listdir(self.d1.get().replace('"', '')):
                    if os.path.splitext(file)[1] != "" and os.path.splitext(file)[1] not in templist:
                        self.posfts.append(os.path.splitext(file)[1])
                        templist.append(os.path.splitext(file)[1])
                        exec(f"menu.add_command(label=os.path.splitext(file)[1], command=tk._setit(self.t{type}, os.path.splitext(file)[1]))")

    def delF(self, ext):

        exec(f"self.f{ext}.destroy()")
        self.fl.remove(f"f{ext}")
        self.famount -= 1
        mainFrame.configure(scrollregion = (0, 0, 800, 450 + (self.famount * 212)))

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

        self.ramount += 1
        self.famount += 1

        self.fl.append(f"f{self.ramount}")

        self.delbut.destroy()
        self.startbut.destroy()

        mainFrame.configure(scrollregion = (0, 0, 800, 450 + ((self.famount) * 212)))

        exec(f'self.f{self.ramount} = tk.Frame(appFrame, bg = "#dedede")')
        exec(f'self.f{self.ramount}.pack(pady = (20, 0), padx = 20)')

        exec(f'tk.Label(self.f{self.ramount},  bg = "#dedede", text = "Selecteer de folder naar waar je een bepaald bestandstype wil sorteren").pack(pady = 5)')
        exec(f'self.d{self.ramount} = tk.Entry(self.f{self.ramount}, width = 50)')
        exec(f'self.d{self.ramount}.pack(padx = 20, pady = 5)')
        exec(f'tk.Button(self.f{self.ramount}, text = "Open folder", command = lambda self = self: self.getDir("{self.ramount}")).pack(pady = 5)')
        exec(f'tk.Label(self.f{self.ramount},  bg = "#dedede", text = "Welke bestandstype wil je sorteren").pack( pady = 5)')
        exec(f"self.t{self.ramount} = tk.StringVar()")
        exec(f"self.t{self.ramount}.set('Bestandstype')")
        exec(f"self.dr{self.ramount} = tk.OptionMenu(self.f{self.ramount}, self.t{self.ramount}, *self.posfts)")
        exec(f"self.dr{self.ramount}.pack(padx = 10, pady = 5)")
        exec(f'tk.Button(self.f{self.ramount}, text = "Verwijder", command = lambda self = self: self.delF({self.ramount})).pack(pady = 5)')

        self.delbut = tk.Button(appFrame, text = "Voeg een bestandtype toe om te sorteren", command = self.addF)
        self.delbut.pack(pady = (20, 0))

        self.startbut = tk.Button(appFrame, text = "Start het sorteren", command = self.sort)
        self.startbut.pack(pady = 20)

        mainFrame.yview_moveto((self.famount) * 212)

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
            cnt = 0
            for file in os.listdir(self.d1.get().replace('"', '')):
                for typer in self.fl:
                    type = int(typer.replace("f", ""))
                    ftype = f".{getattr(self, f't{type}').get().replace('.', '')}"
                    if file.endswith(ftype):
                        shutil.copy(self.d1.get().replace("\"", "") + "/" + file, getattr(self, f"d{type}").get().replace("\"", ""))
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

