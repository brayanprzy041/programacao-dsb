import tkinter as tk
from tkinter import messagebox
import sqlite3


# =========================
# Banco de Dados
# =========================

def conectar_banco():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    return conexao


# =========================
# Função para salvar cliente
# =========================

def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validação dos campos
    if not nome or not email or not telefone:
        messagebox.showwarning(
            "Atenção",
            "Todos os campos devem ser preenchidos."
        )
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO clientes (nome, email, telefone)
            VALUES (?, ?, ?)
        """, (nome, email, telefone))

        conexao.commit()
        conexao.close()

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        limpar_formulario()

    except sqlite3.Error as erro:
        messagebox.showerror(
            "Erro",
            f"Não foi possível salvar o cliente.\nErro: {erro}"
        )


# =========================
# Função para limpar formulário
# =========================

def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# =========================
# Criar banco de dados
# =========================

conectar_banco().close()


# =========================
# Interface Gráfica
# =========================

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("450x300")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)


# Frame do formulário
frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)


# Campo Nome
label_nome = tk.Label(
    frame_formulario,
    text="Nome:",
    font=("Arial", 11)
)
label_nome.grid(row=0, column=0, padx=10, pady=8, sticky="e")

entrada_nome = tk.Entry(
    frame_formulario,
    width=35,
    font=("Arial", 11)
)
entrada_nome.grid(row=0, column=1, padx=10, pady=8)


# Campo E-mail
label_email = tk.Label(
    frame_formulario,
    text="E-mail:",
    font=("Arial", 11)
)
label_email.grid(row=1, column=0, padx=10, pady=8, sticky="e")

entrada_email = tk.Entry(
    frame_formulario,
    width=35,
    font=("Arial", 11)
)
entrada_email.grid(row=1, column=1, padx=10, pady=8)


# Campo Telefone
label_telefone = tk.Label(
    frame_formulario,
    text="Telefone:",
    font=("Arial", 11)
)
label_telefone.grid(row=2, column=0, padx=10, pady=8, sticky="e")

entrada_telefone = tk.Entry(
    frame_formulario,
    width=35,
    font=("Arial", 11)
)
entrada_telefone.grid(row=2, column=1, padx=10, pady=8)


# =========================
# Botões
# =========================

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar",
    width=12,
    command=salvar_cliente,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_salvar.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=12,
    command=limpar_formulario,
    bg="#f44336",
    fg="white",
    font=("Arial", 10, "bold")
)
botao_limpar.grid(row=0, column=1, padx=10)


# Coloca o cursor no primeiro campo
entrada_nome.focus()


# =========================
# Iniciar programa
# =========================

janela.mainloop()
