#!/usr/bin/env python3
"""
Script para testar as operações CRUD.
"""

import sys
import os
from typing import Dict, List, Any

# Adiciona o src ao path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from crud import ENTIDADES

def testar_listar():
    """Testa a operação de listar para cada entidade."""
    print("=== TESTANDO LISTAR ===")
    for entidade in ENTIDADES:
        print(f"\n--- {entidade.label}S ---")
        entidade.listar()

def testar_incluir():
    """Testa incluir um novo registro (simulado)."""
    print("\n=== TESTANDO INCLUIR ===")
    # Para estudantes, vamos adicionar um novo
    estudantes_repo = ENTIDADES[0]  # estudantes
    dados: List[Dict[str, Any]] = estudantes_repo._carregar()
    novo_estudante: Dict[str, Any] = {
        "codigo": 4,
        "nome": "Teste Silva",
        "cpf": "000.000.000-00"
    }
    dados.append(novo_estudante)
    estudantes_repo._salvar(dados)
    print("Novo estudante adicionado para teste.")

def testar_editar():
    """Testa editar um registro."""
    print("\n=== TESTANDO EDITAR ===")
    estudantes_repo = ENTIDADES[0]
    dados: List[Dict[str, Any]] = estudantes_repo._carregar()
    for item in dados:
        if item["codigo"] == 4:
            item["nome"] = "Teste Editado"
            break
    estudantes_repo._salvar(dados)
    print("Estudante editado.")

def testar_excluir():
    """Testa excluir um registro."""
    print("\n=== TESTANDO EXCLUIR ===")
    estudantes_repo = ENTIDADES[0]
    dados: List[Dict[str, Any]] = estudantes_repo._carregar()
    dados = [d for d in dados if d["codigo"] != 4]
    estudantes_repo._salvar(dados)
    print("Estudante removido.")

if __name__ == "__main__":
    testar_listar()
    testar_incluir()
    testar_listar()
    testar_editar()
    testar_listar()
    testar_excluir()
    testar_listar()
    print("\nTestes concluídos!")