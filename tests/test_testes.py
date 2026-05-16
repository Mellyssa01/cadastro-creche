from unittest.mock import patch
from src.main import carregar_dados, salvar_dados, cadastrar_aluno, buscar_endereco_por_cep

def test_cpf_invalido_funcional():
    # Atualizei as entradas pra responder às perguntas do CEP
    entradas = [
        "123",               # CPF do aluno
        "S",                 # Deseja buscar o endereço por CEP? (Sim)
        "01001000",          # CEP válido (Praça da Sé)
        "100",               # Número e Complemento
        "Aluno Teste",       # Nome
        "01/01/2024",        # Data matrícula
        "01/01/2010",        # Data nascimento
        "A",                 # Turma
        "Pai Teste",         # Nome do pai
        "111",               # CPF do pai
        "Mae Teste",         # Nome da mãe
        "222",               # CPF da mãe
        "9999"               # Telefone
    ]

    with patch("builtins.input", side_effect=entradas):
        cadastrar_aluno()

    dados = carregar_dados()

   
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




def test_busca_cep_valido_integracao():
    
    cep_teste = "01001000"  # Praça da Sé - SP
    resultado = buscar_endereco_por_cep(cep_teste)
    
    assert resultado is not None
    assert "Praça da Sé" in resultado
    assert "São Paulo" in resultado


def test_busca_cep_invalido_integracao():
    """Valida se a função lida corretamente com CEPs inexistentes na API."""
    cep_invalido = "99999999"
    resultado = buscar_endereco_por_cep(cep_invalido)
    
    assert resultado is None


