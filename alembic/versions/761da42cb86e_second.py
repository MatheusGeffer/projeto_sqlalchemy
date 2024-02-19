"""second

Revision ID: 761da42cb86e
Revises: 2165c5aa9806
Create Date: 2024-02-18 17:59:38.001709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from projeto.repository.livros_repository import LivrosRepository


# revision identifiers, used by Alembic.
revision: str = '761da42cb86e'
down_revision: Union[str, None] = '2165c5aa9806'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Exemplo de aplicação usando sqlalchemy
# Função para aplicar a migração
def upgrade() -> None:
    # Criando uma instância do repositório de livros
    livros_repository = LivrosRepository()
    # Inserindo um novo livro usando o método insert do repositório
    livros_repository.insert('A Cabana', 'Ficcional', 2007)

# Função para reverter a migração
def downgrade() -> None:
    # Criando uma instância do repositório de livros
    livros_repository = LivrosRepository()
    # Deletando o livro 'A Cabana' usando o método delete do repositório
    livros_repository.delete('A Cabana')
