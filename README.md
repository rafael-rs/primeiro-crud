# 🧭 Sistema de Login com Flask

Este projeto foi desenvolvido com fins **educacionais**, com o objetivo de estudar e praticar o uso do **Flask** para criação de sistemas de autenticação e gerenciamento de usuários, aplicando boas práticas de segurança e integração com frontends modernos.

O sistema implementa as principais operações de um **CRUD** (Create, Read, Update, Delete) com autenticação segura, além de uma interface frontend estilizada com **Mobirise**.

---

## 🚀 Funcionalidades

- **Cadastro de usuário** com validação de dados  
- **Login e logout** com controle de sessão  
- **Atualização de perfil e senha** (somente usuários autenticados, ainda não utiliza tokens para recuperar a senha)  
- **Exclusão de conta** com verificação de autenticação  
- **Proteção de rotas** baseada em sessão  
- **Layout moderno** desenvolvido no **Mobirise**, adaptado para uso com **Flask e Jinja2**

---

## 🧩 Tecnologias utilizadas

### 🔹 Backend
- Python 3.13
- Flask 3.1.2
- PyDAL — ORM simples e robusto
- PyMySQL — driver de conexão MySQL
- argon2-cffi — hashing seguro de senhas
- python-dotenv — gerenciamento de variáveis de ambiente

### 🔹 Frontend (Não possuia muito foco no frontend)
- Mobirise Website Builder — estrutura HTML e CSS inicial  
- Bootstrap 5 — componentes e responsividade  
- Jinja2 — engine de templates utilizada pelo Flask  

---

## ⚙️ Estrutura do projeto (simplificada)

```
project/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   └── assets/           # CSS, JS e imagens do Mobirise
│
├── templates/
│   ├── base.html         # Template principal (com navbar)
│   ├── index.html        # Página inicial
│   ├── cadastro.html     # Formulário de registro
│   ├── login.html        # Tela de login
│   ├── change_password.html
│   └── update.html       # Atualização de dados
│
└── database/
    └── users.db          # Banco de dados local (MySQL)
```

---

## 🔐 Segurança

- Senhas armazenadas com **Argon2** (biblioteca `argon2-cffi`)
- Sessões protegidas por `Flask.secret_key`
- Rotas sensíveis acessíveis apenas se `session['user_id']` estiver ativa

---

## Variáveis de Ambiente

Para rodar o projeto localmente, crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

DB_ROOT_PASSWORD
VOLUME_HOST
DATABASE_URL
SECRET_KEY

---

## 🎨 Créditos

- **Frontend:** adaptado de modelos gerados pelo [Mobirise](https://mobirise.com/)  
- **Backend:** desenvolvido em Flask com integração ao banco via PyDAL  
- **Autor:** Rafael *(projeto pessoal de aprendizado e prática de CRUD + autenticação)*

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e experimentais.  
Sinta-se à vontade para estudar, modificar e expandir.

---

## Observações

Este README foi gerado com o auxílio de Inteligência Artificial para organizar a documentação do projeto de forma clara e objetiva.

