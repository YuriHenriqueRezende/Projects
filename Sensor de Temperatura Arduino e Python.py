## importando a biblioteca ##
from tkinter import *
from tkinter import ttk
import serial

## Variaveis ##
layout = Tk()

## MAIN ##
class sistema():
    def __init__(self):
        self.janela = layout
        self.estrutura()
        self.dados()

        layout.mainloop()

    def estrutura(self):
        self.janela.title("Sistema")
        self.janela.geometry('650x700')
        self.janela.resizable(False, False)
        self.janela.configure()

    def dados(self):
        self.colunas1 = Label(self.janela,background='gray')
        self.colunas1.place(relx=0, rely=0.35, relwidth=1, relheight=0.005)

        self.colunas2 = Label(self.janela, background='gray')
        self.colunas2.place(relx=0.5, rely=0.1, relwidth=0.01, relheight=0.25)

        self.colunas3 = Label(self.janela, background='gray')
        self.colunas3.place(relx=0, rely=0.10, relwidth=1, relheight=0.005)

        self.texto1 = Label(self.janela, text='SISTEMA DE CALCULO',font=('Verdana', '8', 'bold') )
        self.texto1.pack()

        self.texto2 = Label(self.janela, text='SELECIONE O SISTEMA OPERACIONAL', font=('Verdana', '8', 'bold'))
        self.texto2.pack()

        self.texto3 = Label(self.janela, text='SELECIONE  A  ENTRADA DE COMUNICAÇÃO DO ARDUINO', font=('Verdana', '8', 'bold'))
        self.texto3.pack()

        self.texto4 = Label(self.janela, text='SISTEMA OPERACIONAL', font=('Verdana', '8', 'bold'))
        self.texto4.place(relx=0.15, rely=0.12)

        self.texto5 = Label(self.janela, text='CONFIGURAÇÃO DO ARDUINO', font=('Verdana', '8', 'bold'))
        self.texto5.place(relx=0.62, rely=0.12)

        self.texto6 = Label(self.janela, text='DIGITE A ENTRADA DO ARDUINO:', font=('Verdana', '7'))
        self.texto6.place(relx=0.51, rely=0.17)

        self.texto7 = Label(self.janela, text='DIGITE A VELOCIDADE DE COMUNICAÇÃO:', font=('Verdana', '7'))
        self.texto7.place(relx=0.51, rely=0.20)

        self.caixa1 = IntVar()
        self.caixa1 = Entry(self.janela)
        self.caixa1.place(relx=0.81, rely=0.17,relwidth=0.06, relheight=0.03)

        self.caixa2 = IntVar()
        self.caixa2 = Entry(self.janela)
        self.caixa2.place(relx=0.89, rely=0.20,relwidth=0.06, relheight=0.03)

        self.botao1 = Button(text='conectar',font=("verdana", 10, "bold",),command=self.conectar)
        self.botao1.place(relx=0.60, rely=0.26, relwidth=0.12, relheight=0.05)

        self.botao2 = Button(text='desconectar',font=("verdana", 10, "bold"),command=self.desconectar)
        self.botao2.place(relx=0.75, rely=0.26, relwidth=0.16, relheight=0.05)

        self.botao3 = Button(text='fechar programa',font=("verdana", 10, "bold"),command=self.fechar)
        self.botao3.place(relx=0.11, rely=0.26, relwidth=0.25, relheight=0.05)

        self.botao4 = Button(text='testar programação',font=("verdana", 10, "bold"),command=self.programacao)
        self.botao4.place(relx=0.39, rely=0.50, relwidth=0.30, relheight=0.05)

        self.sistem = IntVar()
        self.botaoE = Radiobutton(text="Windows", variable=self.sistem, value=1).place(x=60, y=140)
        self.botaoE = Radiobutton(text="Linux", variable=self.sistem, value=2).place(x=180, y=140)

        self.resultado = StringVar()
        self.resultado_final = Label(self.janela,textvariable=self.resultado)
        self.resultado_final.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

    def conectar(self):
        serialPort = self.caixa1.get()
        velocidade = self.caixa2.get()
        sistema = self.sistem.get()
        try:
            if sistema == 2:
                try:
                    self.serial_objeto = serial.Serial('/dev/tty' + str(serialPort), velocidade)
                    self.texto8 = Label(self.janela, text='CONECTADO             ', font=('Verdana', '7'), foreground="green")
                    self.texto8.place(relx=0.64, rely=0.32)
                except:
                    self.texto9 = Label(self.janela, text='FALHA                  ', font=('Verdana', '7'), foreground="red")
                    self.texto9.place(relx=0.64, rely=0.32)
            elif sistema == 1:
                self.serial_objeto = serial.Serial('COM' + str(serialPort), velocidade)
                self.texto8 = Label(self.janela, text='CONECTADO                     ', font=('Verdana', '7'), foreground="green")
                self.texto8.place(relx=0.64, rely=0.32)
        except:
                self.texto9 = Label(self.janela, text='FALHA                         ', font=('Verdana', '7'), foreground="red")
                self.texto9.place(relx=0.64, rely=0.32)

    def desconectar(self):
        try:
            self.serial_objeto.close()
            self.texto9 = Label(self.janela, text='DESCONECTADO          ', font=('Verdana', '7'), foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)
        except:
            self.texto9 = Label(self.janela, text='DESCONECTADO          ', font=('Verdana', '7'), foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)

    def fechar(self):
        self.janela.quit()

    def programacao(self):
        try:
            linha = str(self.serial_objeto.readline())
            return self.resultado.set(linha[2:-5])
        except:
            self.texto9 = Label(self.janela, text='FALHA                  ', font=('Verdana', '7'), foreground="red")
            self.texto9.place(relx=0.64, rely=0.32)


sistema()