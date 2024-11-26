CREATE VIEW TodosEmprestimos AS 
SELECT l.nome AS NomeLivro,
	   l.categoria AS Categoria,
	   l.editora AS Editora,
       c.nome AS ClienteNome,
       c.cpf AS ClienteCPF,
       f.nome AS FuncionarioNome,  -- Aqui você seleciona os campos de ambos os usuários (cliente e funcionário)
       e.dataEmprestimo AS DataEmprestimo, 
       e.dataDevolucaoPrevista AS DataDevolucaoPrevista, 
       e.dataDevolucao AS DataDevolucao
FROM Emprestimo e
JOIN Livro l ON l.id = e.fk_Livro_id
JOIN Usuario c ON c.id = e.fk_Cliente_id  -- Cliente
JOIN Usuario f ON f.id = e.fk_Funcionaro_id;  -- Funcionário

CREATE VIEW TodosEmprestimosCorrentes AS 
SELECT e.id AS id,
	   l.nome AS NomeLivro,
	   l.categoria AS Categoria,
	   l.editora AS Editora,
       c.nome AS ClienteNome,
       c.cpf AS ClienteCPF,
       f.nome AS FuncionarioNome,  -- Aqui você seleciona os campos de ambos os usuários (cliente e funcionário)
       e.dataEmprestimo AS DataEmprestimo, 
       e.dataDevolucaoPrevista AS DataDevolucaoPrevista
FROM Emprestimo e
JOIN Livro l ON l.id = e.fk_Livro_id
JOIN Usuario c ON c.id = e.fk_Cliente_id
JOIN Usuario f ON f.id = e.fk_Funcionaro_id
WHERE dataDevolucao IS NULL; 


CREATE VIEW TodosClientes AS 
SELECT u.id AS idUser,
	   u.nome AS Nome,
 	   u.cpf AS Cpf
FROM Usuario u
JOIN  Cliente c ON c.fk_Usuario_id = u.id;

CREATE VIEW TodosFuncionarios AS 
SELECT u.id AS idUser,
	   u.nome AS Nome,
 	   u.cpf AS Cpf
FROM Usuario u
JOIN  Funcionaro c ON c.fk_Usuario_id = u.id;

CREATE VIEW TodosLivros AS SELECT * FROM Livro;

CREATE VIEW LivrosEmprestados AS
SELECT l.*
FROM Emprestimo e
JOIN Livro l on l.id = e.fk_Livro_id
WHERE e.dataDevolucao IS NULL;

CREATE VIEW LivrosDisponiveis AS
SELECT tl.*
FROM TodosLivros tl 
LEFT JOIN LivrosEmprestados le 
ON tl.id = le.id
WHERE le.id IS NULL;
