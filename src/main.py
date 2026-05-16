import json
import os
import urllib.request

ARQUIVO = "src/alunos.json"


# --- NOVA FUNÇÃO NO LUGAR CORRETO E INDENTADA ---
def buscar_endereco_por_cep(cep):
    """Consome a API pública ViaCEP para buscar o endereço."""
    cep = cep.replace("-", "").replace(".", "").strip()
    if len(cep) != 8 or not cep.isdigit():
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status == 200:
                dados = json.loads(response.read().decode())
                if "erro" not in dados:
                    return f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
    except Exception:
        return None
    return None


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

    opcao_cep = input("Deseja buscar o endereço por CEP? (S/N): ").strip().upper()
    endereco_final = ""

    if opcao_cep == "S":
        cep_input = input("Digite o CEP (apenas números): ")
        endereco_api = buscar_endereco_por_cep(cep_input)

        if endereco_api:
            print(f"Endereço encontrado: {endereco_api}")
            numero = input("Número e Complemento: ")
            endereco_final = f"{endereco_api}, Nº {numero}"
        else:
            print("CEP não encontrado ou erro na API. Digite manualmente.")
            endereco_final = input("Endereço completo: ")
    else:
        endereco_final = input("Endereço: ")

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
        "endereco": endereco_final,
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