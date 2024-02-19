from projeto.conf.connection import DBConnectionHandler
from projeto.entities.livros import Livros
from sqlalchemy.orm.exc import NoResultFound

class LivrosRepository:
    # Método para selecionar todos os livros
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                # Consultando todos os livros do banco de dados
                dados = db.session.query(Livros).all()
                return dados
            except Exception as exception:
                # Em caso de erro, realizando rollback e relançando a exceção
                db.session.rollback()
                raise exception
    
    # Método para selecionar livros do gênero 'semgenero'
    # Nesse método é propositar o retorno None, pois não há nenhum livro com o gênero 'semgenero'
    def select_genero_livros(self):
        with DBConnectionHandler() as db:
            try:
                # Consultando um livro do gênero 'semgenero' (espera-se apenas um resultado)
                dados = db.session.query(Livros).filter(Livros.genero == 'semgenero').one()
                return dados
            except NoResultFound: 
                # Se nenhum resultado for encontrado, retorna None
                return None
            except Exception as exception:
                # Em caso de erro, realizando rollback e relançando a exceção
                db.session.rollback()
                raise exception
    
    # Método para inserir um novo livro
    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                # Criando um novo objeto Livros com os dados fornecidos
                dados_insert = Livros(titulo=titulo, genero=genero, ano=ano)
                # Adicionando o novo objeto à sessão
                db.session.add(dados_insert)
                db.session.commit()
            except Exception as exception:
                # Em caso de erro, realizando rollback e relançando a exceção
                db.session.rollback()
                raise exception
    
    # Método para deletar um livro pelo título
    def delete(self, titulo):
        with DBConnectionHandler() as db:
            try:
                # Deletando o livro com o título fornecido
                db.session.query(Livros).filter(Livros.titulo == titulo).delete()
                db.session.commit()
            except Exception as exception:
                # Em caso de erro, realizando rollback e relançando a exceção
                db.session.rollback()
                raise exception
    
    # Método para atualizar o ano de publicação de um livro pelo título
    def update(self, titulo, ano):
        with DBConnectionHandler() as db:
            try:
                # Atualizando o ano de publicação do livro com o título fornecido
                db.session.query(Livros).filter(Livros.titulo == titulo).update({'ano': ano})
                db.session.commit()
            except Exception as exception:
                # Em caso de erro, realizando rollback e relançando a exceção
                db.session.rollback()
                raise exception


            
