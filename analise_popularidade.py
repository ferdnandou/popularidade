import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def carregar_dados(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    print(df.columns)  # Verifique os nomes das colunas
    # Supondo que a coluna de datas se chama 'date'
    df['Week'] = pd.to_datetime(df['Week'])
    df.set_index('Week', inplace=True)
    return df

def aplicar_media_movel(df):
    df['Python_Media_Movel_Curto'] = df['Python'].rolling(window=4).mean()
    df['Python_Media_Movel_Longo'] = df['Python'].rolling(window=26).mean()
    return df

def plotar_graficos(df):
    # Gráfico da evolução da popularidade
    fig = px.line(df, x=df.index, y=['Python', 'Java', 'C++'], title='Popularidade das Linguagens de Programação')
    fig.show()
    
    # Gráfico da média móvel
    fig = px.line(df, x=df.index, y=['Python', 'Python_Media_Movel_Curto', 'Python_Media_Movel_Longo'],
                  title='Popularidade do Python e Médias Móveis')
    fig.show()

def analisar_popularidade(caminho_arquivo):
    df = carregar_dados(caminho_arquivo)
    df = aplicar_media_movel(df)
    plotar_graficos(df)

if __name__ == "__main__":
    caminho_arquivo = 'trend_over_time.csv'  # Atualize conforme necessário
    analisar_popularidade(caminho_arquivo)
