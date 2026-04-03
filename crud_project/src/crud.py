import json
import os
from typing import List, Dict, Tuple, Any, Optional, Callable


# ─────────────────────────────────────────────
#  PERSISTÊNCIA GENÉRICA
# ─────────────────────────────────────────────

def salvar(lista: List[Dict[str, Any]], nome_arquivo: str) -> None:
    """Salva uma lista como JSON no arquivo indicado."""
    caminho = os.path.join("data", nome_arquivo)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)


def ler_arquivo(nome_arquivo: str) -> List[Dict[str, Any]]:
    """Lê um arquivo JSON e retorna uma lista. Retorna [] se não existir."""
    caminho = os.path.join("data", nome_arquivo)
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  [AVISO] Erro ao ler '{caminho}': {e}")
        return []


# ─────────────────────────────────────────────
#  REPOSITÓRIO GENÉRICO  (elimina duplicação)
# ─────────────────────────────────────────────

class Repositorio:
    """
    Repositório CRUD genérico para qualquer entidade salva em JSON.

    Parâmetros
    ----------
    arquivo   : nome do arquivo JSON (ex.: 'estudantes.json')
    campo_id  : chave do dicionário usada como identificador único (ex.: 'codigo')
    label     : nome amigável exibido nos menus (ex.: 'ESTUDANTE')
    campos    : lista de tuplas (chave, prompt, tipo) para inclusão/edição
    """

    def __init__(self, arquivo: str, campo_id: str, label: str, campos: List[Tuple[str, str, type]]):
        self.arquivo = arquivo
        self.campo_id = campo_id
        self.label = label
        self.campos = campos  # [(chave, prompt, tipo), ...]

    # ── utilidades internas ──────────────────

    def _carregar(self) -> List[Dict[str, Any]]:
        return ler_arquivo(self.arquivo)

    def _salvar(self, dados: List[Dict[str, Any]]) -> None:
        salvar(dados, self.arquivo)

    def _buscar(self, dados: List[Dict[str, Any]], codigo: int) -> Optional[Dict[str, Any]]:
        return next((d for d in dados if d.get(self.campo_id) == codigo), None)

    @staticmethod
    def _ler_inteiro(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("  [ERRO] Digite apenas números inteiros.")

    # ── operações CRUD ───────────────────────

    def listar(self) -> None:
        print(f"\n  ── Listando {self.label}S ──")
        dados = self._carregar()
        if not dados:
            print("  Nenhum registro cadastrado.")
            return
        for item in dados:
            linha = " | ".join(f"{k}: {v}" for k, v in item.items())
            print(f"  {linha}")

    def incluir(self) -> None:
        print(f"\n  ── Incluir {self.label} ──")
        dados = self._carregar()

        # lê o código garantindo unicidade
        while True:
            codigo = self._ler_inteiro(f"  Código do(a) {self.label}: ")
            if self._buscar(dados, codigo):
                print(f"  [AVISO] Código {codigo} já existe. Tente outro.")
            else:
                break

        novo = {self.campo_id: codigo}
        for chave, prompt, tipo in self.campos:
            while True:
                valor = input(f"  {prompt}: ").strip()
                if not valor:
                    print("  [ERRO] Campo obrigatório.")
                    continue
                try:
                    novo[chave] = tipo(valor)
                    break
                except ValueError:
                    print(f"  [ERRO] Valor inválido para {chave}.")

        dados.append(novo)
        self._salvar(dados)
        print(f"  {self.label} cadastrado(a) com sucesso!")

    def excluir(self) -> None:
        print(f"\n  ── Excluir {self.label} ──")
        dados = self._carregar()
        codigo = self._ler_inteiro(f"  Código do(a) {self.label} a excluir: ")
        item = self._buscar(dados, codigo)
        if item is None:
            print(f"  [AVISO] Código {codigo} não encontrado.")
            return
        dados.remove(item)
        self._salvar(dados)
        print(f"  {self.label} removido(a) com sucesso!")

    def editar(self) -> None:
        print(f"\n  ── Editar {self.label} ──")
        dados = self._carregar()
        codigo = self._ler_inteiro(f"  Código do(a) {self.label} a editar: ")
        item = self._buscar(dados, codigo)
        if item is None:
            print(f"  [AVISO] Código {codigo} não encontrado.")
            return

        print("  (Pressione Enter para manter o valor atual)")
        for chave, prompt, tipo in self.campos:
            atual = item.get(chave, "")
            entrada = input(f"  {prompt} [{atual}]: ").strip()
            if entrada:
                try:
                    item[chave] = tipo(entrada)
                except ValueError:
                    print(f"  [AVISO] Valor inválido; '{chave}' mantido.")

        # permite alterar o próprio código
        novo_codigo_str = input(f"  Novo código [{codigo}]: ").strip()
        if novo_codigo_str:
            try:
                novo_codigo = int(novo_codigo_str)
                if novo_codigo != codigo and self._buscar(dados, novo_codigo):
                    print("  [AVISO] Novo código já existe; código mantido.")
                else:
                    item[self.campo_id] = novo_codigo
            except ValueError:
                print("  [AVISO] Código inválido; mantido o original.")

        self._salvar(dados)
        print(f"  {self.label} atualizado(a) com sucesso!")


# ─────────────────────────────────────────────
#  CONFIGURAÇÃO DAS ENTIDADES
# ─────────────────────────────────────────────

ENTIDADES = [
    Repositorio(
        arquivo="estudantes.json",
        campo_id="codigo",
        label="ESTUDANTE",
        campos=[
            ("nome", "Nome do(a) estudante", str),
            ("cpf",  "CPF do(a) estudante",  str),
        ],
    ),
    Repositorio(
        arquivo="professores.json",
        campo_id="codigo",
        label="PROFESSOR(A)",
        campos=[
            ("nome", "Nome do(a) professor(a)", str),
            ("cpf",  "CPF do(a) professor(a)",  str),
        ],
    ),
    Repositorio(
        arquivo="turmas.json",
        campo_id="codigo_turma",
        label="TURMA",
        campos=[
            ("codigo_professor",  "Código do professor",  int),
            ("codigo_disciplina", "Código da disciplina", int),
        ],
    ),
    Repositorio(
        arquivo="matriculas.json",
        campo_id="codigo_matricula",
        label="MATRÍCULA",
        campos=[
            ("codigo_estudante", "Código do estudante", int),
        ],
    ),
    Repositorio(
        arquivo="disciplinas.json",
        campo_id="codigo",
        label="DISCIPLINA",
        campos=[
            ("nome", "Nome da disciplina", str),
        ],
    ),
]


# ─────────────────────────────────────────────
#  MENUS
# ─────────────────────────────────────────────

def mostrar_menu_principal() -> int:
    print("\n" + "=" * 50)
    print("   SISTEMA DE GERENCIAMENTO ACADÊMICO")
    print("=" * 50)
    for i, entidade in enumerate(ENTIDADES, start=1):
        print(f"  [{i}] Gerenciar {entidade.label}S")
    print(f"  [{len(ENTIDADES) + 1}] Encerrar")
    print("=" * 50)
    while True:
        try:
            opcao = int(input("  Escolha uma opção: "))
            if 1 <= opcao <= len(ENTIDADES) + 1:
                return opcao
            print("  [ERRO] Opção inválida.")
        except ValueError:
            print("  [ERRO] Digite apenas números.")


def menu_operacoes(label: str) -> int:
    print(f"\n  ── Operações: {label} ──")
    print("  [1] Listar")
    print("  [2] Incluir")
    print("  [3] Excluir")
    print("  [4] Editar")
    print("  [5] Voltar ao menu principal")
    while True:
        try:
            opcao = int(input("  Escolha uma opção: "))
            if 1 <= opcao <= 5:
                return opcao
            print("  [ERRO] Opção inválida.")
        except ValueError:
            print("  [ERRO] Digite apenas números.")


# ─────────────────────────────────────────────
#  LOOP PRINCIPAL
# ─────────────────────────────────────────────

OPERACOES: Dict[int, Callable[['Repositorio'], None]] = {
    1: lambda repo: repo.listar(),
    2: lambda repo: repo.incluir(),
    3: lambda repo: repo.excluir(),
    4: lambda repo: repo.editar(),
}


def executar() -> None:
    print("\n  Bem-vindo ao Sistema de Gerenciamento Acadêmico!")
    while True:
        escolha = mostrar_menu_principal()

        if escolha == len(ENTIDADES) + 1:
            print("\n  Sistema encerrado. Até logo!\n")
            break

        repositorio = ENTIDADES[escolha - 1]

        while True:
            operacao = menu_operacoes(repositorio.label)
            if operacao == 5:
                break
            acao = OPERACOES.get(operacao)
            if acao:
                acao(repositorio)


if __name__ == "__main__":
    executar()
