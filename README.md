# Projeto Livraria

Este projeto é uma aplicação básica de exemplo para gerenciar informações sobre livros e autores em uma livraria. Ele utiliza o SQLAlchemy, que se trata de uma biblioteca de mapeamento objeto-relacional (ORM) para Python, para interagir com um banco de dados MySQL.
O intuito é práticar as diversas tecnologias existentes junto ao Python.

## Funcionalidades

- Cadastro de Livros e Autores: Permite adicionar informações sobre novos livros e autores.
- Consulta de Livros e Autores: Permite visualizar informações sobre todos os livros e autores cadastrados.
- Atualização de Informações: Permite atualizar as informações de livros e autores cadastrados, como título, gênero, ano, nome do autor, etc.
- Exclusão de Registros: Possibilita excluir livros e autores do sistema, removendo-os do banco de dados.
- Pesquisa Avançada: Oferece uma funcionalidade de pesquisa avançada que permite buscar livros e autores com base em diversos critérios, como título, gênero, autor, ano de publicação, etc.

## Tecnologias Utilizadas

- Python: Linguagem de programação utilizada para desenvolver a aplicação.
- SQLAlchemy: Biblioteca de mapeamento objeto-relacional (ORM) para Python, utilizada para interagir com o banco de dados MySQL.
- MySQL: Banco de dados relacional utilizado para armazenar os dados da livraria.
- Docker: Plataforma de conteinerização que permite executar aplicativos em contêineres isolados (no caso da aplicação foi criado um container com o MySQL.

 ## Configuração do Ambiente de Desenvolvimento

 - Clone o repositório: git clone 'https://github.com/MatheusGeffer/projeto_sqlalchemy.git'
 - Instale as dependências: 'pip install -r requirements.txt'
 - Crie e inicie o container Docker do MySQL: em seu Promp de Comando, localize o diretório do arquivo docker-compose.yml e execute o comando 'docker-compose up'
 - Execute as migrações do banco de dados: 'alembic upgrade head'
 - Execute a aplicação: python app.py, onde o arquivo já dispõem de alguns exemplos de consultar e inserções

## Estrutura do Projeto

- app.py: Arquivo principal da aplicação, contém a lógica de interação com o usuário.
- bd.sql: Arquivo que possue algumas aplicações utilizando SQL puro.
- docker-compose.yml: Arquivo que possue toda a configuração necessária para criar e iniciar um conteiner do MySQL.
- requirements.txt: Contém todas as bibliotecas utilizadas no projeto.
   - conf/: Módulo responsável pela configuração da aplicação.
   - entities/: Módulo contendo as classes de modelo de dados.
   - repository/: Módulo contendo os repositórios para interação com o banco de dados.
   - alembic/: Diretório contendo os arquivos alembic de migração do banco de dados.

## Referências e Documentações utilizadas

Documentação SQLAlchemy - https://www.sqlalchemy.org/
SQLAlchemy Engine - https://docs.sqlalchemy.org/en/14/core/engines.html
SQLAlchemy Connection Pooling - https://docs.sqlalchemy.org/en/14/core/pooling.html
Documentação SQLAlchemy Relacionamentos - https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
Alembic documentação - https://alembic.sqlalchemy.org/en/latest/tutorial.html
