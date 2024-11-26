from abc import ABC, abstractmethod
from datetime import datetime, date, timedelta
from bibliotecaSubClasses import *
from bibliotecaViews import dbConsultas
import os


class biblioteca():
    
    def __init__(self, banco):
        self.db = dbConsultas(banco)
        self.usuarios = [cliente(c[1], c[2]) for c in self.db.consultaTodosClientes()]
        self.livros = [livro(l[1], l[2], l[3], l[4]) for l in self.db.consultaTodosLivros()]
        self.emprestimos = [emprestimo(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[8]) for e in self.db.consultaTodosEmprestimos()]
        self.menu = menu()  # Instancia o menu para interações

    def adicionarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def realizarEmprestimo(self, funcionario, cliente, livros, dataEmprestimo):
        novoEmprestimo = emprestimo(funcionario, cliente, livros, dataEmprestimo)
        self.emprestimos.append(novoEmprestimo)
        print("Emprestimo realizado") 

    #def devolverLivro(self, emprestimo, dataDevolucao):         VERIFICAR

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
        self.db.dbClose()

