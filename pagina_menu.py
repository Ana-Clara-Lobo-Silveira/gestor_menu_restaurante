import ttkbootstrap as ttk
import tkinter.messagebox
import sqlite3

class Pagina_menu:
    def __init__(self):
        self.pagina = ttk.Window(title = "Página-Menu", themename="simplex")
        self.pagina.geometry("1280x960")
        self.pagina.resizable(0,0)


    def run(self):
        self.pagina.mainloop()

if __name__ == "__main__":
    pagina_m = Pagina_menu()
    pagina_m.run()