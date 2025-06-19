import tkinter as tk
from tkinter import messagebox
from ApiTemperatura import informacao_temperatura_tempo

#definindo formato da janela
janela = tk.Tk()
janela.title("consulta de temperatura ")
janela.geometry("500x400")
janela.resizable(False, False)
form_frame = tk.Frame(janela)
form_frame.pack(pady=20)

cidade_entry = tk.Entry(form_frame, width=30, font=('Arial',12))
cidade_entry.grid(row=0, column=0, padx=(0, 10))

resultado_label = tk.Label(janela, text="", font=('Helvetica', 14))
resultado_label.pack(padx=10)

consultar_btn = tk.Button(form_frame, text="Consultar",
                          font=('Arial', 11),
                          width=10,
                          command=lambda: informacao_temperatura_tempo(cidade_entry.get(), resultado_label))
consultar_btn.grid(row=0, column=1)

janela.mainloop()