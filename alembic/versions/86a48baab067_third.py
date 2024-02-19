"""third

Revision ID: 86a48baab067
Revises: 761da42cb86e
Create Date: 2024-02-18 18:17:24.120030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from projeto.conf.connection import DBConnectionHandler
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = '86a48baab067'
down_revision: Union[str, None] = '761da42cb86e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Exemplo de aplicação usando SQL puro
# Função para aplicar a migração
def upgrade() -> None:
    # Criando uma instância de DBConnectionHandler para interagir com o banco de dados
    db_connection_handler = DBConnectionHandler()
    # Usando 'with' para garantir que a conexão seja fechada corretamente
    with db_connection_handler as db:
        # Definindo a consulta SQL para inserir um novo livro na tabela 'livros'
        query = text(
            '''
            INSERT INTO livros (titulo, genero, ano)
            VALUES ('O Pequeno Príncipe', 'Literatura Infanto-Juvenil', 1943);
            '''
        )
        # Executando a consulta SQL na sessão do banco de dados
        db.session.execute(query)
        db.session.commit()

# Função para reverter a migração
def downgrade() -> None:
    # Criando uma instância de DBConnectionHandler para interagir com o banco de dados
    db_connection_handler = DBConnectionHandler()
    # Usando 'with' para garantir que a conexão seja fechada corretamente
    with db_connection_handler as db:
        # Definindo a consulta SQL para deletar o livro 'O Pequeno Príncipe' da tabela 'livros'
        query = text(
            '''
            DELETE FROM livros
            WHERE titulo = 'O Pequeno Príncipe';
            '''
        )
        # Executando a consulta SQL na sessão do banco de dados
        db.session.execute(query)
        db.session.commit()
