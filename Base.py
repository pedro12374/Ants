Area = []
import  random
Variaveis = ["A","B","C","D","E"]
Ant = 'X'


for i in range(0,5):
    o = ["O"]*5
    Area.append(o)

def print_board(board):
    for i in board:
        print i

def gerar_mapa(X):
    for i in range(len(X)):

        for j in range(len(X)):
            V = random.randrange(0, 5)
            X[i][j] = Variaveis[V]
    X[0][0] = Ant
    for k in X:
        print k


gerar_mapa(Area)

def indice(elemento, lista):
    for i,l in enumerate(lista):
        try:
            return (i, l.index(elemento))
        except:
            pass
    raise ValueError("Nao deu nao")


def andar(X,StrPont):

    FinPont = 0
    while indice("X",X) != (4,4):
        p = random.randrange(0,4)
        print p
        if (p) == 0 and indice("X",X)[0] != 4:
            l = indice("X",X)
            L = l[0]
            C = l[1]
            if X[L + 1][C] != "O":
                Area[L][C] = "O"
                if Area[L + 1][C] == "A":
                    FinPont = StrPont - 2
                elif Area[L + 1][C] == "B":
                    FinPont = StrPont - 1
                elif Area[L + 1][C] == "C":
                    FinPont = StrPont + 0
                elif Area[L + 1][C] == "D":
                    FinPont = StrPont + 1
                elif Area[L + 1][C] == "E":
                    FinPont = StrPont + 2

                Area[L + 1][C] = "X"



            print print_board(Area)
            print str(FinPont) + "  Pontos"
        elif (p) == 1 and indice("X",X)[1] != 0:
            l = indice("X", X)
            L = l[0]
            C = l[1]
            if X[L][C - 1] != "O":
                Area[L][C] = "O"
                if Area[L][C - 1] == "A":
                    FinPont = StrPont - 2
                elif Area[L][C - 1] == "B":
                    FinPont = StrPont - 1
                elif Area[L][C - 1] == "C":
                    FinPont = StrPont + 0
                elif Area[L][C - 1] == "D":
                    FinPont = StrPont + 1
                elif Area[L][C - 1] == "E":
                    FinPont = StrPont + 2

                Area[L][C - 1] = "X"


            print print_board(Area)
            print str(FinPont) + "  Pontos"
        elif (p) == 2 and indice("X", X)[0] != 0:
            l = indice("X", X)
            L = l[0]
            C = l[1]
            if X[L - 1][C] != "O":
                Area[L][C] = "O"
                if Area[L - 1][C] == "A":
                    FinPont = StrPont - 2
                elif Area[L - 1][C] == "B":
                    FinPont = StrPont - 1
                elif Area[L - 1][C] == "C":
                    FinPont = StrPont + 0
                elif Area[L - 1][C] == "D":
                    FinPont = StrPont + 1
                elif Area[L - 1][C] == "E":
                    FinPont = StrPont + 2

                Area[L - 1][C] = "X"



            print print_board(Area)
            print str(FinPont) + "  Pontos"
        elif (p) == 3 and indice("X", X)[1] != 4:
            l = indice("X", X)
            L = l[0]
            C = l[1]
            if X[L][C + 1] != "O":
                Area[L][C] = "O"
                if Area[L][C + 1] == "A":
                    FinPont = StrPont - 2
                elif Area[L][C + 1] == "B":
                    FinPont = StrPont - 1
                elif Area[L][C + 1] == "C":
                    FinPont = StrPont + 0
                elif Area[L][C + 1] == "D":
                    FinPont = StrPont + 1
                elif Area[L][C + 1] == "E":
                    FinPont = StrPont + 2

                Area[L][C + 1] = "X"

            print print_board(Area)
            print str(FinPont) + "  Pontos"

        elif indice("X",X) == (4,4):
            break
    print str(FinPont) + "  Pontos Finais"




andar(Area,0)
print print_board(Area)


