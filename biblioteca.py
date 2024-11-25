from abc import ABC, abstractmethod
from datetime import datetime, date, timedelta


class usuario(ABC):

    def __init__(self, nome, cpf, dataNascimento):
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    @abstractmethod
    def getNome(self):
        pass

    @abstractmethod
    def getCpf(self):
        pass

    @abstractmethod
    def getDataNascimento(self):
        pass

class cliente(usuario):
    
    def __init__(self, nome, cpf, dataNascimento):
        super().__init__(nome, cpf, dataNascimento)

    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf

    def getDataNascimento(self):
        return self.dataNascimento
    
class funcionario(usuario):
    
    def __init__(self, nome, cpf, dataNascimento):
        super().__init__(nome, cpf, dataNascimento)

    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf

    def getDataNascimento(self):
        return self.dataNascimento
    
class livro():

    def __init__(self, nome, categoria, editora, dataLancamento):
        self.nome = nome
        self.categoria = categoria
        self.editora = editora
        self.dataLancamento =  dataLancamento
    
    def getNome(self):
        return self.nome

    def getCategoria(self):
        return self.categoria

    def getEditora(self):
        return self.editora
    
    def getDataLancamento(self):
        return self.dataLancamento
    
class emprestimo():

    def __init__(self, funcionario, cliente, livros, dataEmprestimo, dataDevolucao=None):
        self.funcionario = funcionario
        self.cliente = cliente
        self.livros = livros
        self.dataEmprestimo = dataEmprestimo
        self.dataDevolucaoPrevista = dataEmprestimo + timedelta(days=15)
    
    def getFuncionario(self):
        return self.funcionario

    def getCliente(self):
        return self.cliente

    def getLivros(self):
        return self.livros
    
    def getDataEmprestimo(self):
        return self.dataEmprestimo
    
    def getDataDevolucaoPrevista(self):
        return self.getDataDevolucaoPrevista
    
    def getDataDevolucao(self):
        return self.getDataDevolucao

