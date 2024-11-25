from abc import ABC, abstractmethod
from datetime import datetime, date, timedelta
from bibliotecaSubClasses import *

def biblioteca():
    
    def __init__(self):
        self.usuarios = []  # Lista de usuários (clientes e funcionários)
        self.livros = []    # Lista de livros
        self.emprestimos = []  # Lista de empréstimos
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

    def listaUsuarios(self):
        for usuario in self.usuarios:
            print(f"Nome: {usuario.getNome()}, CPF: {usuario.getCpf()}")

    def consultar_livros(self):
        for livro in self.livros:
            print(f"Nome: {livro.getNome()}, Categoria: {livro.getCategoria()}, Editora: {livro.getEditora()}")
    
    def exibir_menu(self):
        opcao = None
        while opcao != 5:
            opcao = self.menu.menuPrincipal()
            if opcao == 1:
                self.exibir_menuCadastro()
            elif opcao == 2:
                self.exibir_menuConsulta()
