import PyPDF2 
import pandas as pd
from io import StringIO

df = pd.read_excel('ajuste_2023_1_deferidos_pos_ajuste .xlsx')

#definir o nome das colunas: 'RA' 'CÓDIGO TURMA' 'TURMA'
# Set line 0 as the header
df.columns = df.iloc[2]
# Seleciona as linhas da 2ª em diante e as 3 primeiras colunas
df = df.iloc[3:, 0:3]

# Resetar o index
df = df.reset_index(drop=True)
# Exibe o resultado
minhas_matriculas = df[:-1]
print(minhas_matriculas)
