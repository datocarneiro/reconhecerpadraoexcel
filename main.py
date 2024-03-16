import pandas as pd
from sklearn.linear_model import LinearRegression

# Carrega a planilha
planilha = pd.read_excel('teste.xlsx')

# Seleciona as colunas relevantes
coluna1 = planilha['Coluna1']
coluna2 = planilha['Coluna2']
coluna3 = planilha['Coluna3']
coluna4 = planilha['Coluna4']

# Cria o DataFrame combinando as colunas relevantes
dados = pd.concat([coluna1, coluna2, coluna3, coluna4], axis=1)

# Define a entrada X e a saída Y
X = dados[['Coluna1', 'Coluna2', 'Coluna3']]
Y = dados['Coluna4']

# Cria o modelo de regressão linear
modelo = LinearRegression()

# Ajusta o modelo aos dados
modelo.fit(X, Y)

# Obtém os valores mais recentes das outras colunas
valor_coluna1 = coluna1.iloc[-1]
valor_coluna2 = coluna2.iloc[-1]
valor_coluna3 = coluna3.iloc[-1]

# Preve o possível local da próxima entrada
proximo_local = modelo.predict([[valor_coluna1, valor_coluna2, valor_coluna3]])

print("Próximo local previsto:", proximo_local)