import sqlite3

class dbConsultas():
    
    def __init__(self, banco):
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()
    
    def dbClose(self):
        self.cursor.close()
        self.conexao.close()

    def consultaLivrosDisponiveis(self):
        query = "SELECT * FROM LivrosDisponiveis"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def consultaLivrosEmprestados(self):
        query = "SELECT * FROM LivrosEmprestados"
        self.cursor.execute(query)
        return self.cursor.fetchall()
   
    def consultaTodosLivros(self):
        query = "SELECT * FROM TodosLivros"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def consultaTodosClientes(self):
        query = "SELECT * FROM TodosClientes"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def consultaTodosFuncionarios(self):
        query = "SELECT * FROM TodosFuncionarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def consultaTodosEmprestimos(self):
        query = "SELECT * FROM TodosEmprestimos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def consultaTodosEmprestimosCorrentes(self):
        query = "SELECT * FROM TodosEmprestimosCorrentes"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def adicionarUsuario(self, nome, cpf, dataNascimento):
        query = """
            INSERT INTO Usuario (nome, cpf, dataNascimento)
            VALUES (?, ?, ?)
            RETURNING id;
        """
        self.cursor.execute(query, (nome, int(cpf), dataNascimento))
        userId = self.cursor.fetchone()[0]
        query = """
            INSERT INTO Cliente (fk_Usuario_id)
            VALUES (?);
        """
        self.cursor.execute(query, (int(userId),))
        self.conexao.commit()

    def adicionarLivro(self, nome, categoria, editora, dataLancamento):
        query = """
            INSERT INTO Livro (nome, categoria, editora, dataLancamento)
            VALUES (?, ?, ?, ?);
        """
        self.cursor.execute(query, (nome, categoria, editora, dataLancamento))
        self.conexao.commit()

    def adicionarEmprestimo(self, idCliente, idFuncionario, idLivro, dataEmprestimo, dataDevolucaoPrevista):
        query = """
            INSERT INTO Emprestimo (fk_Cliente_id, fk_Funcionaro_id, fk_Livro_id, dataEmprestimo, dataDevolucaoPrevista, dataDevolucao)
            VALUES (?, ?, ?, ?, ?, NULL);
        """
        self.cursor.execute(query, (idCliente, idFuncionario, idLivro, dataEmprestimo, dataDevolucaoPrevista))
        self.conexao.commit()

    def devolverLivro(self, idEmprestimo, dataDevolucao):
        query = """
            UPDATE Emprestimo
            SET dataDevolucao = ?
            WHERE id = ?;
        """
        self.cursor.execute(query, (dataDevolucao, idEmprestimo))
        self.conexao.commit()