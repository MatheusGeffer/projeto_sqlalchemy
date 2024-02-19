from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Classe que manipula a conexão com o Banco de dados
class DBConnectionHandler:

    def __init__(self):
        # String de conexão com o banco de dados
        self.__connection_string = 'mysql+pymysql://root:senha@localhost:3306/livraria'
        # Mecanismo de banco de dados usando a string de conexão
        self.__engine = self.__create_database_engine()
        # Inicialização da sessão como None
        self.session = None

    # Criação do mecanismo de banco de dados
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    # Método para retornar uma conexão
    def get_engine(self):
        return  self.__engine.connect()
    
    # Método chamado ao entrar em um bloco
    def __enter__(self):
         # Criação de um gerador de sessão e atribuição à variável de sessão
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self
    
    # Método chamado ao sair de um bloco
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        
