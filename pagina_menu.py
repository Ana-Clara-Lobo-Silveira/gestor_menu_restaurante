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
Diz-se que o local foi erguido sobre suas cinzas, um portal para o conhecimento arcano e banquetes proibidos. Cada 
prato é uma oferenda inspirada na dualidade da bruxa Morgana: cura e maldição, luz e sombra.""",
                               font=("Times New Roman", 15),
                               foreground="#8400ff",
                               justify="center")
        titulo_II.pack(pady=(20,0))

#______________________________________________________________________________________________________________________________
        frame_nome = ttk.Frame(style="Vapor")
        frame_nome.pack(pady=(25,0))

        ttk.Label(frame_nome, text="Nome do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
        ttk.Entry(frame_nome, width=60,font=("Times New Roman",15)).pack(side = "right")
#------------------------------------------------------------------------------------------------------------------------------
        frame_categoria = ttk.Frame(style="Vapor")
        frame_categoria.pack(pady=(25,0))

        ttk.Label(frame_categoria, text="Descrição do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
        ttk.Entry(frame_categoria, width=60,font=("Times New Roman",15)).pack(side = "right")
#------------------------------------------------------------------------------------------------------------------------------
        frame_preco = ttk.Frame(style="Vapor")
        frame_preco.pack(pady=(25,0))

        ttk.Label(frame_preco, text="Valor do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
        ttk.Entry(frame_preco, width=60,font=("Times New Roman",15)).pack(side = "right")
#------------------------------------------------------------------------------------------------------------------------------
        frame_categoria = ttk.Frame(style="Vapor")
        frame_categoria.pack(pady=(25,0))

        ttk.Label(frame_categoria, text="Categoria do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
        ttk.Entry(frame_categoria, width=60,font=("Times New Roman",15)).pack(side = "right")
#_______________________________________________________________________________________________________________________________
        frame_tv_b = ttk.Frame(style="Vapor")
        frame_tv_b.pack(pady=(0,0))
      
        tv = ttk.Treeview(frame_tv_b)
        tv.pack(pady=(25,0), side="left")

        tv["columns"] = ("nome", "descricao", "valor", "categoria")
        tv ["show"] = "headings"
        tv.heading("nome", text="Nome do prato")
        tv.heading("descricao", text="Descrição")
        tv.heading("valor", text="Valor")
        tv.heading("categoria", text="Categorias")
#_________________________________________________________________________________________________________________________________________

        frame_botoes = ttk.Frame(frame_tv_b, style="Vapor")
        frame_botoes.pack(pady=(0,0), side="right")

        ttk.Button(frame_botoes, text="Adicionar",width=40,padding = 9).pack(pady=(5,0), padx=20)
        ttk.Button(frame_botoes, text="Alterar",width=40,padding = 9).pack(pady=(5,0), padx=20)
        ttk.Button(frame_botoes, text="Excluir",width=40,padding = 9).pack(pady=(5,0), padx=20)
#__Mantendo a janela aberta_______________________________________________________________________________________________________________
    def run(self):
        self.pagina.mainloop()

if __name__ == "__main__":
    pagina_m = Pagina_menu()
    pagina_m.run()