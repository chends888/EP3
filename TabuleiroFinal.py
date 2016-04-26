import tkinter as tk
from tkinter import messagebox
from jogo import jogo

class Tabuleiro:

    def __init__(self):
        self.window = tk.Tk()
        self.jogo=jogo()
        self.window.title('jogo da velha')
        self.window.geometry("300x350+100+100")
        self.window.rowconfigure(0, weight = 3,minsize = 100)
        self.window.rowconfigure(1, weight = 3,minsize = 100)
        self.window.rowconfigure(2, weight = 3,minsize = 100)
        self.window.rowconfigure(3, weight = 1,minsize = 50)
        self.window.columnconfigure(0, weight = 3,minsize = 100)
        self.window.columnconfigure(1, weight = 3,minsize = 100)
        self.window.columnconfigure(2, weight = 3,minsize = 100)



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
        self.label.configure(text = "jogador X")
        self.label.configure(font="Arial 12")
        self.label.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
    def iniciar(self):
        self.window.mainloop()
        
    def limpa_tabuleiro(self):
        self.jogo.limpa_jogadas()
        self.botao1.configure(state= "normal")
        self.botao1.configure(text = "")
        self.botao2.configure(state= "normal")
        self.botao2.configure(text = "")
        self.botao3.configure(state= "normal")
        self.botao3.configure(text = "")
        self.botao4.configure(state= "normal")
        self.botao4.configure(text = "")
        self.botao5.configure(state= "normal")
        self.botao5.configure(text = "")
        self.botao6.configure(state= "normal")
        self.botao6.configure(text = "")
        self.botao7.configure(state= "normal")
        self.botao7.configure(text = "")
        self.botao8.configure(state= "normal")
        self.botao8.configure(text = "")
        self.botao9.configure(state= "normal")
        self.botao9.configure(text = "")
        
    def botao_clicado1(self):
        if self.jogo.click == True:
            self.botao1.configure(text = "X")
            self.botao1.configure(font = "Arial 14")
            self.botao1.configure(state = "disabled")
            self.jogo.recebe_jogada(0,0)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
                
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
                
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
        else:
            self.botao1.configure(text = "O")
            self.botao1.configure(font = "Arial 14")
            self.botao1.configure(state = "disabled")
            self.jogo.recebe_jogada(0,0)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
                
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
                
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
                
    def botao_clicado2(self):
        if self.jogo.click == True:
            self.botao2.configure(text = "X")
            self.botao2.configure(font = "Arial 14")
            self.botao2.configure(state = "disabled")
            self.jogo.recebe_jogada(0,1)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
                
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
            
        else:
            self.botao2.configure(text = "O")
            self.botao2.configure(font = "Arial 14")
            self.botao2.configure(state = "disabled")
            self.jogo.recebe_jogada(0,1)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
                
    def botao_clicado3(self):
        if self.jogo.click == True:
            self.botao3.configure(text = "X")
            self.botao3.configure(font = "Arial 14")
            self.botao3.configure(state = "disabled")
            self.jogo.recebe_jogada(0,2)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
            
        else:
            self.botao3.configure(text = "O")
            self.botao3.configure(font = "Arial 14")
            self.botao3.configure(state = "disabled")
            self.jogo.recebe_jogada(0,2)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()

    def botao_clicado4(self):
        if self.jogo.click == True:
            self.botao4.configure(text = "X")
            self.botao4.configure(font = "Arial 14")
            self.botao4.configure(state = "disabled")
            self.jogo.recebe_jogada(1,0)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
            
        else:
            self.botao4.configure(text = "O")
            self.botao4.configure(font = "Arial 14")
            self.botao4.configure(state = "disabled")
            self.jogo.recebe_jogada(1,0)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()

    def botao_clicado5(self):
        if self.jogo.click == True:
            self.botao5.configure(text = "X")
            self.botao5.configure(font = "Arial 14")
            self.botao5.configure(state = "disabled")
            self.jogo.recebe_jogada(1,1)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
            
        else:
            self.botao5.configure(text = "O")
            self.botao5.configure(font = "Arial 14")
            self.botao5.configure(state = "disabled")
            self.jogo.recebe_jogada(1,1)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()

    def botao_clicado6(self):
        if self.jogo.click == True:
            self.botao6.configure(text = "X")
            self.botao6.configure(font = "Arial 14")
            self.botao6.configure(state = "disabled")
            self.jogo.recebe_jogada(1,2)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()
            
        else:
            self.botao6.configure(text = "O")
            self.botao6.configure(font = "Arial 14")
            self.botao6.configure(state = "disabled")
            self.jogo.recebe_jogada(1,2)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()

    def botao_clicado7(self):
        if self.jogo.click == True:
            self.botao7.configure(text = "X")
            self.botao7.configure(font = "Arial 14")
            self.botao7.configure(state = "disabled")
            self.jogo.recebe_jogada(2,0)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate') 
                self.limpa_tabuleiro()
            
        else:
            self.botao7.configure(text = "O")
            self.botao7.configure(font = "Arial 14")
            self.botao7.configure(state = "disabled")
            self.jogo.recebe_jogada(2,0)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()



    def botao_clicado8(self):
        if self.jogo.click == True:
            self.botao8.configure(text = "X")
            self.botao8.configure(font = "Arial 14")
            self.botao8.configure(state = "disabled")
            self.jogo.recebe_jogada(2,1)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')    
                self.limpa_tabuleiro()
            
        else:
            self.botao8.configure(text = "O")
            self.botao8.configure(font = "Arial 14")
            self.botao8.configure(state = "disabled")
            self.jogo.recebe_jogada(2,1)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate') 
                self.limpa_tabuleiro()


    def botao_clicado9(self):
        if self.jogo.click == True:
            self.botao9.configure(text = "X")
            self.botao9.configure(font = "Arial 14")
            self.botao9.configure(state = "disabled")
            self.jogo.recebe_jogada(2,2)
            self.label.configure(text = "jogador O")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate') 
                self.limpa_tabuleiro()
            
        else:
            self.botao9.configure(text = "O")
            self.botao9.configure(font = "Arial 14")
            self.botao9.configure(state = "disabled")
            self.jogo.recebe_jogada(2,2)
            self.label.configure(text = "jogador X")
            v = self.jogo.verifica_ganhador ()
            if v == 1:
                tk.messagebox.showinfo ('Vencedor', 'Jogador X venceu')
                self.limpa_tabuleiro()
            elif v == 2:
                tk.messagebox.showinfo ('Vencedor', 'Jogador O venceu')
                self.limpa_tabuleiro()
            elif v == -1:
                tk.messagebox.showinfo ('Vencedor', 'empate')
                self.limpa_tabuleiro()


tab = Tabuleiro()
tab.iniciar()