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