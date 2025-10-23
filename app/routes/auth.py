from argon2 import PasswordHasher
from app.models import table_users, db

ph = PasswordHasher()

def create_user(user_name, user_email, user_age, password):
    try:
        hash = ph.hash(password)
        table_users.insert(email=user_email, nome=user_name, idade=user_age, senha=hash)
        db.commit()
        return True
    except:
        return False

def login(user_email, password):
    # criar uma query para retornar a senha e caso o hash passe, buscar o id do usuario e retornar ele para o flask.
    try:
        query = (table_users.email==user_email)
        senha = db(query).select(table_users.senha).first()
        if hash:
            if ph.verify(senha['senha'], password):
                row = db(query).select(table_users.id, table_users.nome).first()
                return row
            else:
                return None
        else:
            return None
    except Exception as e:
        return None
    
def update(user_info):
    try:
        user = table_users(user_info['id'])
        for key, value in user_info.items():
            if key != 'id' and value:
                user.update_record(**{key:value})
        db.commit()
        return True
    except Exception as e:
        return False
    
def change_password(id, old_password, new_password):
    try:
        query = (table_users.id==id)
        db_password = db(query).select(table_users.senha).first()
        if ph.verify(db_password['senha'], old_password):
            hash = ph.hash(new_password)
            print(hash)
            user = table_users(id)
            user.update_record(senha=hash)
            db.commit()
            return True
        else:
            return None
    except Exception as e:
        return False


def get_all_info(id):
    try:
        query = (table_users.id==id)
        user_info = db(query).select(table_users.email, table_users.nome, table_users.idade).first()
        return user_info
    except Exception as e:
        return None
    
def delete(id):
    try:
        table_users(id).delete_record()
        db.commit()
        return True
    except:
        return False

    
if __name__ == '__main__':
    #create_user('rafael', 'rafael@live', 17, 'essa e a senha')
    #create_user('kenia', 'kenia@gmail', 20, 'aquela e a senha')
    #login('rafael@live', 'essa e a senha')
    user_info = {'id':9, 'nome':'Kera Coletto', 'email':'', 'idade':7, 'senha':''}
    