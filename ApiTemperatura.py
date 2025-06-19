import requests
import config
import tkinter as tk
from tkinter import messagebox

def informacao_temperatura_tempo(cidade):
    api_key = config.api_key
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_BR"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    if requisicao.status_code == 200:
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp'] - 273.15
        resultado_label.config(text=f"{descricao.capitalize()},{temperatura:.2f}ºC")
    else:
        print(f"Não foi possivel entrar a cidade: {cidade}. Erro{requisicao_dic.get('message', 'Desconhecido')}")



# interface em tkinter
root = tk.Tk()

root.title("consulta de temperatura ")
tk.Label(root, text="Digite a Cidade: ").pack

cidade_entry = tk.Entry(root)
cidade_entry.pack()

tk.Button(root, text="Consultar", command=lambda: informacao_temperatura_tempo(cidade_entry.get())).pack()

resultado_label = tk.Label(root, text="", font=('Helvetica',12))
resultado_label.pack()

root.mainloop()

