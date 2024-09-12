import hashlib
import tkinter as tk
from tkinter import filedialog

class HashApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hash Generator")

        # Layout da janela principal
        self.master.geometry('600x300')
        
        # Botão para selecionar o arquivo
        self.select_button = tk.Button(master, text="Selecionar Arquivo", command=self.select_file)
        self.select_button.pack(pady=10)

        # Label para mostrar o hash hexadecimal
        self.hash_label = tk.Label(master, text="")
        self.hash_label.pack(pady=10)

    def hash_file(self, filename):
        with open(filename, 'rb') as file:
            content = file.read()
            hash_object = hashlib.sha256()
            hash_object.update(content)
            return hash_object.hexdigest()

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            hex_dig = self.hash_file(file_path)
            self.hash_label.config(text=f"Hash: {hex_dig}")
        else:
            self.file_label.config(text="No file selected.")
            self.hash_label.config(text="")

def main():
    root = tk.Tk()
    app = HashApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
