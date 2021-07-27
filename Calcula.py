# Classe recebe a lista classificada, a não classificada e o índice de da lista não classificada

class CalculaDistancia:
    '''
    Classe que recebe uma lista já classificada: [49962942971, 'Agressivo', (6700., 3300., 5700., 2500.)],
    uma lista não classificada: [52559670741, '', (5700., 4400., 1500., 400.)] e um valor para K vizinhos
    mais próximos. Com o auxílio de seus métodos implementa o k-nearest neighbors algorithm (KNN) e classifica
    os perfis de investidores em: Consevador, Moderado ou Agressivo.
    '''
    
    perfis_classificados = {}
    
    def __init__(self, lista_indefinida, lista_definida, K):
        self.lista_indefinida = lista_indefinida
        self.lista_definida = lista_definida
        self.K = K
        
    def fun_principal(self):
        for i in range(len(self.lista_indefinida)):
            self.define_perfil(i)
        
    def ordena_lista(self, lista):
        '''
        Método que recebe uma lista de listas de dois elementos, e a ordena pelo segundo elemento.
        '''
        
        aux = []         
        indice = 0       
        valor = 0
        for i in range(len(lista)):  # lista = [indice, valor]
            indice = lista[i][0]   # pega o índice
            valor = lista[i][1]    # pega o valor
            aux.append([valor, indice])  # Troca o índice e o valor de posição na lista para lista auxiliar =  [valor, indice]
        l = sorted(aux)     # Ordena a lista e armazena na lista l
        lista_ordenada = []
        for y in range(len(l)):
            valor = l[y][0]   # Devolve o índice para a primeira posição da lista já ordenada e o valor para a segunda posição
            indice = l[y][1]  # da lista já ordenada
            lista_ordenada.append([indice, valor])
        return lista_ordenada

        
    def define_perfil(self, indice):
        '''
        Método que recebe um índice da lista de cpfs não classificados, faz o cálculo da distância Euclidiana em relação
        a todos os cpfs já classificados e a classificação do cpf correspondente ao índice em questão, quanto a: Conservador, Moderado ou agressivo. 
        '''
        lista_distancia = [] 
        for y in range(len(self.lista_definida)): # percorre a lista já definida
            soma = 0
            distancia = 0
            for i in range(len(self.lista_definida[0][2])): #percorre a tupla de carteiras
                soma += (self.lista_indefinida[indice][2][i] - self.lista_definida[y][2][i])**2 # calcula a distância para cada 
            distancia = soma ** (1/2) # investimento entre os cpfs nas suas cateiras e armazena o resultado na lista
            lista_distancia.append([y, distancia]) # y = posição do cpf na lista
            
        lista = self.ordena_lista(lista_distancia)

        mod = 0
        agr = 0
        con = 0

        l = lista[:self.K]
        # pega um número K de menores distâncias 
        for i in range(len(l)): # percorre a lista e soma nas respectivas variáveis de acordo com o perfil do cpf
            num = l[i][0]
            if self.lista_definida[num][1] == 'Conservador':
                con += 1
            elif self.lista_definida[num][1] == 'Agressivo':
                agr += 1
            elif self.lista_definida[num][1] == 'Moderado':
                mod += 1
        l.clear()
        lista_distancia.clear()# Esvazia a lista para a próxima iteração
            # ver qual variável é maior, classifica o cpf e o adiciona no dicionário
        if con >= agr and con >= mod:
            CalculaDistancia.perfis_classificados[self.lista_indefinida[indice][0]] = 'Conservador'
                 
        elif mod >= agr and mod >= con:
            CalculaDistancia.perfis_classificados[self.lista_indefinida[indice][0]] = 'Moderado'
           
        elif agr > mod and agr > con:
            CalculaDistancia.perfis_classificados[self.lista_indefinida[indice][0]] = 'Agressivo'
            

    
