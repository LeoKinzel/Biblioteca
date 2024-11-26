INSERT INTO Usuario (nome, cpf, dataNascimento)
VALUES ('Leonardo Kinzel', 1810708044, '1999-06-23');
INSERT INTO Funcionaro (fk_Usuario_id)
VALUES ((SELECT id FROM Usuario WHERE nome = 'Leonardo Kinzel' AND cpf = 1810708044));


INSERT INTO Livro (nome, categoria, editora, dataLancamento)
VALUES ('teste', 'teste', 'teste', 'teste');

