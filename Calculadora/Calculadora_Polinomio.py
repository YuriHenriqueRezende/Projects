# A calculator of the second degree, which when entering the values ​​of A B C, will display the results of delta, x and be able to plot a graph #
## importando a biblioteca ##
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np

## Variaveis ##
janelaoi = Tk()
canvas = None
i = 0

## MAIN ##
class equacaosegundograu():
    def __init__(j):
        j.janela = janelaoi
        j.janelaa()
        j.dados()
        j.canvas = canvas

        # criando o Loop
        janelaoi.mainloop()

    ## criando a janela ##
    def janelaa(j):
        j.janela.title("EQUAÇÃO DO 2° GRAU")
        j.janela.geometry('1300x900')
        #j.janela.iconbitmap('C:\\Users\\yurih\\Documents\\Programações\\LIP\\Downloads\\calc.ico')
        j.janela.resizable(False, False)
        j.janela.configure(background='#B0C4DE')

    # Criação de formas, textos, botao, e setando os textos de entrada e textos de saida
    def dados(j):
        j.a_entrada = IntVar()
        j.janela.lb_a = Label(text='A:',
                              font=('Verdana', '8', 'bold'),
                              bg='#D3D3D3', fg='#000000')
        j.janela.lb_a.place(relx=0.1, rely=0.05, relwidth=0.1,
                            relheight=0.1)
        j.janela.input_a = Entry(textvariable=j.a_entrada)
        j.janela.input_a.place(relx=0.2, rely=0.05, relwidth=0.10,
                               relheight=0.1)

        j.b_entrada = IntVar()
        j.janela.lb_b = Label(text='B:',
                              font=('Verdana', '8', 'bold'),
                              bg='#D3D3D3', fg='#000000')
        j.janela.lb_b.place(relx=0.1, rely=0.2, relwidth=0.1,
                            relheight=0.1)
        j.janela.input_b = Entry(textvariable=j.b_entrada)
        j.janela.input_b.place(relx=0.2, rely=0.2, relwidth=0.10,
                               relheight=0.1)

        j.c_entrada = IntVar()
        j.janela.lb_c = Label(text='C:',
                              font=('Verdana', '8', 'bold'),
                              bg='#D3D3D3', fg='#000000')
        j.janela.lb_c.place(relx=0.1, rely=0.35, relwidth=0.1,
                            relheight=0.1)
        j.janela.input_c = Entry(textvariable=j.c_entrada)
        j.janela.input_c.place(relx=0.2, rely=0.35, relwidth=0.10,
                               relheight=0.1)

        j.janela.bt_calcular = Button(text='Calcular',
                                      font=("verdana", 10, "bold"),
                                      command=j.calculo)
        j.janela.bt_calcular.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.1)

        j.janela.grafico = Button(text='grafico',
                                      font=("verdana", 10, "bold"),
                                      command=j.grafico)
        j.janela.grafico.place(relx=0.7, rely=0.55, relwidth=0.2, relheight=0.1)

        j.janela.limpar = Button(text='limpar',
                                      font=("verdana", 10, "bold"),
                                      command=j.limpar)
        j.janela.limpar.place(relx=0.1, rely=0.55, relwidth=0.2, relheight=0.1)

        # Resultado
        j.resulfinal = StringVar()
        j.janela.resulfinal_ld = Label(textvariable=j.resulfinal)
        j.janela.resulfinal_ld.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

    #Cria Função Calculo
    def calculo(j):


        #Entrada de valores
        a = j.a_entrada.get()
        b = j.b_entrada.get()
        c = j.c_entrada.get()

        #Calculo:
        if a != 0:

            delta = b ** 2 - 4 * a * c

            if (delta == 0):
                x1 = (-b + (delta ** (1 /2))) / (2 * a)
                if a > 0:
                     final = 'delta: ' + str(delta)+'         ' +'X1: '+ str(x1) + '         ' + 'APENAS UMA RAIZ' +'         '+  'concavidade para cima'
                elif a < 0:
                    final = 'delta:  ' + str(delta)+'         ' +'X1: '+ str(x1 )+ '         ' + 'APENAS UMA RAIZ' +'         '+ 'concavidade para baixo'
            elif delta > 0:
                x1 = (-b + (delta) ** (1 / 2)) / (2 * a)
                x2 = (-b - (delta) ** (1 / 2)) / (2 * a)
                if a > 0:
                    final = 'delta: ' + str(delta)+'         '+ 'X1: ' + str(x1) + '         '+'X2: '+ str(x2)+'         ' + 'DUAS RAIZ' + '        ' + 'concavidade para baixo'
                elif a <0:
                    final = 'delta: ' + str(delta)+'         '+'X1: ' + str(x1) + '         '+'X2: '+ str(x2)+'         ' + 'DUAS RAIZ' + '         ' + 'concavidade para cima'
            elif delta <0:
                if a > 0:
                    final = 'delta:  ' + str(delta)+'         ' + 'NENHUMA RAIZ' + '         ' +  'concavidade para baixo'
                elif a < 0:
                    final = 'delta:  ' + str(delta)+'         ' + 'NENHUMA RAIZ' + '         ' + 'concavidade para cima'
        else:
            final = "Não é uma equação do 2º grau!"

        #Retorno do Resultado, ou seja, o resultado entra na variavel no Final, que se seta como resultado final
        return j.resulfinal.set(final)


    #Função Criar o Grafico
    def grafico(j):
        #Puxa a função Limpar Grafico
        global i
        j.limpargrafico()
        i+=1

        #Criação do Grafico e Calculo
        fig = Figure(figsize=(8, 8),
                     dpi=60)

        x = np.linspace(-10, 10, 100)
        y = j.a_entrada.get() * x ** 2 + j.b_entrada.get() * x + j.c_entrada.get()

        ax = fig.add_subplot()
        ax.plot(x, y)

        j.canvas = FigureCanvasTkAgg(fig,
                                   master=janelaoi)
        # Execução
        j.canvas.draw()

        var = j.canvas.get_tk_widget()

        var.pack()

    #Função Limpar O Grafico
    def limpargrafico(j):
        #Ele esquece o widget do canvas
        if i != 0:
            j.canvas.get_tk_widget().pack_forget()

    #Função Limpar
    def limpar(j):
        #Limpar o Grafico
        j.limpargrafico()

        #Limpa as Entradas de Valores e Resultado
        final = ''
        j.resulfinal.set(final)
        zero = '0'
        j.a_entrada.set(zero)
        j.b_entrada.set(zero)
        j.c_entrada.set(zero)

equacaosegundograu()
