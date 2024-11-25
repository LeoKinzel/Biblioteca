from abc import ABC, abstractmethod
from datetime import datetime, date, timedelta
from bibliotecaSubClasses import *
from bibliotecaViews import dbConsultas

def biblioteca():
    
    def __init__(self):
        self.db = dbConsultas("biblioteca")
        self.usuarios = []  # Lista de usuários (clientes e funcionários)
        self.livros = self.db.consultaTodosLivros()
        self.emprestimos = []  # Lista de empréstimos
        self.menu = menu()  # Instancia o menu para interações
        self.db.dbClose()

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
        for usuario in self.usuarios:
            print(f"Nome: {usuario.getNome()}, CPF: {usuario.getCpf()}")

    def consultarLivros(self):
        for livro in self.livros:
            print(f"Nome: {livro.getNome()}, Categoria: {livro.getCategoria()}, Editora: {livro.getEditora()}")
    
    def exibirMenu(self):
        opcao = None
        while opcao != 5:
            opcao = self.menu.menuPrincipal()
            if opcao == 1:
                self.exibir_menuCadastro()
            elif opcao == 2:
                self.exibir_menuConsulta()
