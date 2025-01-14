## 🛍️ Tech Shop
Tech Shop é um sistema desenvolvido para gerenciar produtos de tecnologia para venda, ideal para pequenas empresas ou empreendedores individuais.

## 🚀 Funcionalidades

- Cadastro de produtos de tecnologia
- Gerenciamento de estoque
- mInterface amigável para administração

## 🛠️ Tecnologias Utilizadas
- Framework: Django
- Frontend: HTML, CSS, Bootstrap
- Banco de Dados: SQLite (pode ser configurado - para PostgreSQL ou MySQL)

## Instalação

Clone o repositorio

```bash
git clone https://github.com/Taylon23/tech_shop.git
cd tech_shop

```
Crie e ative um ambiente virtual:

```bash
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  

```
Instale as dependências:

```bash
pip install -r requirements.txt
```
Aplique as migrações:
```bash
python manage.py migrate
```
Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver

```
Acesse o sistema no navegador: http://localhost:8000
