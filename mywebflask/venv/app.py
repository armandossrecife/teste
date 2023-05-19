from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Simulação de salvamento em um banco de dados
        # Você pode adicionar a lógica de persistência dos dados aqui

        return '''
            <h1>Usuário Cadastrado</h1>
            <p>Usuário: {}</p>
            <p>Nome Completo: {}</p>
            <p>Email: {}</p>
        '''.format(usuario, nome, email)
    
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)