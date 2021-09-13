from utils import get_df_players
import gurobipy as gp
from gurobipy import GRB

df = get_df_players()

N = len(df)

cost = df['preco_num']
cartoletas = 125
medias = df['media_num']
jogos = df['jogos_num']
posicoes = df['posicao_id']
status = df['status_id']

m = gp.Model("Mochila")
x = m.addVars(N, vtype=GRB.BINARY)

m.setObjective(sum(medias[i]*x[i] for i in range(N)), GRB.MAXIMIZE)

m.addConstr(sum(jogos[i]*x[i] for i in range(N)) >= 7) # Deve ter jogado mais de 7 jogos 
m.addConstr(sum(cost[i]*x[i] for i in range(N)) <= cartoletas) # Custo não pode ser maior que o número de cartoletas
m.addConstr(sum(1*x[i] for i in range(N)) <= 12) # Apenas 11 Jogadores
m.addConstr(sum((posicoes[i] == 1)*1*x[i] for i in range(N)) == 1) # Apenas 1 Goleiro
m.addConstr(sum((posicoes[i] == 2)*1*x[i] for i in range(N)) == 2) # Apenas 2 Laterais
m.addConstr(sum((posicoes[i] == 3)*1*x[i] for i in range(N)) == 2) # Apenas 2 Zagueiros
m.addConstr(sum((posicoes[i] == 4)*1*x[i] for i in range(N)) == 3) # Apenar 3 Meias
m.addConstr(sum((posicoes[i] == 5)*1*x[i] for i in range(N)) == 3) # Apenas 3 Atacantes
m.addConstr(sum((posicoes[i] == 6)*1*x[i] for i in range(N)) == 1) # Apenas 1 Tecnico
m.addConstr(sum((status[i] == 7)*1*x[i] for i in range(N)) == 12) # Apenas atletas prováveis
m.optimize()

print("\nValor da solução ótima:\t"+str(m.objVal))
print("Carga ocupada:\t"+str(sum(cost[i]*x[i].X for i in range(N))))
for i in range(N):
    if (x[i].X != 0):
        print("Item "+str(i+1)+": "+str(x[i].X) + " - Nome: " + df.iloc[i]['slug'])

