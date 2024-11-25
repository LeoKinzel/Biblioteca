from abc import ABC, abstractmethod
from datetime import datetime, date, timedelta
import sys



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
        return self.dataDevolucaoPrevista
    
    def getDataDevolucao(self):
        return self.dataDevolucao

class menu():
    
    def menuPrincipal(self):
        print("==SISTEMA BIBLIOTECA==\n")
        print("1. Cadastros")
        print("2. Consultas")
        print("3. Novo Emprestimo")
        print("4. Devolve Livro")
        print("5. Sair")
        opcao = None
        opcao = int(input("Opção Desejada: "))

        if(opcao > 5 or opcao < 1):        #RETORNA 0 CASO A OPÇÃO SELECIONADA SEJA INVALIDA
            opcao = 0
        
        if(opcao == 5):                     #ENCERRA O PROGRAMA
            sys.exit()

        return opcao                        #RETORNA A OPÇÃO

    def menuCadastro(self):
        print("==CADASTRO==\n")
        print("1. Usuario")
        print("2. Livro")
        print("3. Sair")
        opcao = None
        opcao = int(input("Opção Desejada: "))

        if(opcao > 3 or opcao < 1):        #RETORNA 0 CASO A OPÇÃO SELECIONADA SEJA INVALIDA
            opcao = 0

        if(opcao == 3):                     #ENCERRA O PROGRAMA
            sys.exit()
        
        return opcao                        #RETORNA A OPÇÃO
    
    def menuConsulta(self):
        print("==CONSULTA==\n")
        print("1. Usuarios")
        print("2. Livros")
        print("3. Emprestimos")
        print("4. Sair")
        opcao = None
        opcao = int(input("Opção Desejada: "))

        if(opcao > 4 or opcao < 1):        #RETORNA 0 CASO A OPÇÃO SELECIONADA SEJA INVALIDA
            opcao = 0

        if(opcao == 4):                     #ENCERRA O PROGRAMA
            sys.exit()
        
        return opcao                        #RETORNA A OPÇÃO
    
