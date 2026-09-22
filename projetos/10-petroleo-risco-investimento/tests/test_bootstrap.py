"""Testes das funções reais do notebook, sem depender dos CSVs do curso."""

import ast
import contextlib
import io
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd


def carregar_funcoes():
    notebook = Path(__file__).resolve().parents[1] / 'sprint10.ipynb'
    cells = json.loads(notebook.read_text(encoding='utf-8'))['cells']
    context = {
        'pd': pd, 'np': np,
        'N_POCOS': 2, 'N_ESTUDADOS': 3,
        'RECEITA_UNIDADE': 1, 'ORCAMENTO': 0,
    }
    for cell in cells:
        if cell['cell_type'] != 'code':
            continue
        tree = ast.parse(''.join(cell['source']))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name in {
                'calcular_lucro', 'bootstrap_lucro',
            }:
                module = ast.Module(body=[node], type_ignores=[])
                exec(compile(module, str(notebook), 'exec'), context)
    return context


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.context = carregar_funcoes()
        self.lucro = self.context['calcular_lucro']

    def test_rotulos_repetidos_nao_multiplicam_a_selecao(self):
        target = pd.Series([100., 100., 50.], index=[0, 0, 1])
        predicted = pd.Series([90., 90., 40.], index=[0, 0, 1])
        self.assertEqual(self.lucro(target, predicted, n_pocos=2), 200.)

    def test_repeticoes_sorteadas_sao_preservadas(self):
        target = pd.Series([100., 100., 50.], index=[0, 0, 1])
        predicted = pd.Series([90., 90., 40.], index=[0, 0, 1])
        self.assertEqual(self.lucro(target, predicted, n_pocos=3), 250.)

    def test_ranking_usa_previsao_e_soma_os_valores_reais(self):
        target = pd.Series([20., 100., 50.], index=[8, 3, 15])
        predicted = pd.Series([90., 10., 80.], index=[8, 3, 15])
        self.context['RECEITA_UNIDADE'] = 4500
        self.context['ORCAMENTO'] = 100000
        self.assertEqual(self.lucro(target, predicted, n_pocos=2), 215000.)

    def test_bootstrap_constante_tem_lucro_exato(self):
        # Todas as amostras têm a mesma soma: 2 ocorrências de volume 100.
        # Sortear 3 vezes de uma população de 2 força ao menos um índice repetido.
        target = pd.Series([100., 100.])
        predicted = pd.Series([100., 100.])
        with contextlib.redirect_stdout(io.StringIO()):
            media, risco = self.context['bootstrap_lucro'](target, predicted, 'Teste')
        self.assertEqual(media, 200.)
        self.assertEqual(risco, 0.)


if __name__ == '__main__':
    unittest.main()
