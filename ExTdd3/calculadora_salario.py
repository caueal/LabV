from cargo import Cargo


class CalculadoraSalario:

    def calcular(self, funcionario):

        salario = funcionario.salario_base

        if funcionario.cargo == Cargo.DESENVOLVEDOR:
            if salario >= 3000:
                return salario * 0.80
            return salario * 0.90

        elif funcionario.cargo == Cargo.DBA:
            if salario >= 2000:
                return salario * 0.75
            return salario * 0.85

        elif funcionario.cargo == Cargo.TESTADOR:
            if salario >= 2000:
                return salario * 0.75
            return salario * 0.85

        elif funcionario.cargo == Cargo.GERENTE:
            if salario >= 5000:
                return salario * 0.70
            return salario * 0.80

        raise ValueError("Cargo inválido")