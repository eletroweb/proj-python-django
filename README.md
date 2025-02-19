## Requisitos

- Python 3 ou superior - Conferir a versão: python --version
- pip - Conferir a versão: pip --version
- Django 5 ou superior - Conferir a versão: django-admin --version
- Necessário ter o MySQL 8 ou superior - Conferir a versão: mysql --version

## Como usar Github

Cria uma pasta git dentro da pasta
'''
git init
'''
Commit registra as alterações feitas no projeto

'''
git commit -m "first commit"
'''
Verificar em qual branch está.
'''
git branch
'''
Renomear a branch atual no Git para main.
'''
git branch -M main
'''
Adicionar um repositório remoto ao repositório local
'''
git remote add origin https://github.com/eletroweb/proj-python-django.git

'''

Enviar os arquivos ao Git
'''
git push -u origin main
'''

Criar o arquivo .gitignore e não enviar os arquivos compilados
'''
git rm --cached -r admin/**pycache**/
'''

## Como rodar o projeto baixado

Instalar o conector mysql<br>
Para mudar o banco de dados padrão, exclua o arquivo db.sqlite3 e vamos instalar o mysqlclient<br>
'''
pip install mysqlclient
'''

Criar a base de dados usei o nome do banco como sendo django
'''
CREATE DATABASE django CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
'''

Criar um super usuario

'''
python manage.py createsuperuser
'''
'''
User: admin
E-mail: techmixsp@gmail.com
Password: 12345678
'''

Alterar no arquivo "settings.py" as credenciais

'''
'ENGINE': 'djando.db.backends.mysql',
'NAME': 'nome-do-banco-de-dados',
'USER': 'ususrio-do-banco-de-dados',
'PASSWORD': 'senha',
'HOST': 'localhost',
'PORT': '3306'
'''

Depois executa as Migrations

'''
python manage.py migrate
'''
'''
python manage.py makemigrations
'''

Instalar o Bootstrap
'''
pip install django-bootstrap-v5
'''

Instalar o Editor para área de descrição
'''
pip install django-tinymce
'''

Instalar a django-jet para mudar o painel administration
'''
pip install django-jet
'''

## Sequencia para criar o projeto

1. Criar o projeto Djando

Instalar o Django.
'''
pip install Django
'''

Para verificar se foi instalado

'''
django-admin --version
'''

## 2. Criar o arquivo de configuração

'''
django-admin startproject admin .
'''

## 3. Sequencia para rodar o projeto

'''
python manage.py runserver 80
'''

acessar o projeto
'''
http://127.0.0.1/
'''

Acessar a área administrativa
'''
http://127.0.0.1/admin
'''

# Criar os pacotes do projeto

alterar dentro da pasta admin, em aplicativos e adicionar o app que foi criado.
obs: o bom se algo der ruim é só excluir o app que você criou, não altera o projeto em nada.
'''
python manage.py startapp travel_packages
'''

Instalar a Biblioteca para trabalhar com o campo ImageField
'''
python -m pip install Pillow
'''

Verificar se o Pillow foi instalada
'''
python -m pip show Pillow
'''
Depois de mexer no arquivo models do app que você criou, precisa criar as tabelas, então é necessário rodar o arquivo abaixo.
'''
python manage.py makemigrations travel_packages --name travel_packages
'''
