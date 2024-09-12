import hashlib
import tkinter as tk
from tkinter import filedialog

def hash_file(filename):
    # Abrir o arquivo em modo de leitura binária
    with open(filename, 'rb') as file:
        # Ler o conteúdo do arquivo
        content = file.read()

        # Criar o objeto hash usando SHA-256
        hash_object = hashlib.sha256()
        hash_object.update(content)

        # Obter o hash em hexadecimal
        hex_dig = hash_object.hexdigest()
        return hex_dig

def select_file():
    # Criar uma janela raiz e escondê-la
    root = tk.Tk()
    root.withdraw()

    # Mostrar um diálogo de seleção de arquivo e obter o caminho do arquivo escolhido
    file_path = filedialog.askopenfilename()

    # Verificar se um arquivo foi selecionado
    if file_path:
        result = hash_file(file_path)
        print("Arquivo selecionado:", file_path)
        print("Hash em hexadecimal:", result)
    else:
        print("Nenhum arquivo foi selecionado.")

select_file()
