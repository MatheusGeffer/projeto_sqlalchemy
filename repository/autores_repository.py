from projeto.conf.connection import DBConnectionHandler
from projeto.entities.autores import Autores
from projeto.entities.livros import Livros


class AutoresRepository:
    # Método para selecionar todos os autores e informações sobre os livros que eles escreveram
    def select_all(self):
        with DBConnectionHandler() as db:
            # Executando uma consulta para selecionar todos os autores e informações sobre os livros
            dados = db.session\
                .query(Autores)\
                .join(Livros, Autores.titulo_livro == Livros.titulo)\
                .with_entities(
                    Autores.nome,
                    Livros.genero,
                    Livros.titulo,
                    Livros.ano
                )\
                .all()
            return dados
    
    # Método para inserir um novo autor e associá-lo a um livro pelo título
    def insert(self, nome, titulo_livro):
        with DBConnectionHandler() as db:
            try:
                # Criando um novo objeto Autores com os dados fornecidos
                dados_insert = Autores(nome=nome, titulo_livro=titulo_livro)
                # Adicionando o novo objeto à sessão
                db.session.add(dados_insert)
                db.session.commit()
            except Exception as exception:
                # Em caso de erro, realizando rollback e relançando a exceção
                db.session.rollback()
                raise exception

            