import ttkbootstrap as ttk
import tkinter.messagebox
import sqlite3
#__ _____________________________________________________________________________________________________________________________



class Pagina_menu:
#__Definições principais da janela_______________________________________________________________________________________________________________
    def __init__(self):
        self.pagina = ttk.Window(title = "Oráculo de Morgana - MENU", themename="vapor")
        self.pagina.geometry("1280x960")
        self.pagina.resizable(0,0)

#__Criando os frames de label e entry___________________________________________________________________________________________________________________________
        titulo_I = ttk.Label(text = """Seja muito bem-vindo ao Oráculo de Morgana! 
Preparado para construir nosso menu?""",
                  font=("Times New Roman",30),
                  foreground="#8400ff",
                  justify="center")
        titulo_I.pack(pady=(20, 0))

        titulo_II = ttk.Label(text="""O restaurante nasceu de um grimório esquecido, que detalhava as receitas e elixires da poderosa feiticeira Morgana Le Fay. 
Diz-se que o local foi erguido sobre suas cinzas, um portal para o conhecimento arcano e banquetes proibidos. 
Cada prato é uma oferenda inspirada na dualidade da bruxa Morgana: cura e maldição, luz e sombra.""",
                               font=("Times New Roman", 15),
                               foreground="#8400ff",
                               justify="center")
        titulo_II.pack(pady=(20,0))

        frame_nome = ttk.Frame(style="Vapor")
        frame_nome.pack()


#__Mantendo a janela aberta_______________________________________________________________________________________________________________
    def run(self):
        self.pagina.mainloop()

if __name__ == "__main__":
    pagina_m = Pagina_menu()
    pagina_m.run()