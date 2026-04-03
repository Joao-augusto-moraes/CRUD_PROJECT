#!/usr/bin/env python3
"""
Testes unitários para o sistema CRUD.
"""

import unittest
import sys
import os
import tempfile
import shutil
from typing import Dict, List, Any

# Adiciona o src ao path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from crud import Repositorio, salvar, ler_arquivo

class TestCRUD(unittest.TestCase):

    def setUp(self):
        """Configura um diretório temporário para testes."""
        self.test_dir = tempfile.mkdtemp()
        # Mock da pasta data
        self.mock_data_dir = os.path.join(self.test_dir, 'data')
        os.makedirs(self.mock_data_dir)

        # Temporariamente alterar o diretório de trabalho
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        """Limpa o diretório temporário."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_salvar_e_ler_arquivo(self):
        """Testa salvar e ler um arquivo JSON."""
        dados: List[Dict[str, Any]] = [{"id": 1, "nome": "Teste"}]
        salvar(dados, "teste.json")

        lidos = ler_arquivo("teste.json")
        self.assertEqual(lidos, dados)

    def test_repositorio_crud(self):
        """Testa operações CRUD do repositório."""
        repo = Repositorio(
            arquivo="teste.json",
            campo_id="codigo",
            label="TESTE",
            campos=[("nome", "Nome", str)]
        )

        # Testar incluir
        # Simular entrada (não podemos usar input em testes)
        # Vamos manipular diretamente
        dados: List[Dict[str, Any]] = [{"codigo": 1, "nome": "João"}]
        repo._salvar(dados)

        # Verificar listar
        # Como listar imprime, vamos verificar os dados diretamente
        carregados = repo._carregar()
        self.assertEqual(len(carregados), 1)
        self.assertEqual(carregados[0]["nome"], "João")

    def test_arquivo_inexistente(self):
        """Testa leitura de arquivo inexistente."""
        dados = ler_arquivo("inexistente.json")
        self.assertEqual(dados, [])

if __name__ == '__main__':
    unittest.main()