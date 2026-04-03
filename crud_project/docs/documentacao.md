# Sistema de Gerenciamento Acadêmico

Este é um sistema CRUD genérico para gerenciamento de entidades acadêmicas, desenvolvido em Python puro (apenas bibliotecas padrão).

## Funcionalidades

O sistema permite gerenciar as seguintes entidades:

- **Estudantes**: Código, Nome, CPF
- **Professores**: Código, Nome, CPF
- **Disciplinas**: Código, Nome
- **Turmas**: Código da Turma, Código do Professor, Código da Disciplina
- **Matrículas**: Código da Matrícula, Código do Estudante

### Operações CRUD

Para cada entidade, são suportadas as operações:

- **Listar**: Exibe todos os registros cadastrados
- **Incluir**: Adiciona um novo registro
- **Editar**: Modifica um registro existente
- **Excluir**: Remove um registro

## Estrutura do Projeto

```
crud_project/
├── README.md              # Este arquivo
├── requirements.txt       # Dependências (apenas bibliotecas padrão)
├── src/
│   └── crud.py           # Código principal da aplicação
├── data/                 # Arquivos JSON com os dados
├── docs/                 # Documentação
└── tests/                # Testes automatizados
```

## Como Executar

1. Certifique-se de ter Python 3.6+ instalado
2. Execute o arquivo principal:

```bash
python src/crud.py
```

3. Navegue pelos menus para gerenciar as entidades

## Persistência de Dados

Os dados são armazenados em arquivos JSON na pasta `data/`. Cada entidade tem seu próprio arquivo:

- `estudantes.json`
- `professores.json`
- `disciplinas.json`
- `turmas.json`
- `matriculas.json`

## Testes

Para executar os testes automatizados:

```bash
python tests/test_crud.py
```

## Arquitetura

O sistema utiliza uma arquitetura genérica baseada na classe `Repositorio`, que pode ser facilmente estendida para novas entidades. A persistência é feita através de funções utilitárias que salvam/lerem JSON.