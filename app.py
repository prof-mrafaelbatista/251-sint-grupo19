from flask import Flask, render_template, request, redirect, url_for
from dicionario_utils import carregar_termos, salvar_termos
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("A variável de ambiente GOOGLE_API_KEY não está definida. "
                     "Certifique-se de ter um arquivo .env na raiz do projeto com GOOGLE_API_KEY=SUA_CHAVE_AQUI.")

model = genai.GenerativeModel('gemini-2.0-flash')

app = Flask(__name__)

# ======== ROTAS DE PÁGINAS ========

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/dicionario-termos')
def dicionario():
    termos = carregar_termos()
    return render_template('dicionario-termos.html', termos=termos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    termo = request.form.get('termo').strip()
    definicao = request.form.get('definicao').strip()

    if termo and definicao:
        termos = carregar_termos()
        termos[termo] = definicao
        salvar_termos(termos)

    return redirect(url_for('dicionario'))

@app.route('/alterar', methods=['POST'])
def alterar():
    termo = request.form.get('termo')
    nova_definicao = request.form.get('definicao').strip()
    termos = carregar_termos()
    if termo in termos and nova_definicao:
        termos[termo] = nova_definicao
        salvar_termos(termos)
    return redirect(url_for('dicionario'))

@app.route('/deletar', methods=['POST'])
def deletar():
    termo = request.form.get('termo')
    termos = carregar_termos()
    if termo in termos:
        del termos[termo]
        salvar_termos(termos)
    return redirect(url_for('dicionario'))


# ======== ROTA DO GEMINI (IA) ========

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    ai_response = None
    error = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['user_input']
        try:
            response = model.generate_content(user_input)
            ai_response = response.text
        except Exception as e:
            error = f"Erro ao obter resposta do Gemini: {e}"

    return render_template('ia.html',
                           ai_response=ai_response,
                           user_input=user_input,
                           error=error)


# ======== INICIAR APP ========
if __name__ == '__main__':
    app.run(debug=True)
