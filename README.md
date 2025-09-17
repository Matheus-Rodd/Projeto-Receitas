# 🍴 Projeto Receitas

Um sistema web desenvolvido em **Django** para cadastrar, gerenciar e visualizar receitas de forma prática e organizada.  
O projeto foi criado com foco em aprendizado e boas práticas, mas também pode ser utilizado como base para portfólios e aplicações reais.

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Django Framework**
- **HTML5, CSS3**
- **SQLite** (banco de dados padrão para desenvolvimento)
- **Bootstrap** (estilização dos templates)
- **Upload de imagens** para receitas

---

## ⚙️ Funcionalidades
- Cadastro de novas receitas
- Upload e exibição de imagens
- Listagem de receitas com detalhes
- Sistema de templates organizado
- Estrutura de projeto escalável (apps separados no Django)

---

## 🛠️ Como rodar o projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Matheus-Rodd/Projeto-Receitas.git
2️⃣ Acesse a pasta do projeto
bash
Copiar código
cd Projeto-Receitas
3️⃣ Crie e ative um ambiente virtual
bash
Copiar código
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
4️⃣ Instale as dependências
bash
Copiar código
pip install -r requirements.txt
(se o arquivo requirements.txt ainda não existir, podemos gerar com pip freeze > requirements.txt)

5️⃣ Realize as migrações
bash
Copiar código
python manage.py makemigrations
python manage.py migrate
6️⃣ Execute o servidor
bash
Copiar código
python manage.py runserver
Acesse em: http://127.0.0.1:8000/

📂 Estrutura do Projeto
lua
Copiar código
Projeto-Receitas/
│-- manage.py
│-- projeto/          # Configurações principais do Django
│-- receitas/         # App responsável pelas receitas
│-- media/            # Uploads de imagens
│-- templates/        # Templates HTML
│-- db.sqlite3        # Banco de dados local (não usar em produção)
🖼️ Screenshots
(adicione aqui prints da aplicação rodando, por exemplo tela inicial, cadastro de receitas, listagem, etc.)

🚧 Melhorias Futuras
 Sistema de login e autenticação

 Categorias de receitas

 Busca por ingredientes

 Deploy na nuvem (Heroku / Render / Railway)

👨‍💻 Autor
Matheus Rodd
📌 GitHub

Se gostou do projeto, deixe uma ⭐ no repositório!
