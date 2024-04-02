import tkinter as tk
from tkinter import ttk

# Variáveis globais para as entradas de valores
entry_peso, entry_altura, entry_a, entry_b, entry_c, entry_principal, entry_taxa, entry_tempo = None, None, None, None, None, None, None, None
entry_valor_moeda, entry_taxa_conversao, entry_valores = None, None, None

# Funções para cálculos
def calcular_imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura ** 2)
    label_resultado["text"] = f"Seu IMC é: {imc:.2f}"

def resolver_equacao():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    delta = (b ** 2) - (4 * a * c)
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    label_resultado["text"] = f"As raízes da equação são: {x1} e {x2}"

def calcular_juros():
    principal = float(entry_principal.get())
    taxa = float(entry_taxa.get())
    tempo = float(entry_tempo.get())

    juros_simples = principal * taxa * tempo
    juros_compostos = principal * (1 + taxa) ** tempo - principal

    label_resultado["text"] = f"Juros simples: {juros_simples}\nJuros compostos: {juros_compostos}"

def converter_moeda():
    valor = float(entry_valor_moeda.get())
    taxa = float(entry_taxa_conversao.get())
    resultado = valor * taxa

    label_resultado["text"] = f"Valor convertido: {resultado}"

# Criar janela
root = tk.Tk()
root.title("Calculadora Grind")

# Frame para escolha de cálculos
frame_calculos = ttk.LabelFrame(root, text="Escolha o cálculo:")
frame_calculos.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Opções de cálculos
calculos = ["IMC", "Equação de segundo grau (Bhaskara)", "Juros", "Conversão de moeda"]
combo_calculos = ttk.Combobox(frame_calculos, values=calculos)
combo_calculos.grid(row=0, column=0, padx=5, pady=5)

# Frame para inserção de valores
frame_inputs = ttk.LabelFrame(root, text="Insira os valores:")
frame_inputs.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Função para mostrar apenas as entradas necessárias conforme a escolha do usuário
def mostrar_entradas(event):
    global entry_peso, entry_altura, entry_a, entry_b, entry_c, entry_principal, entry_taxa, entry_tempo, entry_valor_moeda, entry_taxa_conversao, entry_valores
    escolha = combo_calculos.get()
    for widget in frame_inputs.winfo_children():
        widget.destroy()  # Destruir todos os widgets dentro do frame

    if escolha == "IMC":
        frame_inputs.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        label_peso = ttk.Label(frame_inputs, text="Peso (kg):")
        label_peso.grid(row=0, column=0, padx=5, pady=5)
        entry_peso = ttk.Entry(frame_inputs)
        entry_peso.grid(row=0, column=1, padx=5, pady=5)
        label_altura = ttk.Label(frame_inputs, text="Altura (m):")
        label_altura.grid(row=1, column=0, padx=5, pady=5)
        entry_altura = ttk.Entry(frame_inputs)
        entry_altura.grid(row=1, column=1, padx=5, pady=5)
    elif escolha == "Equação de segundo grau (Bhaskara)":
        frame_inputs.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        label_a = ttk.Label(frame_inputs, text="Coeficiente 'a':")
        label_a.grid(row=0, column=0, padx=5, pady=5)
        entry_a = ttk.Entry(frame_inputs)
        entry_a.grid(row=0, column=1, padx=5, pady=5)
        label_b = ttk.Label(frame_inputs, text="Coeficiente 'b':")
        label_b.grid(row=1, column=0, padx=5, pady=5)
        entry_b = ttk.Entry(frame_inputs)
        entry_b.grid(row=1, column=1, padx=5, pady=5)
        label_c = ttk.Label(frame_inputs, text="Coeficiente 'c':")
        label_c.grid(row=2, column=0, padx=5, pady=5)
        entry_c = ttk.Entry(frame_inputs)
        entry_c.grid(row=2, column=1, padx=5, pady=5)
    elif escolha == "Juros":
        frame_inputs.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        label_principal = ttk.Label(frame_inputs, text="Principal:")
        label_principal.grid(row=0, column=0, padx=5, pady=5)
        entry_principal = ttk.Entry(frame_inputs)
        entry_principal.grid(row=0, column=1, padx=5, pady=5)
        label_taxa = ttk.Label(frame_inputs, text="Taxa de juros (%):")
        label_taxa.grid(row=1, column=0, padx=5, pady=5)
        entry_taxa = ttk.Entry(frame_inputs)
        entry_taxa.grid(row=1, column=1, padx=5, pady=5)
        label_tempo = ttk.Label(frame_inputs, text="Tempo (anos):")
        label_tempo.grid(row=2, column=0, padx=5, pady=5)
        entry_tempo = ttk.Entry(frame_inputs)
        entry_tempo.grid(row=2, column=1, padx=5, pady=5)
    elif escolha == "Conversão de moeda":
        frame_inputs.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        label_valor_moeda = ttk.Label(frame_inputs, text="Valor a ser convertido:")
        label_valor_moeda.grid(row=0, column=0, padx=5, pady=5)
        entry_valor_moeda = ttk.Entry(frame_inputs)
        entry_valor_moeda.grid(row=0, column=1, padx=5, pady=5)
        label_taxa_conversao = ttk.Label(frame_inputs, text="Taxa de conversão:")
        label_taxa_conversao.grid(row=1, column=0, padx=5, pady=5)
        entry_taxa_conversao = ttk.Entry(frame_inputs)
        entry_taxa_conversao.grid(row=1, column=1, padx=5, pady=5)

# Atribuir a função mostrar_entradas para o evento de mudança na escolha
combo_calculos.bind("<<ComboboxSelected>>", mostrar_entradas)

# Atribuir a função de cálculo correspondente com base na escolha do usuário
def calcular():
    opcao = combo_calculos.get()
    if opcao == "IMC":
        calcular_imc()
    elif opcao == "Equação de segundo grau (Bhaskara)":
        resolver_equacao()
    elif opcao == "Juros":
        calcular_juros()
    elif opcao == "Conversão de moeda":
        converter_moeda()

# Botão para calcular
btn_calcular = ttk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=2, column=0, padx=10, pady=10)

# Label para mostrar resultado
label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()