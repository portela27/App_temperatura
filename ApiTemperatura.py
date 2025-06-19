import requests
import config
from datetime import datetime


#buscando informaçoes na API openweathermap
def informacao_temperatura_tempo(cidade, resultado_label):
    api_key = config.api_key
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_BR"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    timestamp = requisicao_dic['dt']
    offset = requisicao_dic['timezone']
    # verificação basica para retorno do resultado
    if requisicao.status_code == 200:
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        temperatura_max = requisicao_dic['main']['temp_max'] - 273.15
        hora_cidade = datetime.fromtimestamp(timestamp + offset).strftime('%H:%M:%S')
        resultado_label.config(text=f"Na cidade de {cidade}\n, {descricao.capitalize()}\n, {temperatura:.2f}°C e máxima de {temperatura_max:.2f}°C\n horario local de {hora_cidade}")
    else:
        print(f"Não foi possivel entrar a cidade: {cidade}. Erro{requisicao_dic.get('message', 'Desconhecido')}")



