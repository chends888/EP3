import sys
import os
import tkinter as tk
from tkinter import messagebox
import numpy as np


a = np.zeros([3,3])


click = True
   
           
class Tabuleiro:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('jogo da velha')
        self.window.geometry("400x400+100+100")
        self.window.rowconfigure(0, weight = 3)
        self.window.rowconfigure(1, weight = 3)
        self.window.rowconfigure(2, weight = 3)
        self.window.rowconfigure(3, weight = 1)
        self.window.columnconfigure(0, weight = 3)
        self.window.columnconfigure(1, weight = 3)
        self.window.columnconfigure(2, weight = 3)



        self.botao1 = tk.Button(self.window)
        self.botao1.grid(row = 0, column = 0, sticky="nsew")
        self.botao1.configure(command = self.botao_clicado1)
        self.botao2 = tk.Button(self.window)
        self.botao2.grid(row = 0, column = 1, sticky="nsew")
        self.botao2.configure(command = self.botao_clicado2)
        self.botao3 = tk.Button(self.window)
        self.botao3.grid(row = 0, column = 2, sticky="nsew")
        self.botao3.configure(command = self.botao_clicado3)
        self.botao4 = tk.Button(self.window)
        self.botao4.grid(row = 1, column = 0, sticky="nsew")
        self.botao4.configure(command = self.botao_clicado4)
        self.botao5 = tk.Button(self.window)
        self.botao5.grid(row = 1, column = 1, sticky="nsew")
        self.botao5.configure(command = self.botao_clicado5)
        self.botao6 = tk.Button(self.window)
        self.botao6.grid(row = 1, column = 2, sticky="nsew")
        self.botao6.configure(command = self.botao_clicado6)
        self.botao7 = tk.Button(self.window)
        self.botao7.grid(row = 2, column = 0, sticky="nsew")
        self.botao7.configure(command = self.botao_clicado7)
        self.botao8 = tk.Button(self.window)
        self.botao8.grid(row = 2, column = 1, sticky="nsew")
        self.botao8.configure(command = self.botao_clicado8)
        self.botao9 = tk.Button(self.window)
        self.botao9.grid(row = 2, column = 2, sticky="nsew")
        self.botao9.configure(command = self.botao_clicado9)
        
        self.label = tk.Label(self.window)
        self.label.configure(text = "jogador 1")
        self.label.configure(font="Arial 12")
        self.label.grid(row=3, column=0, columnspan=3, sticky="nsew")
    def iniciar(self):
        self.window.mainloop()
        
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    def jogador(self, i, j):
        if click == True:
            self.label.configure(text = "jogador 1")
            a[i][j] = 1 
        else:
            self.label.configure(text = "jogador 2")
            a[i][j] = 2
            
    def verifica_ganhador(self):
        if (a[0][0] == 1 and a[0][1] == 1 and a[0][2] == 1 or a[1][0] == 1 and a[1][1] == 1 and a[1][2] == 1 or a[2][0] == 1 and a[2][1] == 1 and a[2][2] == 1 or a[0][0] == 1 and a[1][0] == 1 and a[2][0] == 1 or a[0][1] == 1 and a[1][1] == 1 and a[2][1] == 1 or a[0][2] == 1 and a[1][2] == 1 and a[2][2] == 1 or a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1 or a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1):
            tk.messagebox.showinfo ('Vencedor', 'Jogador 1 venceu')
            self.restart_program()
        elif (a[0][0] == 2 and a[0][1] == 2 and a[0][2] == 2 or a[1][0] == 2 and a[1][1] == 2 and a[1][2] == 2 or a[2][0] == 2 and a[2][1] == 2 and a[2][2] == 2 or a[0][0] == 2 and a[1][0] == 2 and a[2][0] == 2 or a[0][1] == 2 and a[1][1] == 2 and a[2][1] == 2 or a[0][2] == 2 and a[1][2] == 2 and a[2][2] == 2 or a[0][0] == 2 and a[1][1] == 2 and a[2][2] == 2 or a[0][2] == 2 and a[1][1] == 2 and a[2][0] == 2):
            tk.messagebox.showinfo ('Vencedor', 'Jogador 2 venceu')
            self.restart_program()
        elif (a[0][0] != 0 and a[0][1] != 0 and a[0][2] != 0 and a[1][0] != 0 and a[1][1] != 0 and a[1][2] != 0 and a[2][0] != 0 and a[2][1] != 0 and a[2][2] != 0):
            tk.messagebox.showinfo ('Deu velha', 'Empate')
            self.restart_program()

        
        
    def botao_clicado1(self):
        global click
        if click == True:
            self.botao1.configure(text = "X")
            self.botao1.configure(font = "Arial 14")
            self.botao1.configure(state = "disabled")
            self.jogador(0,0)
            self.verifica_ganhador ()
            click = False
            
            
        else:
            self.botao1.configure(text = "O")
            self.botao1.configure(font = "Arial 14")
            self.botao1.configure(state = "disabled")
            self.jogador(0,0)
            self.verifica_ganhador ()
            click = True
        
    def botao_clicado2(self):
        global click
        if click == True:
            self.botao2.configure(text = "X")
            self.botao2.configure(font = "Arial 14")
            self.botao2.configure(state = "disabled")
            self.jogador(0,1)
            self.verifica_ganhador ()
            click = False
            
        else:
            self.botao2.configure(text = "O")
            self.botao2.configure(font = "Arial 14")
            self.botao2.configure(state = "disabled")
            self.jogador(0,1)
            self.verifica_ganhador ()
            click = True

    def botao_clicado3(self):
        global click
        if click == True:
            self.botao3.configure(text = "X")
            self.botao3.configure(font = "Arial 14")
            self.botao3.configure(state = "disabled")
            self.jogador(0,2)
            self.verifica_ganhador ()
            click = False
            
        else:
            self.botao3.configure(text = "O")
            self.botao3.configure(font = "Arial 14")
            self.botao3.configure(state = "disabled")
            self.jogador(0,2)
            self.verifica_ganhador ()
            click = True
        
    def botao_clicado4(self):
        global click
        if click == True:
            self.botao4.configure(text = "X")
            self.botao4.configure(font = "Arial 14")
            self.botao4.configure(state = "disabled")
            self.jogador(1,0)
            self.verifica_ganhador ()
            click = False
        
        else:
            self.botao4.configure(text = "O")
            self.botao4.configure(font = "Arial 14")
            self.botao4.configure(state = "disabled")
            self.jogador(1,0)
            self.verifica_ganhador ()
            click = True
           
    def botao_clicado5(self):
        global click
        if click == True:
            self.botao5.configure(text = "X")
            self.botao5.configure(font = "Arial 14")
            self.botao5.configure(state = "disabled")
            self.jogador(1,1)
            self.verifica_ganhador ()
            click = False
            
        else:
            self.botao5.configure(text = "O")
            self.botao5.configure(font = "Arial 14")
            self.botao5.configure(state = "disabled")
            self.jogador(1,1)
            self.verifica_ganhador ()
            click = True    
           
    def botao_clicado6(self):
        global click
        if click == True:
            self.botao6.configure(text = "X")
            self.botao6.configure(font = "Arial 14")
            self.botao6.configure(state = "disabled")
            self.jogador(1,2)
            self.verifica_ganhador ()
            click = False
            
        else:
            self.botao6.configure(text = "O")
            self.botao6.configure(font = "Arial 14")
            self.botao6.configure(state = "disabled")
            self.jogador(1,2)
            self.verifica_ganhador ()
            click = True
        
    def botao_clicado7(self):
        global click
        if click == True:
            self.botao7.configure(text = "X")
            self.botao7.configure(font = "Arial 14")
            self.botao7.configure(state = "disabled")
            self.jogador(2,0)
            self.verifica_ganhador ()
            click = False
            
        else:
            self.botao7.configure(text = "O")
            self.botao7.configure(font = "Arial 14")
            self.botao7.configure(state = "disabled")
            self.jogador(2,0)
            self.verifica_ganhador ()
            click = True     
            
    def botao_clicado8(self):
        global click
        if click == True:
            self.botao8.configure(text = "X")
            self.botao8.configure(font = "Arial 14")
            self.botao8.configure(state = "disabled")
            self.jogador(2,1)
            self.verifica_ganhador ()
            click = False
            
        else:
            self.botao8.configure(text = "O")
            self.botao8.configure(font = "Arial 14")
            self.botao8.configure(state = "disabled")
            self.jogador(2,1)
            self.verifica_ganhador ()
            click = True 

    def botao_clicado9(self):
        global click
        if click == True:
            self.botao9.configure(text = "X")
            self.botao9.configure(font = "Arial 14")
            self.botao9.configure(state = "disabled")
            self.jogador(2,2)
            self.verifica_ganhador ()
            click = False
            
            
        else:
            self.botao9.configure(text = "O")
            self.botao9.configure(font = "Arial 14")
            self.botao9.configure(state = "disabled")
            self.jogador(2,2)
            self.verifica_ganhador ()
            click = True


tab = Tabuleiro()
tab.iniciar()