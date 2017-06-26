"""
    Alunos:
        nome: Danilo de Moraes Costa ()
        nome: Lucas de Almeida Carotta ()
        nome: Isadora ()

    Trabalho:
        Implementação do trabalho de Base de Dados: Tóquio Olimpíadas 2020
"""

from fpdf import FPDF
import tkinter as tk
from tkinter import font as tkfont
from BD.SGBD import Database

# ------------------------------------ SGBD ---------------------------------- #

class baseDeDados:
    def __init__(self, *args, **kwargs):
        self.DB = Database('./BD/olimpiadas.db')

    def gerar_relatorio(self, tipo):
        if('altetlas' == tipo):
            print("Nothing")

    def fechar_conexao(self):
        self.DB.close()

# --------------------------------- INTERFACE -------------------------------- #

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Selecione a opção desejada", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Gerar relatório", command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Rodar scripts", command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Fechar", command=lambda: controller.encerrar())
        button1.pack()
        button2.pack()
        button3.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Gerar relatório", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        text_intro = tk.Label(self, text="Selecione o tipo de relatório que deseja.")
        text_description = tk.Label(self, text="Os relatórios gerados serão salvos em pdf no diretório atual.")
        text_intro.pack(side="top", fill="x")
        text_description.pack(side="top", fill="x")
        atletas = tk.Button(self, text="Listagem por atletas", command=controller.base.gerar_relatorio('atletas'))
        medico = tk.Button(self, text="Listagem por médicos", command=controller.base.gerar_relatorio('médicos'))
        treinos = tk.Button(self, text="Listagem por treinos", command=controller.base.gerar_relatorio('treinos'))
        treinador = tk.Button(self, text="Listagem por treinador", command=controller.base.gerar_relatorio('treinador'))
        menu = tk.Button(self, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        atletas.pack()
        medico.pack()
        treinos.pack()
        treinador.pack()
        menu.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Rodar scripts", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        text = tk.Label(self, text="Selecione o tipo de scprit que deseja rodar.")
        text.pack(side="top", fill="x")
        menu = tk.Button(self, text="Voltar", command=lambda: controller.show_frame("StartPage"))
        menu.pack()

# --------------------------------- SISTEMA ---------------------------------- #

class olimpiadas(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="Opções", size=18, weight="bold", slant="italic")

        self.base = baseDeDados()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Motre a tela na janela da interface selcionada'''
        frame = self.frames[page_name]
        frame.tkraise()

    def encerrar(self):
        self.destroy()
        self.base.fechar_conexao()

# ---------------------------------- MAIN ------------------------------------ #

app = olimpiadas()
app.mainloop()

# ----------------------------------- EOF ------------------------------------ #
