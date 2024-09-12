# Transforme Arquivos de Texto em Hash e Ler Hexadecimal

Este projeto é um utilitário Python simples que permite que o usuário selecione um arquivo de texto e gere um hash SHA-256 em formato hexadecimal a partir do conteúdo do arquivo. Ele também oferece uma interface gráfica (GUI) interativa para facilitar a seleção de arquivos e a exibição do resultado.

## Funcionalidades

- Interface gráfica para seleção de arquivos usando `tkinter`.
- Geração de hash SHA-256 a partir de arquivos de texto.
- Exibição do hash gerado em formato hexadecimal na interface gráfica.

## Requisitos

- Python 3.6 ou superior
- `tkinter` (incluído na instalação padrão do Python)
- Bibliotecas externas listadas em `requirements.txt`

## Passo a Passo para Executar o Projeto

### 1. Clonar o Repositório

Clone este repositório em seu ambiente local.

```bash
git clone https://github.com/LeiteBayer/atividade-hash.git
cd atividade-hash
```

### 2. Criar um Ambiente Virtual

Recomenda-se o uso de um ambiente virtual (venv) para isolar as dependências do projeto. Para criar um ambiente virtual, execute o seguinte comando:

#### No Windows:
```bash
python -m venv venv
```

#### No Linux/macOS:
```bash
python3 -m venv venv
```

### 3. Ativar o Ambiente Virtual

Após criar o ambiente virtual, é necessário ativá-lo.

#### No Windows:
```bash
.\venv\Scripts\activate
```

#### No Linux/macOS:
```bash
source venv/bin/activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Executar o Script

Agora que tudo está configurado, você pode executar o script principal para abrir a interface gráfica e selecionar um arquivo para gerar o hash.

```bash
python file_hash_generator_console.py
```

```bash
python file_hash_generator_interface.py
```

### 6. Desativar o Ambiente Virtual

Após terminar de trabalhar no projeto, você pode desativar o ambiente virtual com o seguinte comando:

```bash
deactivate
```

### Estrutura do Projeto

```plaintext
.
├── venv/                                # Ambiente virtual (não precisa ser commitado no Git)
├── file_hash_generator_console.py       # Script principal que contém a lógica do programa executanda no console
├── file_hash_generator_interface.py     # Script principal que contém a lógica do programa executando interface grafica
├── requirements.txt                     # Lista de dependências do projeto
└── README.md                            # Instruções do projeto
```

### Detalhes do Script

O script `script.py` contém as seguintes funcionalidades principais:

1. **Geração de Hash SHA-256**: O conteúdo de um arquivo de texto selecionado pelo usuário é lido e convertido em um hash SHA-256.
2. **Interface Gráfica**: O usuário pode selecionar o arquivo via uma janela gráfica (`tkinter`), e o hash gerado é exibido na mesma interface.
3. **Manutenção de Simplicidade**: O foco é facilitar o processo de cálculo de hash de um arquivo sem precisar usar o terminal diretamente, oferecendo uma interface amigável.

### Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Atualmente, o projeto utiliza as seguintes bibliotecas:

- `numpy==1.21.2`
- `requests==2.25.1`

Além disso, a biblioteca padrão `tkinter` é usada para a interface gráfica e `hashlib` para geração do hash, ambos incluídos por padrão no Python.

### Como Atualizar as Dependências

Caso seja necessário atualizar ou adicionar dependências ao projeto, você pode usar o comando:

```bash
pip freeze > requirements.txt
```

Isso irá atualizar o arquivo `requirements.txt` com todas as dependências instaladas no ambiente virtual.

## Autor

Projeto desenvolvido por **Leite Bayer**.
