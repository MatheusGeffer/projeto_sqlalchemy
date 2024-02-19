from projeto.conf.base import Base
from sqlalchemy import Column, String, Integer

# Definindo a classe Livros, que herda da classe Base
class Livros(Base):
    # Definindo o nome da tabela no banco de dado
    __tablename__ = 'livros'

    # Definindo as colunas da tabela 'livros'
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    # Método para retornar uma representação legível de Python do objeto 
    def __repr__(self):
        return f'Livro [titulo= {self.titulo}, ano= {self.ano}]'