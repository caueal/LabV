import unittest 
from triangulo import Triangulo


class TrianguloTest(unittest.TestCase):

    def setUp(self):
        self.triangulo = Triangulo()


    # testes de validade 

    # teste validade escaleno
    def test_escaleno_valido(self):
        self.assertEqual(
            self.triangulo.classificar(3, 4, 5),
            "Escaleno"
           )

    # teste validade isoceles 
    def test_isosceles_valido(self):
        self.assertEqual(
            self.triangulo.classificar(3, 3, 5),
            "Isósceles"
        )

    # teste triangulo equilatero 
    def test_equilatero_valido(self): 
        self.assertEqual(
            self.triangulo.classificar(3, 3, 3),
            "Equilátero"
        )

    # Permutacoes triangulo isoscleles 

    def test_isosceles_per1(self): 
        self.assertEqual(
            self.triangulo.classificar(5, 5, 3),
            "Isósceles"
        )

    def test_isosceles_per2(self): 
        self.assertEqual(
            self.triangulo.classificar(5, 5, 3),
            "Isósceles"
         )    

    def test_isosceles_per3(self): 
        self.assertEqual(
            self.triangulo.classificar(5, 5, 3),
            "Isósceles"
        ) 

    #Um valor zero 

    def test_valor_zero(self): 
        self.assertEqual(
            self.triangulo.classificar(3, 0, 4),
            "Inválido"
        )       

    #Um valor negativo

    def test_valor_neg(self): 
        self.assertEqual(
            self.triangulo.classificar(3, -3, 4),
            "Inválido"
        )

    #Soma de 2 valores igual ao 3

    def test_valor_soma2(self): 
        self.assertEqual(
            self.triangulo.classificar(3, 3, 6),
            "Inválido"
        )

    # 8. Permutações da soma igual ao terceiro
    def test_soma_igual_perm_1(self):
        self.assertEqual(
            self.triangulo.classificar(2, 3, 5),
            "Inválido"
        )

    def test_soma_igual_perm_2(self):
        self.assertEqual(
            self.triangulo.classificar(2, 5, 3),
            "Inválido"
        )

    def test_soma_igual_perm_3(self):
        self.assertEqual(
            self.triangulo.classificar(5, 2, 3),
            "Inválido"
        )

    # 9. Soma de dois lados menor que o terceiro
    def test_soma_menor_que_terceiro(self):
        self.assertEqual(
            self.triangulo.classificar(2, 3, 6),
            "Inválido"
        )

    # 10. Permutações da soma menor que o terceiro
    def test_soma_menor_permutacao_1(self):
        self.assertEqual(
            self.triangulo.classificar(2, 3, 6),
            "Inválido"
        )

    def test_soma_menor_permutacao_2(self):
        self.assertEqual(
            self.triangulo.classificar(2, 6, 3),
            "Inválido"
        )

    def test_soma_menor_permutacao_3(self):
        self.assertEqual(
            self.triangulo.classificar(6, 2, 3),
            "Inválido"
        )

    # 11. Três valores iguais a zero
    def test_tres_zeros(self):
        self.assertEqual(
            self.triangulo.classificar(0, 0, 0),
            "Inválido"
        )

if __name__ == "__main__":
    unittest.main()    