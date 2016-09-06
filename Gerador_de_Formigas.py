import  random
import os 
import shutil

direc = os.getcwd()


def gerador():
    numeros = []
    for i in range(random.randrange(10,26)):
        str(numeros.append(random.randrange(0,4)))
    #print numeros
    #print len(numeros)
    return numeros
    
 
def AntsGen(quant):
    shutil.rmtree(str(direc) + "\Ants") #Exclui a pasta Ants
    os.makedirs(str(direc) + "\Ants") #Recria a pasta Ants
    for i in range(quant):
        temp = gerador()
        f = open(str(direc) + "\Ants\Ant" + str(i) + ".txt","w")
        for c in temp:
            f.write(str(c) + "\n")
        f.close()

def AntsReader():
    n = len(os.listdir(str(direc) + "\Ants"))#conta quantos arquivos tem no diretorio    
    dct = {}
    for i in range(n):
        open(str(direc) + "\Ants\Ant" + str(i) + ".txt","r" )
        names =[]        
        names.append(i)
        Ants = []
        with open(str(direc) + "\Ants\Ant" + str(i) + ".txt") as f:
            linhas = f.read().splitlines()            
            for k in names:         
                for m in linhas:
                    Ants.append(int(m))
                dct['Ant_%s' %k] = Ants
    return dct
        
                


