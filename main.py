import pandas as pd
from flask import Flask, jsonify 

app = Flask (__name__)

#construir as funcionalidades
@app.route('/')
def homepage():
    return 'Homepage'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


#rodar api
app.run(host='0.0.0.0')


