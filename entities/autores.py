from projeto.conf.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

# Definindo a classe Autores, que herda da classe Base
class Autores(Base):
    # Definindo o nome da tabela no banco de dados
    __tablename__ = 'autores'

    # Definindo as colunas da tabela 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_livro= Column(String, ForeignKey('livros.titulo'))

    # Método para retornar uma representação legível de Python do objeto 
    def __repr__(self):
        return f'Autores [nome= {self.nome}, filme= {self.titulo_livro}]'