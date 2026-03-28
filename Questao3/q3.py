import pandas as pd

dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = pd.DataFrame.from_dict(dados_extraidos) 

# vai dar o drop e gravar as informações no dataframe
df.dropna(subset=['id_processo'], inplace=True)
df['status'] = df['status'].str.title()

# remove o R$ e qualquer espaço que possa ter
df['valor_causa'] = df['valor_causa'].str.replace('R$', "", regex=False).str.strip()

# verifica se está no formato brasileiro antes de tentar qualquer substituição de caracter
df['valor_causa'] = df['valor_causa'].where(
  ~df['valor_causa'].str.contains(','),
  df['valor_causa'].str.replace('.','').str.replace(',','.').str.replace(',','')
)

# convertendo tipo
df['valor_causa'] = df['valor_causa'].astype(float)

# mesmo não sendo solicitado, optei por tornar os estados em letras maiusculas para manter harmônico
df['estado'] = df['estado'].str.upper()

print(df)