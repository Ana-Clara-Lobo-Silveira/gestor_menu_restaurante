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
                self.e_nome = ttk.Entry(frame_nome, width=60,font=("Times New Roman",15))
                self.e_nome.pack(side = "right")
        #------------------------------------------------------------------------------------------------------------------------------
                frame_descricao = ttk.Frame(style="Vapor")
                frame_descricao.pack(pady=(25,0))

                ttk.Label(frame_descricao, text="Descrição do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
                self.e_descricao = ttk.Entry(frame_descricao, width=60,font=("Times New Roman",15))
                self.e_descricao.pack(side = "right")
        #------------------------------------------------------------------------------------------------------------------------------
                frame_valor = ttk.Frame(style="Vapor")
                frame_valor.pack(pady=(25,0))

                ttk.Label(frame_valor, text="Valor do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
                self.e_valor = ttk.Entry(frame_valor, width=60,font=("Times New Roman",15))
                self.e_valor.pack(side = "right")
        #------------------------------------------------------------------------------------------------------------------------------
                frame_categoria = ttk.Frame(style="Vapor")
                frame_categoria.pack(pady=(25,0))

                ttk.Label(frame_categoria, text="Categoria do prato: ", font=("Times New Roman", 15), foreground="#8400ff").pack(side = "left")
                self.e_categoria = ttk.Entry(frame_categoria, width=60,font=("Times New Roman",15))
                self.e_categoria.pack(side = "right")
        #_______________________________________________________________________________________________________________________________
                frame_tv_b = ttk.Frame(style="Vapor")
                frame_tv_b.pack(pady=(0,0))
        
                self.tv = ttk.Treeview(frame_tv_b)
                self.tv.pack(pady=(25,0), side="left")

                self.tv["columns"] = ("nome", "descricao", "valor", "categoria")
                self.tv ["show"] = "headings"
                self.tv.heading("nome", text="Nome do prato")
                self.tv.heading("descricao", text="Descrição")
                self.tv.heading("valor", text="Valor")
                self.tv.heading("categoria", text="Categorias")
        #------------------------------------------------------------------------------------------------------------------------------
                conexao = sqlite3.connect("./bd_menu_restaurante.sqlite")
                cursor = conexao.cursor()

                sql_para_criar_tabela = """
                                        CREATE TABLE IF NOT EXISTS menu (
                                        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nome VARCHAR (50),
                                        descricao VARCHAR (200),
                                        preco VARCHAR (15),
                                        categoria VARCHAR (15)
                                        );
                                        """
                
                cursor.execute(sql_para_criar_tabela)
                conexao.commit()
                conexao.close()

                self.atualizar_tv()
        #------------------------------------------------------------------------------------------------------------------------------

        
                frame_botoes = ttk.Frame(frame_tv_b, style="Vapor")
                frame_botoes.pack(pady=(0,0), side="right")

                ttk.Button(frame_botoes, text="Adicionar",width=40,padding = 9,command=self.adicionar).pack(pady=(5,0), padx=20)
                ttk.Button(frame_botoes, text="Alterar",width=40,padding = 9).pack(pady=(5,0), padx=20)
                ttk.Button(frame_botoes, text="Excluir",width=40,padding = 9, command=self.excluir).pack(pady=(5,0), padx=20)

        def atualizar_tv(self):

                for teste in self.tv.get_children():
                       self.tv.delete(teste)


                self.conexao_III = sqlite3.connect("bd_menu_restaurante.sqlite")
                self.cursor_III = self.conexao_III.cursor()
                self.sql_atualizar_tv = """
                                                SELECT nome, descricao, preco, categoria from menu;  
                                        """
                self.cursor_III.execute(self.sql_atualizar_tv)

                res = self.cursor_III.fetchall()
                self.conexao_III.close()

                for linha in res:
                        self.tv.insert("","end", values = linha)

        def adicionar(self):
                
                self.n = self.e_nome.get()
                self.d = self.e_descricao.get()
                self.v = self.e_valor.get()
                self.c = self.e_categoria.get()


                conexao_II = sqlite3.connect("bd_menu_restaurante.sqlite")
                cursor_II = conexao_II.cursor()

                sql_para_inserir_itens = """
                                                INSERT INTO menu (nome, descricao, preco, categoria)
                                                VALUES (?,?,?,?);
                                        """

                cursor_II.execute(sql_para_inserir_itens, [self.n,self.d,self.v,self.c])
                conexao_II.commit()
                conexao_II.close()
                self.atualizar_tv()

        def excluir(self):
                s_e = self.tv.selection()
                iid_s  = s_e[0]
                item_valores = self.tv.item(iid_s, 'values')
                codigo_do_registro = item_valores[0]
                self.tv.delete(s_e)

                self.conexao_IV = sqlite3.connect("bd_menu_restaurante.sqlite")
                self.cursor_IV = self.conexao_IV.cursor()

                sql_para_excluir = """
                                        DELETE FROM menu WHERE nome = ?;
                                        """

                self.cursor_IV.execute(sql_para_excluir, [codigo_do_registro])
                self.conexao_IV.commit()
                self.conexao_IV.close()
#-----------------------------------------------------------------------------------------------------------------------------------------

#__Mantendo a janela aberta_______________________________________________________________________________________________________________
        def run(self):
                self.pagina.mainloop()

if __name__ == "__main__":
    pagina_m = Pagina_menu()
    pagina_m.run()