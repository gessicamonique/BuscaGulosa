class State(object):
    def __init__(self, nome, estimativa): # criando construtor cidade, self é a propria classe
        self.nome = nome
        self.estimativa = estimativa
        self.vizinhos = []
        self.origin = None

    def add_vizinhos(self, vizinhos):
        self.vizinhos.extend(vizinhos) # extend pega cada elemento da lista parametro e coloca na lista do objeto

    def __repr__(self):
        return self.nome


def busca(initial_state, goal):
    frontier = []
    frontier.append([initial_state, 0])
    explored = set() # Criando uma coleção vazia para adicionar os explorados
    cont = 1;

    while True:
        print("Passo ", cont, ".")
        msg = "Fronteira: "
        for i in range(len(frontier)):
            if(i == len(frontier)-1): # Pegando o último índice da lista com -1, ou seja, se o tamanho for 5 - 1 = 4 adicionar sem vígula no último
                msg = msg + frontier[i][0].nome + ": " + str(frontier[i][0].estimativa)
            else:
                 msg = msg + frontier[i][0].nome + ": " + str(frontier[i][0].estimativa) + ", "
        print (msg)

        if len(frontier) == 0:
            return False

        result = choose_state(frontier) # pega da fronteira a cidade da menor euristica
        cost = result[1]
        state = result[0]
        print("Explorado: ", state, "\n") # O que eu puxei da fronteira da vez através do método choose
        
        explored.add(state) # Adicionou na coleção de estados explorados

        if state == goal: # Retorna o destino
            return state

        for vizinho in state.vizinhos: # explora todos os vizinhos 
            vizinho_state = vizinho[0]
            vizinho_cost = vizinho[1]

            if vizinho_state not in explored: # Se o estado não tiver na coleção dos explorados
                if hasState(frontier, vizinho_state): 
                    replaceCost(frontier, vizinho_state,
                                vizinho_cost+cost, state)  # o custo do vizinho da vez + os custos anteriores
                else:
                    vizinho_state.origin = state
                    frontier.append([vizinho_state, vizinho_cost])

        cont +=1

    
def replaceCost(frontier, state, cost, origin):
    replace_element = None
    
    for element in frontier:
        queue_state = element[0]

        if queue_state == state:
            replace_element = element
            break
    
    if replace_element[1] > cost:
        frontier.remove(replace_element) # Removendo o elemento com maior custo
        state.origin = origin
        frontier.append([state, cost]) # Adicionando o elemento com menor custo
    

def hasState(frontier, state): # Retorna true ou false, se o vizinho estiver na fronteira
    for element in frontier: #Elemento vai ser cada listinha da fronteira
        queue_state = element[0]

        if queue_state == state:
            return True

    return False

# Pegar o elemento com menor custo de eurística
def choose_state(frontier):
    menor = 0 #subtende-se que o índice 0 apresenta a menor estimativa custo
    for i in range(len(frontier)): # Varrendo a lista 
        if(frontier[i][0].estimativa < frontier[menor][0].estimativa): # Comparando a euristica da cidade do indice[i] com a euristica da cidade menor
            menor = i; # Se a cidade do indice i tiver  menor euristica, menor será o índice dessa cidade 
    return frontier.pop(menor) # retorna a cidade do indice menor e tira da fronteira;

def print_path(goal): # Recebendo o destino, exibe o caminho pecorrido
    state = goal
    path = []

    while state != None:
        path.append(state)
        state = state.origin

    path.reverse()
    print(path)




# Criando os objetos cidades

joao_pessoa = State("João pessoa",460)
itabaina = State("Itabaiana", 360)
santa_rita = State("Santa Rita", 451)
campina_grande = State("Campina Grande",300)
mamanguape = State("Mamanguape",380)
guarabira = State("Guarabira",340)
areia = State("Areia",316)
soledade = State("Soledade",243)
coxixola = State("Coxixola",232)
picui = State("Picui",250)
patos = State("Patos",122)
monteiro = State("Monteiro",195)
pombal = State("Pombal",55)
catole = State("Catole do Rocha",110)
itaporanga = State("Itaporanga",65)
sousa = State("Sousa",20)
cajazeiras = State("Cajazeiras",0)

# Adicionando os vizinhos

joao_pessoa.add_vizinhos([[itabaina, 68], [santa_rita, 26],
                          [campina_grande, 125]])

itabaina.add_vizinhos([[joao_pessoa, 68], [campina_grande, 65]])
santa_rita.add_vizinhos([[joao_pessoa, 26], [mamanguape, 38]])
campina_grande.add_vizinhos([[joao_pessoa, 125], [itabaina, 65],
                             [areia, 40], [soledade, 58],
                             [coxixola, 128]])

mamanguape.add_vizinhos([[santa_rita, 39], [guarabira, 42]])
guarabira.add_vizinhos([[areia, 41], [mamanguape, 42]])
areia.add_vizinhos([[campina_grande, 40], [guarabira, 41]])
soledade.add_vizinhos([[campina_grande, 58], [picui, 69], [patos, 117]])
coxixola.add_vizinhos([[campina_grande, 128], [monteiro, 83]])
picui.add_vizinhos([[soledade, 69]])
patos.add_vizinhos([[soledade, 117], [pombal, 71], [itaporanga, 108]])
monteiro.add_vizinhos([[coxixola, 83], [itaporanga, 224]])
pombal.add_vizinhos([[patos, 71], [sousa, 56], [catole, 57]])
catole.add_vizinhos([[pombal, 57]])
itaporanga.add_vizinhos([[cajazeiras, 121], [monteiro, 224], [patos,108]])
sousa.add_vizinhos([[cajazeiras, 43], [pombal, 56]])
cajazeiras.add_vizinhos([[sousa, 43], [itaporanga, 121]])

# SAÍDA!

goal = busca(joao_pessoa, cajazeiras)

# Retorna o caminho todo pecorrido
print_path(goal)

