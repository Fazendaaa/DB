"""
    Alunos:
        nome: Danilo de Moraes Costa (8921972)
        nome: Lucas de Almeida Carotta (8598732)
        nome: Isadora ()

    Trabalho:
        Implementação do trabalho de Base de Dados: Tóquio Olimpíadas 2020
"""

from fpdf import FPDF
import tkinter as tk
from tkinter import font as tkfont
from BD.SGBD import Database

# ------------------------------------ PDF ----------------------------------- #

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Olimpíadas 2020 - Tóquio', 1, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def relatorio(self):
        self.alias_nb_pages()
        self.add_page()
        self.set_font('Times', '', 12)
        self.cell(0, 10, 'Modalidade: ' + modalidadeStr.get(), 0, 1)
        self.cell(0, 10, 'Médico: ' + medicoStr.get(), 0, 1)
        self.cell(0, 10, 'Treinador: ' + treinadorStr.get(), 0, 1)
        self.output('atleta.pdf', 'F')

# ------------------------------------ SGBD ---------------------------------- #

class baseDeDados(Database):
    def __init__(self):
        Database.__init__(self, './BD/olimpiadas.db')
        self.pdf = PDF()

    def gerar_relatorio_atleta(self):
        self.pdf.relatorio()

    def gerar_relatorio_medico(self):
        self.pdf.relatorio()
    
    def gerar_relatorio_treinador(self):
        self.pdf.relatorio()
    
    def fechar_conexao(self):
        self.close()

# --------------------------------- INTERFACE -------------------------------- #

def get_linha_selecionada(event):
    """Função para retornar a opção selecionada"""
    global tupla_selecionada, listBox
    tupla_selecionada = listBox.get(listBox.curselection()[0])

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Selecione a opção desejada", font=controller.title_font)

        button1 = tk.Button(self, text="Gerenciar relação", command=lambda: controller.show_frame("Relacao"))
        button2 = tk.Button(self, text="Gerar relatório", command=lambda: controller.show_frame("Relatorios"))
        button3 = tk.Button(self, text="Rodar scripts", command=lambda: controller.show_frame("Scripts"))
        button4 = tk.Button(self, text="Fechar", command=lambda: controller.encerrar())
        
        label.pack()
        
        button1.pack(fill="x", padx=5, pady=5)
        button2.pack(fill="x", padx=5, pady=5)
        button3.pack(fill="x", padx=5, pady=5)
        button4.pack(fill="x", padx=5, pady=5)

class Relacao(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global listBox

        label = tk.Label(self, text="Gerenciar relação", font=controller.title_font)
        text_intro = tk.Label(self, text="Selecione os dados seguido da opção que deseja realizar.")

        resultadoLabel = tk.Label(self, text="Resultado:")

        listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(listBox)

        scrollBar.configure(command=listBox.yview)
        listBox.configure(yscrollcommand=scrollBar.set)
        listBox.bind('<<ListboxSelect>>', get_linha_selecionada)

        atletas = tk.Button(self, text="Rodar", command=lambda: controller.show_frame('Menu'))
        menu = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Menu'))
        
        label.pack(padx=5, pady=5)
        text_intro.pack(padx=5, pady=5)
        resultadoLabel.pack(padx=5, pady=5)
        listBox.pack(fill="x", padx=5, pady=5)
        scrollBar.pack(side='right')

        atletas.pack(fill="x", padx=5, pady=5)
        menu.pack(fill="x", padx=5, pady=5)

class Relatorios(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Gerar relatório", font=controller.title_font)
        text_intro = tk.Label(self, text="Selecione o tipo de relatório que deseja.")
        text_description = tk.Label(self, text="Os relatórios gerados serão salvos em pdf no diretório atual.")

        atletas = tk.Button(self, text="Listagem por atletas", command=lambda: controller.show_frame('ListarAtletas'))
        medico = tk.Button(self, text="Listagem por médicos", command=lambda: controller.show_frame('ListarMedicos'))
        treinador = tk.Button(self, text="Listagem por treinador", command=lambda: controller.show_frame('ListarTreinador'))
        menu = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Menu'))

        label.pack(padx=5, pady=5)
        text_intro.pack(padx=5, pady=5)
        text_description.pack(padx=5, pady=5)

        atletas.pack(fill="x", padx=5, pady=5)
        medico.pack(fill="x", padx=5, pady=5)
        treinador.pack(fill="x", padx=5, pady=5)
        menu.pack(fill="x", padx=5, pady=5)

class ListarAtletas(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global listBox

        label = tk.Label(self, text="Listagem por atletas", font=controller.title_font)
        
        modalidadeLabel = tk.Label(self, text="Digite o nome da modalidade:")
        modalidadeEntry = tk.Entry(self, textvariable=modalidadeStr, width=50)
        
        medicoLabel = tk.Label(self, text="Digite o nome do médico:")
        medicoEntry = tk.Entry(self, textvariable=medicoStr, width=50)
        
        treinadorLabel = tk.Label(self, text="Digite o nome do treinador:")
        treinadorEntry = tk.Entry(self, textvariable=treinadorStr, width=50)

        resultadoLabel = tk.Label(self, text="Resultado:")

        listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(listBox)

        scrollBar.configure(command=listBox.yview)
        listBox.configure(yscrollcommand=scrollBar.set)
        listBox.bind('<<ListboxSelect>>', get_linha_selecionada)

        rodar = tk.Button(self, text="Rodar", command=controller.base.gerar_relatorio_atleta)
        voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Relatorios'))
        pdf = tk.Button(self, text="Gerar PDF", command=controller.base.gerar_relatorio_atleta)
        
        label.pack(padx=5, pady=5)
        modalidadeLabel.pack(padx=5, pady=5)
        modalidadeEntry.pack(fill="x", padx=5, pady=5)
        medicoLabel.pack(padx=5, pady=5)
        medicoEntry.pack(fill="x", padx=5, pady=5)
        treinadorLabel.pack(padx=5, pady=5)
        treinadorEntry.pack(fill="x", padx=5, pady=5)
        resultadoLabel.pack(padx=5, pady=5)
        listBox.pack(fill="x", padx=5, pady=5)
        scrollBar.pack(side='right')

        rodar.pack(fill="x", padx=5, pady=5)
        pdf.pack(fill="x", padx=5, pady=5)
        voltar.pack(fill="x", padx=5, pady=5)

class ListarMedicos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global listBox

        label = tk.Label(self, text="Listagem por médicos", font=controller.title_font)
        
        atletaLabel = tk.Label(self, text="Digite o nome do atetla:")
        atletaEntry = tk.Entry(self, textvariable=atetlaStr, width=50)
        
        nacaoLabel = tk.Label(self, text="Digite o nome da nação:")
        nacaoEntry = tk.Entry(self, textvariable=nacaoStr, width=50)
        
        resultadoLabel = tk.Label(self, text="Resultado:")

        listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(listBox)

        scrollBar.configure(command=listBox.yview)
        listBox.configure(yscrollcommand=scrollBar.set)
        listBox.bind('<<ListboxSelect>>', get_linha_selecionada)

        rodar = tk.Button(self, text="Rodar", command=controller.base.gerar_relatorio_medico)
        voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Relatorios'))
        pdf = tk.Button(self, text="Gerar PDF", command=controller.base.gerar_relatorio_medico)
        
        label.pack(padx=5, pady=5)
        atletaLabel.pack(padx=5, pady=5)
        atletaEntry.pack(fill="x", padx=5, pady=5)
        nacaoLabel.pack(padx=5, pady=5)
        nacaoEntry.pack(fill="x", padx=5, pady=5)
        resultadoLabel.pack(padx=5, pady=5)
        listBox.pack(fill="x", padx=5, pady=5)
        scrollBar.pack(side='right')
        
        rodar.pack(fill="x", padx=5, pady=5)
        pdf.pack(fill="x", padx=5, pady=5)
        voltar.pack(fill="x", padx=5, pady=5)

class ListarTreinador(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global listBox

        label = tk.Label(self, text="Listagem por treinador", font=controller.title_font)

        atletaLabel = tk.Label(self, text="Aperte o botão rodar para realizar a tarefa.")
       
        resultadoLabel = tk.Label(self, text="Resultado:")

        listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(listBox)

        scrollBar.configure(command=listBox.yview)
        listBox.configure(yscrollcommand=scrollBar.set)
        listBox.bind('<<ListboxSelect>>', get_linha_selecionada)
        
        rodar = tk.Button(self, text="Rodar", command=controller.base.gerar_relatorio_treinador)
        voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Relatorios'))
        pdf = tk.Button(self, text="Gerar PDF", command=controller.base.gerar_relatorio_treinador)

        label.pack(padx=5, pady=5)
        atletaLabel.pack(padx=5, pady=5)
        resultadoLabel.pack(padx=5, pady=5)
        listBox.pack(fill="x", padx=5, pady=5)
        scrollBar.pack(side='right')
        
        rodar.pack(fill="x", padx=5, pady=5)
        pdf.pack(fill="x", padx=5, pady=5)
        voltar.pack(fill="x", padx=5, pady=5)

class Scripts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Scripts", font=controller.title_font)
        text = tk.Label(self, text="Os scripts se encontram na pasta 'scripts' no mesmo diretório.")
        
        menu = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Menu'))
        
        label.pack(padx=5, pady=5)
        text.pack(padx=5, pady=5)
        
        menu.pack(fill="x", padx=5, pady=5)

# --------------------------------- SISTEMA ---------------------------------- #

class olimpiadas(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Olimpíada 2020 - Tóquio")
        self.base = baseDeDados()

        global modalidadeStr, medicoStr, treinadorStr, atetlaStr, nacaoStr
        
        modalidadeStr = tk.StringVar(self)
        medicoStr = tk.StringVar(self)
        treinadorStr = tk.StringVar(self)
        atetlaStr = tk.StringVar(self)
        nacaoStr = tk.StringVar(self)

        self.title_font = tkfont.Font(family="Arial", size=18, weight="bold", slant="italic")

        container = tk.LabelFrame(self, text="Ações", padx=0, pady=0)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Relacao, Relatorios, Scripts, ListarAtletas, ListarMedicos, ListarTreinador):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Motre a tela na janela da interface selcionada'''
        frame = self.frames[page_name]
        frame.tkraise()

    def encerrar(self):
        self.base.fechar_conexao()
        self.destroy()

# ---------------------------------- MAIN ------------------------------------ #

app = olimpiadas()
app.mainloop()

# ----------------------------------- EOF ------------------------------------ #
