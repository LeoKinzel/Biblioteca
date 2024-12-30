from abc import ABC, abstractmethod
from datetime import datetime, date, timedelta
from bibliotecaSubClasses import *
from bibliotecaDb import dbConsultas
import os


class biblioteca():
    
    def __init__(self, banco):
        self.db = dbConsultas(banco)
        self.usuarios = [cliente(c[1], c[2]) for c in self.db.consultaTodosClientes()]
        self.livros = [livro(l[1], l[2], l[3], l[4]) for l in self.db.consultaTodosLivros()]
        self.emprestimos = [emprestimo(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[8]) for e in self.db.consultaTodosEmprestimos()]
        self.menu = menu()  # Instancia o menu para interações

    def atualizarDados(self):
        self.usuarios = [cliente(c[1], c[2]) for c in self.db.consultaTodosClientes()]
        self.livros = [livro(l[1], l[2], l[3], l[4]) for l in self.db.consultaTodosLivros()]
        self.emprestimos = [emprestimo(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[8]) for e in self.db.consultaTodosEmprestimos()]

    def adicionarUsuarios(self):
        nome = input("Nome: ")
        cpf = input("Cpf: ")
        data = input("Data de Nascimento: ")
        self.db.adicionarUsuario(nome, cpf, data)
        self.atualizarDados()
        print("\nUsuario Adicionado!")

    def adicionarLivro(self):
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        editora = input("Editora: ")
        dataLancamento = input("DataLancamento: ")
        self.db.adicionarLivro(nome, categoria, editora, dataLancamento)
        self.atualizarDados()
        print("\nLivro Adicionado!")

    def novoEmprestimo(self):

        print('\n')
        print("==Livros Disponiveis==\n")
        print(self.db.consultaLivrosDisponiveis())

        if not self.db.consultaLivrosDisponiveis():
            print("\n Sem livros Disponiveis para Locação!")
            input()
            return
        
        print('\n')
        print("==Clientes Cadastrados==\n")
        print(self.db.consultaTodosClientes())

        print('\n')
        print("==Funcionarios==\n")
        print(self.db.consultaTodosFuncionarios())
        print('\n')

        idLivro = input("Selecione o Id do Livro a ser locado: ")
        idCliente = input("Selecione o Id do Cliente: ")
        idFuncionario = input("Selecione o Id do Funcionario: ")
        dataEmprestimo = input("Data do Emprestimo: ")
        dataDevolucaoPrevista = str(datetime.strptime(dataEmprestimo, "%Y-%m-%d") + timedelta(days=15))[0:10]
        self.db.adicionarEmprestimo(idCliente, idFuncionario, idLivro, dataEmprestimo, dataDevolucaoPrevista)
        self.atualizarDados()

        print("\nEmprestimo Realizado!")

    def devolverLivro(self,):
        print("==Emprestimo Correntes==\n")
        print(self.db.consultaTodosEmprestimosCorrentes())
        print('\n')

        idEmprestimo = input("Selecione o Id do Livro a ser devolvido: ")
        dataDevolucao = input("Data de Devolução: ")
        self.db.devolverLivro(idEmprestimo, dataDevolucao)
        self.atualizarDados()

        print("\nEmprestimo Finalizado")

    def listarUsuarios(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("\n----Usuario----\n")
        for usuario in self.usuarios:
            print(f"Nome: {usuario.getNome()}, CPF: {usuario.getCpf()}")
        print('\n')

    def consultarLivros(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("\n----Livros----\n")
        for livro in self.livros:
            print(f"Livro: {livro.getNome()}, Categoria: {livro.getCategoria()}, Editora: {livro.getEditora()}")
        print('\n')

    def consultarEmprestimos(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("\n----Emprestimos----\n")
        for emprestimo in self.emprestimos:
            print(f"Livro: {emprestimo.getNomeLivro()}, Categoria: {emprestimo.getCategoriaLivro()}, Editora: {emprestimo.getEditoraLivro()}")
            print(f"Cliente: {emprestimo.getClienteNome()}, CPF: {emprestimo.getClienteCpf()}")
            print(f"Funcionário responsável: {emprestimo.getFuncionarioNome()}")
            print(f"Data do empréstimo: {emprestimo.getDataEmprestimo()}")
            print(f"Data de devolução prevista: {emprestimo.getDataDevolucaoPrevista()}")
        print('\n')

    
    def exibirMenu(self):
        opcao = None
        while opcao != 5:
            os.system('cls')
            opcao = self.menu.menuPrincipal()
            if opcao == 1:
                os.system('cls')
                opcao = self.menu.menuCadastro()
                while opcao !=4:
                    if opcao == 1:
                        os.system('cls')
                        self.adicionarUsuarios()
                        opcao = 0
                        break
                    elif opcao == 2:
                        os.system('cls')
                        self.adicionarLivro()
                        opcao = 0
                        break
                    elif opcao == 3:
                        os.system('cls')
                        opcao = 5
                        break
            elif opcao == 2:
                os.system('cls')
                opcao = self.menu.menuConsulta()
                while opcao !=4:
                    if opcao == 1:
                        os.system('cls')
                        self.listarUsuarios()
                        input()
                        opcao = 0
                        break
                    elif opcao == 2:
                        os.system('cls')
                        self.consultarLivros()
                        input()
                        opcao = 0
                        break
                    elif opcao == 3:
                        os.system('cls')
                        self.consultarEmprestimos()
                        input()
                        opcao = 0
                        break
            elif opcao == 3:
                os.system('cls')
                self.novoEmprestimo()
                input()
                opcao = 0
            elif opcao == 4:
                os.system('cls')
                self.devolverLivro()
                input()
                opcao = 0
        self.db.dbClose()

