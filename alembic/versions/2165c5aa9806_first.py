"""first

Revision ID: 2165c5aa9806
Revises: 
Create Date: 2024-02-18 16:58:24.515496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2165c5aa9806'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Exemplo de aplicação do alembic a partir de sua documentação
# Função para aplicar a migração
def upgrade() -> None:
    # Criando a tabela 'account'
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

# Função para reverter a migração
def downgrade() -> None:
    # Excluindo a tabela 'account'
    op.drop_table('account')