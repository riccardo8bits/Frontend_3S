from flask import Flask, render_template, request, flash, redirect, url_for

from api_routes import routes
from database import db_session, Usuario, Funcionario
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senai_terapia_sp'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/animais')
def animais():
    return render_template("animais.html")




@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/funcionarios')
def funcionarios():
    # Busca todos os funcionários do banco
    funcionarios = Funcionario.query.all()
    return render_template("funcionarios.html", funcionarios=funcionarios)


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            flash("Preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            resultado_subtracao = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=resultado_subtracao)
        else:
            flash("Preencha o campo para realizar a subtracao", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multuplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            resultado_multiplicacao = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=resultado_multiplicacao)
        else:
            flash("Preencha o campo para realizar a multiplicacao", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/divisao', methods=['GET', 'POST'])
def divisao():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            if n2 == 0:
                flash("Não é possível dividir por zero", 'alert-danger')
                return render_template("operacoes.html")

            resultado_divisao = "{:.2f}".format(n1 / n2)
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=resultado_divisao)
        else:
            flash("Preencha o campo para realizar a divisao", 'alert-danger')
    return render_template('operacoes.html')


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/geometria/triangulo/area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            area = ((n1 * n1) * (3 ** 0.5)) / 4
            return render_template("geometria.html", area=round(area, 2))
        else:
            flash("Preencha o campo", 'alert-danger')
            return render_template("geometria.html")
    return render_template("geometria.html")


@app.route('/geometria/triangulo/perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = float(request.form['form-n1'])
            perimetro = n1 * 3
            return render_template("geometria.html", perimetro=perimetro)
    return render_template("geometria.html")


@app.route('/funcionarios/cadastrar', methods=['POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        # Pega os dados
        nome = request.form['form-nome']
        data = request.form['form-data']
        cpf = request.form['form-cpf']
        email = request.form['form-email']
        senha = generate_password_hash(request.form['form-senha'])  # <-- CRIPTOGRAFA AQUI
        cargo = request.form['form-cargo']
        salario = request.form['form-salario']

        # Cria o funcionario
        novo_func = Funcionario(
            nome=nome,
            data_nascimento=data,
            cpf=cpf,
            email=email,
            senha=senha,  # Agora vai salvar o hash
            cargo=cargo,
            salario=salario
        )

        # Salva
        db_session.add(novo_func)
        db_session.commit()

        flash(f"Funcionário {nome} cadastrado!", 'alert-success')
        return redirect(url_for('funcionarios'))





@app.route('/gatos')
def listar_gatos():
    gatos = routes.get_gatos()

    for gato in gatos:
        gato["temperament"] = gato["temperament"].split(',')
        gato["image"] = routes.get_image()["url"]



    return render_template("gatos.html", gatos=gatos)













if __name__ == '__main__':
    app.run(debug=True)