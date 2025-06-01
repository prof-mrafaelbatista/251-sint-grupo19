# 251-sint-grupo19

# Dicionário Interativo de Termos Python com IA (Flask + Gemini)

Este projeto é um site desenvolvido com **Flask**, que permite ao usuário adicionar, visualizar, editar e excluir termos relacionados à linguagem **Python**. O sistema também integra uma funcionalidade de **inteligência artificial** (IA), permitindo ao usuário fazer perguntas sobre programação usando a API **Gemini**, da Google.

---

## 📌 Estrutura do Site

O site possui as seguintes seções:

- **Página Inicial (`/`)**  
  Breve introdução ao projeto.

- **Sobre (`/sobre`)**  
  Informações gerais sobre a finalidade do projeto.

- **Dicionário de Termos (`/dicionario-termos`)**  
  Área principal onde:
  - Termos podem ser **visualizados** em uma lista;
  - É possível **adicionar** novos termos e definições;
  - Termos existentes podem ser **editados**;
  - Termos podem ser **removidos** com um clique.

- **IA com Gemini (`/ia`)**  
  Um campo de texto onde o usuário pode enviar perguntas e receber respostas geradas pela API Gemini, da Google.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Framework**: [Flask](https://flask.palletsprojects.com/)
- **Front-end**: HTML, CSS (com [Bootstrap](https://getbootstrap.com/))
- **Persistência de dados**: Arquivo `.json`
- **Variáveis de ambiente**: [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Integração com IA**: [Google Generative AI (Gemini)](https://ai.google.dev/)

---

## 🤖 Integração com a API do Gemini

A integração foi feita usando a biblioteca oficial `google-generativeai`. O modelo utilizado é o `gemini-2.0-flash`.

### Passos principais:

1. Instalação da biblioteca:

   ```bash
   pip install google-generativeai
   ```

2. Carregamento da chave de API via `.env`:

   ```python
   from dotenv import load_dotenv
   load_dotenv()
   GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
   ```

3. Inicialização do modelo:

   ```python
   import google.generativeai as genai
   model = genai.GenerativeModel('gemini-2.0-flash')
   ```

4. Uso na rota `/ia`:

   ```python
   response = model.generate_content(user_input)
   ai_response = response.text
   ```

---

## 🧪 Como Executar a Aplicação Localmente

### 1. Clone o repositório:

```bash
git clone git@github.com:prof-mrafaelbatista/251-sint-grupo19.git
cd seu-repo
```

### 2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Crie o arquivo `.env`:

Crie um arquivo chamado `.env` e adicione sua chave da API Gemini:

```
GOOGLE_API_KEY=sua_chave_aqui
```

> Obtenha sua chave em: https://ai.google.dev/

### 5. Execute o aplicativo Flask:

```bash
python app.py
```

Abra no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📄 Principais Partes do Código

### `app.py`

- Contém todas as **rotas** do site:
  - `/` e `/sobre`: páginas estáticas.
  - `/dicionario-termos`: carrega os termos do dicionário.
  - `/adicionar`, `/alterar`, `/deletar`: manipulam o arquivo de dados JSON.
  - `/ia`: envia perguntas para a API do Gemini e exibe a resposta.

### `dicionario_utils.py`

- Contém funções para **carregar** e **salvar** os termos no arquivo `termos.json`.

### `templates/`

- Contém os arquivos HTML com a **interface do usuário**, estruturados com **Jinja2**.

---

## 📚 Exemplo de Termos Cadastráveis

| Termo        | Definição |
|--------------|-----------|
| Variável     | Espaço da memória onde se armazena um valor. |
| Lista        | Estrutura que armazena uma coleção ordenada de elementos. |
| Função       | Bloco de código reutilizável que executa uma tarefa. |
| Classe       | Modelo para criar objetos com atributos e comportamentos. |
| Dicionário   | Estrutura de dados que armazena pares de chave e valor. |

---

## 👨‍💻 Autor

- Victor Melquiades Leite
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=0E76A8)](https://www.linkedin.com/in/victormleite/)

---


