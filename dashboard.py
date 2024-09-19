# pip install dash
# pip install pandas
# pip install openpyxl

# Estrutura
# Layout -> Tudo que vai ser visualizado
# Callbacks -> Funcionalidades que você terá do dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel('dados_posts_remama.xlsx')

fig = px.bar(df, x="Tipo de post", y="Curtidas", color="Tipo de post", barmode="group")

opcoes = list(df['Tipo de post'].unique())

opcoes.append('Todos os tipos')

app.layout = html.Div(children=[
    html.H1(children='Quantidade de curtidas reels e posts remamadragaorosa'),
    html.H2(children='Gráfico com dados de curtidas dos reels e posts do remama'),
    dcc.Dropdown(opcoes, value='Todos os tipos', id='lista_tipos'),
    
    dcc.Graph(
        id='grafico_quantidade_curtidas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_curtidas', 'figure'),
    Input('lista_tipos', 'value')
)

def update_output(value):
    if value == 'Todas os tipos':
        fig = px.bar(df, x='Produto', y='Quantidade', color='ID Loja', barmode='group')
    else:
        tabela_filtrada = df.loc[df['Tipo de post'] == value, :]
        fig = px.bar(tabela_filtrada, x='Tipo de post', y='Curtidas', color='Tipo de post', barmode='group')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)