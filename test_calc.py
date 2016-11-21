from unittest import TestCase
from calc import *

class Test_Transforma_csv_em_lista(TestCase):
    def test_transforma_csv_em_lista_vazia(self):
        self.assertEqual(transforma_csv_em_lista([]),[])

    def test_transforma_csv_em_lista_1_elemento(self):
        self.assertEqual(transforma_csv_em_lista(['Ana;10.0']), [('Ana', 10.0)])
        self.assertEqual(transforma_csv_em_lista(['Ana;10.0\n']), [('Ana', 10.0)])

    def test_transforma_csv_em_lista_2_elementos(self):
        self.assertEqual(transforma_csv_em_lista(['Ana;10.0','Ana;20.0']),
                         [('Ana', 10.0), ('Ana', 20)])
        self.assertEqual(transforma_csv_em_lista(['Ana;10.0\n','Ana;20.0\n']),
                         [('Ana', 10.0), ('Ana', 20)])

    def test_transforma_csv_em_lista_2_elementos_nomes_diferentes(self):
        self.assertEqual(transforma_csv_em_lista(['Ana;10.0\n', 'Bia;20.0\n']),
                         [('Ana', 10.0), ('Bia', 20)])

    def test_transforma_csv_em_lista_2_elementos_nomes_diferentes(self):
        self.assertEqual(transforma_csv_em_lista(['Bia;10.0\n', 'Ana;20.0\n']),
                         [('Ana', 20.0), ('Bia', 10.0)])

class Test_Agrupa_dividas_por_nome(TestCase):
    def test_agrupa_dividas_por_nome_vazio(self):
        self.assertEqual(agrupa_dividas_por_nome([]),
                         {})

    def test_agrupa_dividas_por_nome_1_nome_1_divida(self):
        self.assertEqual(agrupa_dividas_por_nome([('Ana', 10.0)]),
                         {'Ana': [10.0]})

    def test_agrupa_dividas_por_nome_1_nome_2_dividas(self):
        self.assertEqual(agrupa_dividas_por_nome([('Ana', 10.0), ('Ana', 20.0)]),
                         {'Ana': [10.0, 20.0]})

    def test_agrupa_dividas_por_nome_2_nome_1_divida(self):
        self.assertEqual(agrupa_dividas_por_nome([('Ana', 10.0), ('Bia', 20.0)]),
                         {'Ana': [10.0], 'Bia': [20.0]})

    def test_agrupa_dividas_por_nome_2_nome_2_dividas(self):
        self.assertEqual(agrupa_dividas_por_nome([('Ana Luiza', 10.0), ('Bia', 20.0),
                                                  ('Bia', 30.0), ('Ana Luiza', 40.0)]),
                         {'Ana Luiza': [10.0, 40.0], 'Bia': [20.0, 30.0]})


class Test_Soma_dividas_por_nome(TestCase):
    def test_soma_dividas_por_nome_vazio(self):
        self.assertEqual(soma_dividas_por_nome({}),{})

    def test_soma_dividas_por_nome_1_lancamento(self):
        self.assertEqual(soma_dividas_por_nome({'Ana': [10.0]}),{'Ana': 10.0})

    def test_soma_dividas_por_nome_2_lancamentos(self):
        self.assertEqual(soma_dividas_por_nome({'Ana': [10.0, 20.0]}),
                         {'Ana': 30.0})

    def test_soma_dividas_por_nome_clientes_diferentes(self):
        self.assertEqual(soma_dividas_por_nome({'Ana': [10.0], 'Bia': [20.0]}),
                         {'Ana': 10.0, 'Bia':20.0})

    def test_soma_dividas_por_nome_clientes_diferentes_diversas_contas(self):
        self.assertEqual(soma_dividas_por_nome({'Ana': [10.0, 40.0], 'Bia': [10.0, 15.0]}),
                         {'Ana': 50.0, 'Bia': 25.0})

class Test_Top_dividas(TestCase):
    def test_top_dividas_vazio(self):
        self.assertEqual(top_dividas({}), [])

    def test_top_dividas_1_item(self):
        self.assertEqual(top_dividas({'Ana': 30.0}), [('Ana', 30.0)])

    def test_top_dividas_2_itens_ordenado(self):
        self.assertEqual(top_dividas({'Ana': 50.0, 'Bia': 25.0}),
                         [('Ana', 50.0),('Bia', 25.0)])

    def test_top_dividas_2_itens_desordenados(self):
        self.assertEqual(top_dividas({'Ana': 10.0, 'Bia': 25.0}),
                         [('Bia', 25.0), ('Ana', 10.0)])

    def test_top_dividas_4_itens_desordenados(self):
        self.assertEqual(top_dividas({'Ana': 10.0, 'Bia': 25.0, 'Ale': 5.0, 'Cris': 7.0}),
                         [('Bia', 25.0), ('Ana', 10.0), ('Cris', 7.0), ('Ale', 5.0)])

    def test_top_dividas_4_itens_desordenados_pega_2(self):
        self.assertEqual(top_dividas({'Ana': 10.0, 'Bia': 25.0, 'Ale': 5.0, 'Cris': 7.0}, 2),
                         [('Bia', 25.0), ('Ana', 10.0)])
