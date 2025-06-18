import requests
import config

def informacao_temperatura_tempo(cidade):
    api_key = config.api_key
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_BR"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    if requisicao.status_code == 200:
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        print(descricao, f"{temperatura}ºC")
    else:
        print(f"Não foi possivel entrar a cidade: {cidade}. Erro{requisicao_dic.get('message', 'Desconhecido')}")



