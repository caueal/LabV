import unittest

from person import Person
from email_model import Email
from person_dao import PersonDAO


class PersonDAOTest(unittest.TestCase):

    def setUp(self):
        self.dao = PersonDAO()

    def test_pessoa_valida(self):
        p = Person(
            1,
            "Joao Silva",
            25,
            [Email(1, "joao@email.com")]
        )

        self.assertEqual(
            self.dao.isValidToInclude(p),
            []
        )

    def test_nome_com_uma_parte(self):
        p = Person(
            1,
            "Joao",
            25,
            [Email(1, "joao@email.com")]
        )

        self.assertIn(
            "Nome deve possuir ao menos 2 partes",
            self.dao.isValidToInclude(p)
        )

    def test_nome_com_numeros(self):
        p = Person(
            1,
            "Joao123 Silva",
            25,
            [Email(1, "joao@email.com")]
        )

        self.assertIn(
            "Nome deve conter apenas letras",
            self.dao.isValidToInclude(p)
        )

    def test_idade_menor_que_1(self):
        p = Person(
            1,
            "Joao Silva",
            0,
            [Email(1, "joao@email.com")]
        )

        self.assertIn(
            "Idade deve estar entre 1 e 200",
            self.dao.isValidToInclude(p)
        )

    def test_idade_maior_que_200(self):
        p = Person(
            1,
            "Joao Silva",
            201,
            [Email(1, "joao@email.com")]
        )

        self.assertIn(
            "Idade deve estar entre 1 e 200",
            self.dao.isValidToInclude(p)
        )

    def test_sem_email(self):
        p = Person(
            1,
            "Joao Silva",
            25,
            []
        )

        self.assertIn(
            "Pessoa deve possuir ao menos um email",
            self.dao.isValidToInclude(p)
        )

    def test_email_sem_arroba(self):
        p = Person(
            1,
            "Joao Silva",
            25,
            [Email(1, "joaoemail.com")]
        )

        erros = self.dao.isValidToInclude(p)

        self.assertTrue(
            any("Email inválido" in erro for erro in erros)
        )

    def test_email_sem_dominio(self):
        p = Person(
            1,
            "Joao Silva",
            25,
            [Email(1, "joao@")]
        )

        erros = self.dao.isValidToInclude(p)

        self.assertTrue(
            any("Email inválido" in erro for erro in erros)
        )

    def test_email_sem_usuario(self):
        p = Person(
            1,
            "Joao Silva",
            25,
            [Email(1, "@gmail.com")]
        )

        erros = self.dao.isValidToInclude(p)

        self.assertTrue(
            any("Email inválido" in erro for erro in erros)
        )


if __name__ == "__main__":
    unittest.main()