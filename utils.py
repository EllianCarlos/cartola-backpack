import pandas as pd
import requests as req
import json

def get_df_players():
    base_url = 'https://api.cartolafc.globo.com'
    mercado_path = '/atletas/mercado'
    res = req.get(base_url + mercado_path)

    df = pd.json_normalize(res.json()["atletas"])
    df = df[['atleta_id', 'slug', 'posicao_id', 'status_id', 'preco_num', 'media_num', 'jogos_num']]
    return df

