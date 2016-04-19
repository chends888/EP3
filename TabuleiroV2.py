import tkinter as tk

class Tabuleiro:
   
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('jogo da velha')        
        self.window.geometry("500x500+100+100")
        self.window.rowconfigure(0, weight = 1)
        self.window.rowconfigure(1, weight = 1)
        self.window.rowconfigure(2, weight = 1)
        self.window.columnconfigure(0, weight = 1)
        self.window.columnconfigure(1, weight = 1)
        self.window.columnconfigure(2, weight = 1)
    
        botão1 = tk.Button(self.window)
        botão1.grid(row = 0, column = 0, sticky="nsew")
        botão2 = tk.Button(self.window)
        botão2.grid(row = 0, column = 1, sticky="nsew")
        botão3 = tk.Button(self.window)
        botão3.grid(row = 0, column = 2, sticky="nsew")
        botão4 = tk.Button(self.window)
        botão4.grid(row = 1, column = 0, sticky="nsew")
        botão5 = tk.Button(self.window)
        botão5.grid(row = 1, column = 1, sticky="nsew")
        botão6 = tk.Button(self.window)
        botão6.grid(row = 1, column = 2, sticky="nsew")
        botão7 = tk.Button(self.window)
        botão7.grid(row = 2, column = 0, sticky="nsew")
        botão8 = tk.Button(self.window)
        botão8.grid(row = 2, column = 1, sticky="nsew")
        botão9 = tk.Button(self.window)
        botão9.grid(row = 2, column = 2, sticky="nsew")
        
    def iniciar(self):
        self.window.mainloop()


tab = Tabuleiro()
tab.iniciar()        
