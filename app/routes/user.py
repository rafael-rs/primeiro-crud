from flask import Flask, render_template, session, redirect, request, url_for, flash, get_flashed_messages
from app.routes import auth
import os
import dotenv
dotenv.load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            print(f'{email}\n{senha}')
            user_info = auth.login(email, senha)
            if user_info['id'] is not None:
                session['user_id'] = user_info['id']
                session['user_name'] = user_info['nome']
                flash(f'Login realizado com sucesso')
            else:
                flash('Usuario ou senha incorretos')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Erro no processamento: {e}')
        return redirect(url_for('home'))
    
@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    flash('Logout realizado!')
    return redirect(url_for('home'))

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']
        senha = request.form['senha']
        usuario_criado = auth.create_user(nome,email,idade,senha)
        if usuario_criado:
            flash('Usuario criado!')
        else:
            flash('Usuario não pode ser criado!')
        return render_template('index.html')
    return render_template('cadastro.html')

@app.route('/update', methods=['POST', 'GET'])
def update():
    if not session.get('user_id'):
        return redirect(url_for('/home'))
    
    if request.method == 'GET':    
        user_info_db = auth.get_all_info(session.get('user_id'))
        return render_template('area_usuario.html', user=user_info_db)

    elif request.method == 'POST':      
        user_request = {'id':session.get('user_id'), 'nome':request.form['nome'], 'email':request.form['email'], 'idade':request.form['idade']} 
        updated = auth.update(user_request)
        if updated:
            flash('Informações do usuario atualizadas')
        else:
            flash('Informações não atualizadas')
        return redirect(url_for('update'))
    
    else:
        redirect(url_for('/'))

@app.route('/change_password', methods=['POST','GET'])
def change_password():
    if not session.get('user_id'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if confirm_password == new_password:
            changed = auth.change_password(session.get('user_id'),current_password,new_password)
            if changed:
                flash('Senha atualizada!')
                return redirect(url_for('update'))
            elif changed == False:
                flash('Não foi possível atualizar')
                return redirect(url_for('update'))
            elif changed == None:
                flash('Senha atual não confere')
                return redirect(url_for('update'))
        else:
            flash('Senhas não são iguais')
            return redirect(url_for('update'))
    
    if request.method == 'GET':
        return render_template('change_password.html')
    

        
    
@app.route('/delete', methods=['POST'])
def delete():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    elif request.method == 'POST':
        deleted = auth.delete(user_id)
        print(deleted)
        if deleted:
            session.clear()
            flash('Usuario deleteado!')
            return redirect(url_for('home'))
        else:
            flash('Usuario não pode ser deletado!')
            return redirect(url_for('update'))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    app.run()
