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
from BD.SGBD import SGBD

# ------------------------------------ PDF ----------------------------------- #

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(80, 10, 'Olimpíadas 2020 - Tóquio', 1, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# ------------------------------------ SGBD ---------------------------------- #

class baseDeDados(SGBD):
    def __init__(self, dbname=None, user=None, password=None, host=None, port=None):
        SGBD.__init__(self, dbname, user, password, host, port)
        self.pdf = PDF()

    def atualizar_relacao(self, fruta, preco, quantidade):
        print('Editado')
    
    def fechar_conexao(self):
        self.encerrar()

# --------------------------------- INTERFACE -------------------------------- #

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
        self.quantidadeStr = tk.StringVar()
        self.frutaStr = tk.StringVar()
        self.precoStr = tk.StringVar()

        label = tk.Label(self, text="Gerenciar relação", font=controller.title_font)
        text_intro = tk.Label(self, text="Selecione a tupla que deseja editar, depois faça as alterações e salve.")

        resultadoLabel = tk.Label(self, text="Resultado:")

        self.listBox = tk.Listbox(self, height=6, width=50, selectmode=tk.SINGLE)
        scrollBar = tk.Scrollbar(self.listBox)

        self.visualizar_relacao()
        
        scrollBar.configure(command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=scrollBar.set)
        self.listBox.bind('<<ListboxSelect>>', self.get_linha_selecionada)

        frutaLabel = tk.Label(self, text="Fruta:")
        self.frutaEntry = tk.Entry(self, textvariable=self.frutaStr, width=50)
        
        quantidadeLabel = tk.Label(self, text="Quantidade:")
        self.quantidadeEntry = tk.Entry(self, textvariable=self.quantidadeStr, width=50)

        precoLabel = tk.Label(self, text="Preço:")
        self.precoEntry = tk.Entry(self, textvariable=self.precoStr, width=50)
        
        salvar = tk.Button(self, text="Salvar", command=self.editar_relacao)
        menu = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Menu'))
        
        label.pack(padx=5, pady=5)
        text_intro.pack(padx=5, pady=5)
        frutaLabel.pack(padx=5, pady=5)
        self.frutaEntry.pack(fill="x", padx=5, pady=5)
        precoLabel.pack(padx=5, pady=5)
        self.precoEntry.pack(fill="x", padx=5, pady=5)
        quantidadeLabel.pack(fill="x", padx=5, pady=5)
        self.quantidadeEntry.pack(fill="x", padx=5, pady=5)
        resultadoLabel.pack(padx=5, pady=5)
        self.listBox.pack(fill="both", expand=True, padx=5, pady=5)
        scrollBar.pack(fill="both", side='right')

        salvar.pack(fill="x", padx=5, pady=5)
        menu.pack(fill="x", padx=5, pady=5)

    def get_linha_selecionada(self, event):
        """Função para carregar os dados selecionados pelo usuário nos campos de edição"""
        tupla_selecionada = self.listBox.get(self.listBox.curselection()[0])
        self.frutaEntry.delete(0, tk.END)
        self.quantidadeEntry.delete(0, tk.END)
        self.precoEntry.delete(0, tk.END)
        self.frutaEntry.insert(0, tupla_selecionada[0])
        self.quantidadeEntry.insert(0, tupla_selecionada[1])
        self.precoEntry.insert(0, tupla_selecionada[2])
    
    def visualizar_relacao(self):
        self.listBox.delete(0, tk.END)
        for row in self.controller.base.visualizar():
            self.listBox.insert(tk.END, row)
    
    def editar_relacao(self):
        self.controller.base.atualizar_relacao(self.frutaStr.get(), self.quantidadeStr.get(), self.precoStr.get())
        self.visualizar_relacao()

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
        self.modalidadeStr = tk.StringVar()
        self.medicoStr = tk.StringVar()
        self.treinadorStr = tk.StringVar()

        label = tk.Label(self, text="Listagem por atletas", font=controller.title_font)
        
        modalidadeLabel = tk.Label(self, text="Digite o nome da modalidade:")
        modalidadeEntry = tk.Entry(self, textvariable=self.modalidadeStr, width=50)
        
        medicoLabel = tk.Label(self, text="Digite o nome do médico:")
        medicoEntry = tk.Entry(self, textvariable=self.medicoStr, width=50)
        
        treinadorLabel = tk.Label(self, text="Digite o nome do treinador:")
        treinadorEntry = tk.Entry(self, textvariable=self.treinadorStr, width=50)

        resultadoLabel = tk.Label(self, text="Resultado:")

        self.listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(self.listBox)

        scrollBar.configure(command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=scrollBar.set)

        pesquisar = tk.Button(self, text="Pesquisar", command=self.pesquisar_atletas)
        voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Relatorios'))
        pdf = tk.Button(self, text="Gerar PDF", command=self.relatorio)
        
        label.pack(padx=5, pady=5)
        modalidadeLabel.pack(padx=5, pady=5)
        modalidadeEntry.pack(fill="x", padx=5, pady=5)
        medicoLabel.pack(padx=5, pady=5)
        medicoEntry.pack(fill="x", padx=5, pady=5)
        treinadorLabel.pack(padx=5, pady=5)
        treinadorEntry.pack(fill="x", padx=5, pady=5)
        
        pesquisar.pack(fill="x", padx=5, pady=5)
        
        resultadoLabel.pack(padx=5, pady=5)
        self.listBox.pack(fill='both', expand=True, padx=5, pady=5)
        scrollBar.pack(fill='both', side='right')

        pdf.pack(fill="x", padx=5, pady=5)
        voltar.pack(fill="x", padx=5, pady=5)
    
    def pesquisar_atletas(self):
        self.listBox.delete(0, tk.END)
        for row in self.controller.base.visualizar():
            self.listBox.insert(tk.END, row)

    def relatorio(self):        
        queries = self.listBox.get(0, last=tk.END);

        if len(queries) > 0 and self.controller.pdfGerado != queries[0] and self.controller.pdfErro != queries[0]:
            for row in queries:
                self.controller.pdf.cell(0, 10, 'Modalidade: ' + str(row[0]), 0, 1)
                self.controller.pdf.cell(0, 10, 'Médico: ' + str(row[1]), 0, 1)
                self.controller.pdf.cell(0, 10, 'Treinador: ' + str(row[2]), 0, 1)
            
            self.controller.pdf.output('atleta.pdf', 'F')
            self.listBox.delete(0, tk.END)
            self.listBox.insert(tk.END, self.controller.pdfGerado)
        
        else:
            self.listBox.delete(0, tk.END)
            self.listBox.insert(tk.END, self.controller.pdfErro)

class ListarMedicos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.atletaStr = tk.StringVar()
        self.nacaoStr = tk.StringVar()

        label = tk.Label(self, text="Listagem por médicos", font=controller.title_font)
        
        atletaLabel = tk.Label(self, text="Digite o nome do atetla:")
        atletaEntry = tk.Entry(self, textvariable=self.atletaStr, width=50)
        
        nacaoLabel = tk.Label(self, text="Digite o nome da nação:")
        nacaoEntry = tk.Entry(self, textvariable=self.nacaoStr, width=50)
        
        resultadoLabel = tk.Label(self, text="Resultado:")

        self.listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(self.listBox)

        scrollBar.configure(command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=scrollBar.set)

        pesquisar = tk.Button(self, text="Pesquisar", command=self.pesquisar_medicos)
        voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Relatorios'))
        pdf = tk.Button(self, text="Gerar PDF", command=self.relatorio)
        
        label.pack(padx=5, pady=5)
        atletaLabel.pack(padx=5, pady=5)
        atletaEntry.pack(fill="x", padx=5, pady=5)
        nacaoLabel.pack(padx=5, pady=5)
        nacaoEntry.pack(fill="x", padx=5, pady=5)
        
        pesquisar.pack(fill="x", padx=5, pady=5)
        
        resultadoLabel.pack(padx=5, pady=5)
        self.listBox.pack(fill="both", expand=True, padx=5, pady=5)
        scrollBar.pack(fill='both', side='right')
        
        pdf.pack(fill="x", padx=5, pady=5)
        voltar.pack(fill="x", padx=5, pady=5)

    def pesquisar_medicos(self):
        self.listBox.delete(0, tk.END)
        for row in self.controller.base.visualizar():
            self.listBox.insert(tk.END, row)

    def relatorio(self):        
        queries = self.listBox.get(0, last=tk.END);

        if len(queries) > 0 and self.controller.pdfGerado != queries[0] and self.controller.pdfErro != queries[0]:            
            for row in queries:
                self.controller.pdf.cell(0, 10, 'Modalidade: ' + str(row[0]), 0, 1)
                self.controller.pdf.cell(0, 10, 'Médico: ' + str(row[1]), 0, 1)
                self.controller.pdf.cell(0, 10, 'Treinador: ' + str(row[2]), 0, 1)
            
            self.controller.pdf.output('medico.pdf', 'F')
            self.listBox.delete(0, tk.END)
            self.listBox.insert(tk.END, self.controller.pdfGerado)
        
        else:
            self.listBox.delete(0, tk.END)
            self.listBox.insert(tk.END, self.controller.pdfErro)

class ListarTreinador(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Listagem por treinador", font=controller.title_font)

        atletaLabel = tk.Label(self, text="Aperte o botão rodar para realizar a tarefa.")
       
        resultadoLabel = tk.Label(self, text="Resultado:")

        self.listBox = tk.Listbox(self, height=6, width=50)
        scrollBar = tk.Scrollbar(self.listBox)

        scrollBar.configure(command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=scrollBar.set)
        
        pesquisar = tk.Button(self, text="Pesquisar", command=self.pesquisar_treinador)
        voltar = tk.Button(self, text="Voltar", command=lambda: controller.show_frame('Relatorios'))
        pdf = tk.Button(self, text="Gerar PDF", command=self.relatorio)

        label.pack(padx=5, pady=5)
        atletaLabel.pack(padx=5, pady=5)
        
        pesquisar.pack(fill="x", padx=5, pady=5)
        
        resultadoLabel.pack(padx=5, pady=5)
        self.listBox.pack(fill="both", expand=True, padx=5, pady=5)
        scrollBar.pack(fill='both', side='right')
        
        pdf.pack(fill="x", padx=5, pady=5)
        voltar.pack(fill="x", padx=5, pady=5)
    
    def pesquisar_treinador(self):
        self.listBox.delete(0, tk.END)
        for row in self.controller.base.visualizar():
            self.listBox.insert(tk.END, row)

    def relatorio(self):        
        queries = self.listBox.get(0, last=tk.END);

        if len(queries) > 0 and self.controller.pdfGerado != queries[0] and self.controller.pdfErro != queries[0]:            
            for row in queries:
                self.controller.pdf.cell(0, 10, 'Modalidade: ' + str(row[0]), 0, 1)
                self.controller.pdf.cell(0, 10, 'Médico: ' + str(row[1]), 0, 1)
                self.controller.pdf.cell(0, 10, 'Treinador: ' + str(row[2]), 0, 1)
            
            self.controller.pdf.output('treinador.pdf', 'F')
            self.listBox.delete(0, tk.END)
            self.listBox.insert(tk.END, self.controller.pdfGerado)
        
        else:
            self.listBox.delete(0, tk.END)
            self.listBox.insert(tk.END, self.controller.pdfErro)

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
        self.pdf = PDF()
        self.pdf.set_font('Times', '', 12)
        self.pdf.add_page()
        self.pdfGerado = 'PDF gerado e salvo.'
        self.pdfErro = 'Realize uma busca antes.'

        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Olimpíada 2020 - Tóquio")
        self.base = baseDeDados(dbname='postgres', user='postgres', password='postgres123', host='localhost', port='5432')
        
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
