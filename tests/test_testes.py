from src.main import carregar_dados, salvar_dados, cadastrar_aluno
from unittest.mock import patch

def test_cpf_invalido_funcional():
    entradas = [
        "123",                # CPF inválido
        "Aluno Teste",
        "01/01/2024",
        "01/01/2010",
        "A",
        "Pai Teste",
        "111",
        "Mae Teste",
        "222",
        "Rua X",
        "9999"
    ]

    with patch("builtins.input", side_effect=entradas):
        cadastrar_aluno()

    dados = carregar_dados()

    # Verifica se o CPF inválido foi cadastrado (comportamento atual do sistema)
    assert any(a["cpf"] == "123" for a in dados)
def test_salvar():
    alunos = [{"nome": "Teste", "cpf": "999"}]
    salvar_dados(alunos)

    dados = carregar_dados()
    assert dados[0]["cpf"] == "999"
    print("Teste salvar OK")

def test_lista_vazia():
    salvar_dados([])
    dados = carregar_dados()
    assert dados == []
    print("Teste lista vazia OK")

    


