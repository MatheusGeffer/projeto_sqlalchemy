CREATE DATABASE IF NOT EXISTS livraria;

USE livraria;

CREATE TABLE livros(
	titulo VARCHAR(50) NOT NULL,
	genero VARCHAR(30) NOT NULL,
	ano INT NOT NULL,
	PRIMARY KEY(titulo)
);

INSERT INTO livros (titulo, genero, ano)
VALUES ('O Alquimista', 'Romance', 1988);

CREATE TABLE IF NOT EXISTS autores (
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	titulo_livro VARCHAR(50) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (titulo_livro) REFERENCES livros(titulo)
);

INSERT INTO autores (nome, titulo_livro)
VALUE ('Paulo Coelho', 'O Alquimista')