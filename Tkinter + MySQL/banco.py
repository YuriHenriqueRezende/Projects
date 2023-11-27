from tkinter import *
layout = Tk()


class banco():
    ## MAIN ##
    def __init__(self):
        self.janela = layout
        self.dados_menu()
        self.estrutura_menu()
        layout.mainloop()

    # Menu #
    def estrutura_menu(self):
        self.janela.title("Banco de Dados")
        self.janela.geometry('350x300')
        self.janela.resizable(False, False)
        self.janela.configure()

    def dados_menu(self):
        # Titulo_do_menu #
        self.texto0 = Label(self.janela, text='', font=('Verdana', '5', 'bold'))
        self.texto0.pack()
        self.texto1 = Label(self.janela, text='Banco de Dados MSQL', font=('Verdana', '12', 'bold'))
        self.texto1.pack()
        self.texto4 = Label(self.janela, text='', font=('Verdana', '5', 'bold'))
        self.texto4.pack()

        # Botao_do_menu #
        self.botao1 = Button(text='Interface Grafica de Banco de Dados', font=("verdana", 10, "bold",))
        self.botao1.place(relx=0.06, rely=0.26)
        self.botao3 = Button(text='About', font=("verdana", 10, "bold",), command=self.about)
        self.botao3.place(relx=0.41, rely=0.55)
        self.botao4 = Button(text='Exit', font=("verdana", 10, "bold",), command=self.janela.destroy)
        self.botao4.place(relx=0.43, rely=0.70)

    # About #
    def about(self):
        # Estrutura_do_about #
        self.about = Toplevel()
        self.about.title("About")
        self.about.geometry('250x200')
        self.about.resizable(False, False)
        self.about.configure()
        self.about.focus_force()
        self.about.grab_set()

        # Bot?o_do_about #
        self.botao_about = Button(self.about,text='Exit', font=("verdana", 10, "bold",), command=self.about.destroy)
        self.botao_about.place(relx=0.40, rely=0.70)

        # Texto_do_about#
        self.texto_about = Label(self.about, text='Interface e Banco de dados 1.0 (64 e 32 bit)')
        self.texto_about.place(relx=0.05, rely=0.01)
        self.texto_about1 = Label(self.about, text='Publicado por Yuri Henrique Rezende')
        self.texto_about1.place(relx=0.05, rely=0.11)
        self.texto_about2 = Label(self.about, text='Professor Orientador: Luciano Andre Santos')
        self.texto_about2.place(relx=0.05, rely=0.21)
        self.texto_about3 = Label(self.about, text='Apoio: Faculdade Senai "Roberto Mange" ')
        self.texto_about3.place(relx=0.05, rely=0.31)



banco()
