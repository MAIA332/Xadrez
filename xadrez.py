import sys
#import itertools

# Entrada : peça posição, ex: peao c2, torre c3, bispo d1

class chess:   
    tabuleiro =[]
    
    def __init__(self,argv):
        pecas ={
            "peao":{
                "mov":lambda x: [x+1], #[1,argv[1]] -- Função de movimento da peça
                #"bvtype":"vertical", # border validation type, tipo de validação para o fim do tabuleiro
                "multiAngular":False # propriedade que verifica se a peça se move para mais de um ângulo (cima, baixo, esqueda, direita)
            },
            "torre":{
                "mov":self.rectilinear_move,
                #"bvtype":"vertival horizontal",
                "multiAngular":True # Validação multiangular ainda não existe
            },
            "bispo":{
                "mov":self.diagonal_move,
                #"bvtype":"vertical horizontal",
                "multiAngular":True
            },
            "cavalo":{
                "mov":"a",
                "multiAngular":True
            }
        }
                
        l = ['a','b','c','d','e','f','g','h']
        for i in l:
            for j in range(1,9):
                self.tabuleiro.append([i,str(j)])
        
        #converte a entrada "c2" em ['c','2']
        self.origin = self.tabuleiro[self.find_pos(argv[1])]

        #valida se existe movimentos válidos para o peao
        teste = self.border_validation(self.origin)
        if(teste[1] == 0 and pecas[argv[0]]["multiAngular"]==False and teste[1] != False):
            self.prox = None
        else:
            index_prox = pecas[argv[0]]['mov'](self.find_pos(argv[1]))
            self.prox = []

            for i in index_prox:
                self.prox.append(self.tabuleiro[i])
        
        #self.mov(pecas[argv[0]])
    
    def horse(self,aux):
        border = self.border_validation(self.origin)
        f = [lambda x: (x+2)-8,lambda x: (x+2)+8, lambda x: (x-2)+8,lambda x: (x-2)-8,lambda x:(x+1)-16,lambda x:(x+1)+16,lambda x:(x-1)+16,lambda x:(x-1)-16]



    def rectilinear_move(self,aux):
        #all index x* and *y
        valid = [self.find_pos(x) for x in self.tabuleiro if x[0] ==self.origin[0] or x[1] == self.origin[1]]
        return valid

    def diagonal_move(self,aux):
        border = self.border_validation(self.origin)
        f= [lambda x: x+9,lambda x:x-7,lambda x: x-9,lambda x:x+7]
        moves = {
            "[0, 0]":[f[2]],
            "[0, 1]":[f[1]],
            "[1, 0]":[f[3]],
            "[1, 1]":[f[0]],
            "[False, 0]":[f[2],f[3]],
            "[0, False]":[f[1],f[2]],
            "[False, 1]":[f[0],f[1]],
            "[1, False]":[f[0],f[3]],
            "[False, False]":[f[0],f[1],f[2],f[3]]
        }

        def search(function,aux):
            trigger=0
            valids =[]
            
            while(trigger ==0):
                
                tmp = function(aux)
                valids.append(tmp)
                aux = tmp

                b = self.border_validation(self.tabuleiro[tmp])
            
                if(str(b)!="[False, False]"):
                    trigger =1
            
            #temp = itertools.combinations(moves.keys(),2)
            return valids

        tmp = []
        for i in moves[str(border)]: 
            a = search(i,aux)
            tmp.append(a) 
        
        #print(tmp)

        z = len(tmp)
        valids = []
        for i in range(0,z):
            for j in tmp[i]:
                valids.append(j)
        
        #print(valids)
        return valids


    def find_pos(self,pos):
        i = 0
        for p in self.tabuleiro:
            if(pos[0] == p[0] and pos[1] == p[1]):
                return i
            else:
                i+=1

    def border_validation(self,argv):
        
        def verify_line(line):
            if(line == "8"):
                return 0
            elif(line=="1"):
                return 1
            else:
                return False
        
        def verify_column(column):
            if(column == 'h'):
                return 0
            elif(column =='a'):
                return 1
            else:
                return False
        
        bv = [verify_column(argv[0]),verify_line(argv[1])]
        return bv

    #peao = lambda x: x+1

#captura os argumentos passados na execução do programa e passa para o construtor da posição 1 em diante
g = sys.argv[1:] #input('input ')).split(" ")
c = chess(g)

#Verifica se há movimentos válidos e Busca na variável tabuleiro o pela posição correspondente ao index retornado pela função
if(c.prox == None):
    print(f"{g[0]} não tem movimentos válidos \n")
else:
    print(c.prox)

#print(c.find_pos(g[1]))
#C:/Users/lucas.maia/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/lucas.maia/Desktop/modulos/Desafios NM/xadrez.py" peao c2