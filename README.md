*Nome do projeto
Cadastro de Alunos

#Descrição
Sistema simples em python para registrar, consultar e gerenciar alunos, facilitando o controle acadêmico de uma creche em pequenos contextos educacionais.

#Demonstração
###Sistema funcionando
![Sistema rodando] (assets/sistema.png)
!(assets/sistema2.png)
###Testes
!(assets/funcionando.png)
---

#Problema
Uma escola esta com dificuldade para gestao de alunos pois ainda usa sistema manual e de planilhas e precisa de um sistema interno para melhor organização.

#Solução
Essa plataforma ira oferecer melhores formas para essa gestão, e facilitando o processo da, matricula e tambem desligamento.

#Público-Alvo
Secretaria escolar.

#Funcionalida
Cadastrar Aluno
Remover Aluno
Atualizar Dados
Buscar aluno
Listar Alunos.

#Tecnologias 
Python 3.12
Pytest(Testes)
Ruff (Verifica o código)
GitHub Actions (CI/CD)

#Estrutura do projeto

controle-gastos-cli/
│
├── src/                # Código principal
│   ├── app.py
│   ├── main.py
|   └── __init__.py
│
├── tests/              # Testes automatizados
│   └── test_app.py
│
├── .github/workflows/  # CI (GitHub Actions)
│   └── ci.yml
|
├── assets/                # Print do código funcionando
│   ├── sistema.png
|   └── testes.png
│
├── README.md
├── requirements.txt
├── .gitignore
├── pytest.ini
├── ruff.toml
├── CHANGELOG.md
├── LICENSE
└── VERSION

#Requisitos e Dependências
Python 3.11+
instalado js:
pip install -r requirements.txt

