import numpy as np
class jogo:

    def __init__(self):
        self.click = True
        self.a = np.zeros([3,3])
                
    def recebe_jogada(self, i, j):
        a = self.a
        if self.click == True:
            a[i][j] = 1
            self.click = False 
        else:
            a[i][j] = 2
            self.click = True
      
    def verifica_ganhador(self):
        a = self.a
        if (a[0][0] == 1 and a[0][1] == 1 and a[0][2] == 1 or a[1][0] == 1 and a[1][1] == 1 and a[1][2] == 1 or a[2][0] == 1 and a[2][1] == 1 and a[2][2] == 1 or a[0][0] == 1 and a[1][0] == 1 and a[2][0] == 1 or a[0][1] == 1 and a[1][1] == 1 and a[2][1] == 1 or a[0][2] == 1 and a[1][2] == 1 and a[2][2] == 1 or a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1 or a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1):
            return 1
        elif (a[0][0] == 2 and a[0][1] == 2 and a[0][2] == 2 or a[1][0] == 2 and a[1][1] == 2 and a[1][2] == 2 or a[2][0] == 2 and a[2][1] == 2 and a[2][2] == 2 or a[0][0] == 2 and a[1][0] == 2 and a[2][0] == 2 or a[0][1] == 2 and a[1][1] == 2 and a[2][1] == 2 or a[0][2] == 2 and a[1][2] == 2 and a[2][2] == 2 or a[0][0] == 2 and a[1][1] == 2 and a[2][2] == 2 or a[0][2] == 2 and a[1][1] == 2 and a[2][0] == 2):
            return 2
        elif (a[0][0] != 0 and a[0][1] != 0 and a[0][2] != 0 and a[1][0] != 0 and a[1][1] != 0 and a[1][2] != 0 and a[2][0] != 0 and a[2][1] != 0 and a[2][2] != 0):
            return -1
   
    def limpa_jogadas(self):
        self.a = np.zeros([3,3])
