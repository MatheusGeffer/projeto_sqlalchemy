from projeto.repository.autores_repository import AutoresRepository
from projeto.repository.livros_repository import LivrosRepository

# Instanciando o repositório de Autores para selecionar todos os autores e suas informações
consulta = AutoresRepository()
response = consulta.select_all()
print(response)

print('------')

# Instanciando o repositório de Livros para selecionar todos os livros e suas informações
consulta2 = LivrosRepository()
response2 = consulta2.select_all()
print(response2)

print('------')

# Instanciando o repositório de Livros para inserir um novo livro
inserir_livro = LivrosRepository()
response3 = inserir_livro.insert('It', 'Terror', 1986)
print(response3)

print('------')

# Instanciando o repositório de Autores para inserir um novo autor
inserir_ator = AutoresRepository()
response4 = inserir_ator.insert('Stephen King', 'It')
print(response4)

