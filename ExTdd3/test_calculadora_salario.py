import unittest

from cargo import Cargo
from funcionario import Funcionario
from calculadora_salario import CalculadoraSalario


class TestCalculadoraSalario(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraSalario()

    # DESENVOLVEDOR

    def test_desenvolvedor_salario_maior_igual_3000(self):
        funcionario = Funcionario(
            "Joao",
            "joao@email.com",
            3000.00,
            Cargo.DESENVOLVEDOR
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            2400.00
        )

    def test_desenvolvedor_salario_menor_3000(self):
        funcionario = Funcionario(
            "Joao",
            "joao@email.com",
            2500.00,
            Cargo.DESENVOLVEDOR
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            2250.00
        )

    # DBA

    def test_dba_salario_maior_igual_2000(self):
        funcionario = Funcionario(
            "Maria",
            "maria@email.com",
            2000.00,
            Cargo.DBA
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            1500.00
        )

    def test_dba_salario_menor_2000(self):
        funcionario = Funcionario(
            "Maria",
            "maria@email.com",
            1800.00,
            Cargo.DBA
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            1530.00
        )

    # TESTADOR

    def test_testador_salario_maior_igual_2000(self):
        funcionario = Funcionario(
            "Carlos",
            "carlos@email.com",
            2000.00,
            Cargo.TESTADOR
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            1500.00
        )

    def test_testador_salario_menor_2000(self):
        funcionario = Funcionario(
            "Carlos",
            "carlos@email.com",
            1800.00,
            Cargo.TESTADOR
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            1530.00
        )

    # GERENTE

    def test_gerente_salario_maior_igual_5000(self):
        funcionario = Funcionario(
            "Ana",
            "ana@email.com",
            5000.00,
            Cargo.GERENTE
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            3500.00
        )

    def test_gerente_salario_menor_5000(self):
        funcionario = Funcionario(
            "Ana",
            "ana@email.com",
            4500.00,
            Cargo.GERENTE
        )

        self.assertEqual(
            self.calculadora.calcular(funcionario),
            3600.00
        )


if __name__ == "__main__":
    unittest.main()