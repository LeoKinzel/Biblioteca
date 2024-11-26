/* Mapa Lógico */

-- Tabela Livro
CREATE TABLE Livro (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    categoria VARCHAR,
    editora VARCHAR,
    dataLancamento VARCHAR
);

-- Tabela Usuario
CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    cpf INTEGER,
    dataNascimento DATE
);

-- Tabela Emprestimo
CREATE TABLE Emprestimo (
    id INTEGER PRIMARY KEY,
    fk_Cliente_id INTEGER,
    fk_Funcionaro_id INTEGER,
    fk_Livro_id INTEGER,
    dataEmprestimo DATE,
    dataDevolucaoPrevista DATE,
    dataDevolucao DATE,
    CONSTRAINT FK_Emprestimo_2 FOREIGN KEY (fk_Cliente_id)
        REFERENCES Cliente (id)
        ON DELETE CASCADE,
    CONSTRAINT FK_Emprestimo_3 FOREIGN KEY (fk_Funcionaro_id)
        REFERENCES Funcionaro (id)
        ON DELETE CASCADE,
    CONSTRAINT FK_Emprestimo_4 FOREIGN KEY (fk_Livro_id)
        REFERENCES Livro (id)
        ON DELETE CASCADE
);

-- Tabela Funcionaro
CREATE TABLE Funcionaro (
    id INTEGER PRIMARY KEY,
    fk_Usuario_id INTEGER,
    CONSTRAINT FK_Funcionaro_2 FOREIGN KEY (fk_Usuario_id)
        REFERENCES Usuario (id)
        ON DELETE CASCADE
);

-- Tabela Cliente
CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY,
    fk_Usuario_id INTEGER,
    CONSTRAINT FK_Cliente_2 FOREIGN KEY (fk_Usuario_id)
        REFERENCES Usuario (id)
        ON DELETE CASCADE
);

-- Tabela Possui (Relaciona Livro com Empréstimo)
CREATE TABLE Possui (
    fk_Livro_id INTEGER,
    fk_Emprestimo_id INTEGER,
    CONSTRAINT FK_Possui_1 FOREIGN KEY (fk_Livro_id)
        REFERENCES Livro (id)
        ON DELETE RESTRICT,
    CONSTRAINT FK_Possui_2 FOREIGN KEY (fk_Emprestimo_id)
        REFERENCES Emprestimo (id)
        ON DELETE SET NULL
);
