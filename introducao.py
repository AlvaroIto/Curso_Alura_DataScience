import pandas as pd
import matplotlib.pyplot
import seaborn as sns

notas = pd.read_csv('ratings.csv')

#mostrar tabela
print(notas)

#mudar nomes das colunas
nome_colunas = notas.columns = ['usuarioID', 'filmeID', 'nota', 'momento']

#mostrar top5
#top5 = notas.head()
#print(top5)

#mostrar as notas possíveis
#valor_notas = notas['nota'].unique()
#print(valor_notas)

#mostrar contagem de notas
#contagem_notas = notas['nota'].value_counts()
#print(contagem_notas)

#mostrar gráficamente
#fig, simple_chart = matplotlib.pyplot.subplots()
#simple_chart.plot(notas)
#matplotlib.pyplot.show()

#mostrar alguns dados
#dados = notas.nota.describe()
#print(dados)

print(sns.boxplot(notas.nota))
