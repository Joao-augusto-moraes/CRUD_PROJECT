#!/usr/bin/env python3
"""
Script para popular a base de dados com dados de exemplo.
"""

import sys
import os
from typing import Dict, List, Any

# Adiciona o src ao path para importar crud
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from crud import ENTIDADES

def popular_dados():
    """Popula cada entidade com dados de exemplo."""

    # Dados de exemplo para estudantes
    estudantes: List[Dict[str, Any]] = [
        {"codigo": 1, "nome": "João Silva", "cpf": "123.456.789-00"},
        {"codigo": 2, "nome": "Maria Santos", "cpf": "987.654.321-00"},
        {"codigo": 3, "nome": "Pedro Oliveira", "cpf": "456.789.123-00"},
    ]

    # Professores
    professores: List[Dict[str, Any]] = [
        {"codigo": 1, "nome": "Prof. Ana Costa", "cpf": "111.222.333-44"},
        {"codigo": 2, "nome": "Prof. Carlos Lima", "cpf": "555.666.777-88"},
    ]

    # Disciplinas
    disciplinas: List[Dict[str, Any]] = [
        {"codigo": 1, "nome": "Matemática"},
        {"codigo": 2, "nome": "Português"},
        {"codigo": 3, "nome": "História"},
    ]

    # Turmas
    turmas: List[Dict[str, Any]] = [
        {"codigo_turma": 1, "codigo_professor": 1, "codigo_disciplina": 1},
        {"codigo_turma": 2, "codigo_professor": 2, "codigo_disciplina": 2},
    ]

    # Matrículas
    matriculas: List[Dict[str, Any]] = [
        {"codigo_matricula": 1, "codigo_estudante": 1},
        {"codigo_matricula": 2, "codigo_estudante": 2},
        {"codigo_matricula": 3, "codigo_estudante": 3},
    ]

    dados_exemplo: Dict[str, List[Dict[str, Any]]] = {
        "estudantes.json": estudantes,
        "professores.json": professores,
        "disciplinas.json": disciplinas,
        "turmas.json": turmas,
        "matriculas.json": matriculas,
    }

    for entidade in ENTIDADES:
        if entidade.arquivo in dados_exemplo:
            entidade._salvar(dados_exemplo[entidade.arquivo])
            print(f"Dados populados para {entidade.arquivo}")

if __name__ == "__main__":
    popular_dados()
    print("Base de dados populada com sucesso!")