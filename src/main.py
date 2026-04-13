import json
import os

ARQUIVO = "src/alunos.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(alunos):
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)

def cadastrar_aluno():
    alunos = carregar_dados()

    cpf = input("CPF do aluno: ")

    for a in alunos:
        if a["cpf"] == cpf:
            print("Aluno já cadastrado!")
            return

    aluno = {
        "nome": input("Nome: "),
        "cpf": cpf,
        "data_matricula": input("Data matrícula: "),
        "data_nascimento": input("Data nascimento: "),
        "turma": input("Turma: "),
        "pai": {
            "nome": input("Nome do pai: "),
            "cpf": input("CPF do pai: ")
        },
        "mae": {
            "nome": input("Nome da mãe: "),
            "cpf": input("CPF da mãe: ")
        },
        "endereco": input("Endereço: "),
        "telefone": input("Telefone: ")
    }

    alunos.append(aluno)
    salvar_dados(alunos)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    alunos = carregar_dados()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for a in alunos:
        print(f"\nNome: {a['nome']}")
        print(f"CPF: {a['cpf']}")
        print(f"Turma: {a['turma']}")

def buscar_aluno():
    alunos = carregar_dados()
    cpf = input("CPF: ")

    for a in alunos:
        if a["cpf"] == cpf:
            print(a)
            return

    print("Aluno não encontrado.")

def atualizar_aluno():
    alunos = carregar_dados()
    cpf = input("CPF: ")

    for a in alunos:
        if a["cpf"] == cpf:
            a["nome"] = input("Novo nome: ")
            a["turma"] = input("Nova turma: ")
            salvar_dados(alunos)
            print("Atualizado!")
            return

    print("Aluno não encontrado.")

def remover_aluno():
    alunos = carregar_dados()
    cpf = input("CPF: ")

    novos = [a for a in alunos if a["cpf"] != cpf]
    salvar_dados(novos)
    print("Removido!")

def menu():
    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            listar_alunos()
        elif op == "3":
            buscar_aluno()
        elif op == "4":
            atualizar_aluno()
        elif op == "5":
            remover_aluno()
        elif op == "0":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()