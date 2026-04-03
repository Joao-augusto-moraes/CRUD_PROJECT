# Sistema de Gerenciamento Acadêmico - CRUD Project

Este é um projeto de sistema CRUD genérico em Python usando JSON para persistência de dados. O sistema permite gerenciar entidades acadêmicas como estudantes, professores, disciplinas, turmas e matrículas.

## Funcionalidades

- Gerenciamento completo (CRUD) de estudantes, professores, disciplinas, turmas e matrículas
- Persistência de dados em arquivos JSON
- Interface de linha de comando interativa
- Arquitetura genérica e extensível

## Como Executar

### Pré-requisitos

- Python 3.6 ou superior
- Apenas bibliotecas padrão (json, os)

### Execução

1. Clone ou baixe o projeto
2. Navegue até a pasta do projeto
3. Execute o sistema:

```bash
python src/crud.py
```

### Testes

Para executar os testes automatizados:

```bash
python tests/test_crud.py
```

Para executar os testes unitários:

```bash
python -m unittest tests/test_unit.py
```

### Popular Dados de Exemplo

Para popular a base com dados de exemplo:

```bash
python populate.py
```

## Estrutura do Projeto

```
crud_project/
├── README.md              # Este arquivo
├── requirements.txt       # Dependências
├── populate.py            # Script para popular dados
├── src/
│   └── crud.py           # Código principal
├── data/                 # Dados JSON (gerados automaticamente)
├── docs/
│   └── documentacao.md   # Documentação detalhada
└── tests/
    ├── test_crud.py      # Testes funcionais
    └── test_unit.py      # Testes unitários
```

## Entidades Gerenciadas

- **Estudantes**: Código, Nome, CPF
- **Professores**: Código, Nome, CPF
- **Disciplinas**: Código, Nome
- **Turmas**: Código da Turma, Código do Professor, Código da Disciplina
- **Matrículas**: Código da Matrícula, Código do Estudante

## Arquitetura

O sistema utiliza uma classe `Repositorio` genérica que implementa operações CRUD para qualquer entidade. A persistência é feita através de funções utilitárias que trabalham com JSON.

## Como executar

Execute o script principal:

```bash
python src/crud.py
```