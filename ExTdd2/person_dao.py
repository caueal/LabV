import re

class PersonDAO:

    def isValidToInclude(self, person):
        erros = []

        # Nome com pelo menos 2 partes e somente letras
        partes = person.name.strip().split()

        if len(partes) < 2:
            erros.append("Nome deve possuir ao menos 2 partes")

        for parte in partes:
            if not parte.isalpha():
                erros.append("Nome deve conter apenas letras")
                break

        # Idade entre 1 e 200
        if person.age < 1 or person.age > 200:
            erros.append("Idade deve estar entre 1 e 200")

        # Pelo menos um email
        if len(person.emails) == 0:
            erros.append("Pessoa deve possuir ao menos um email")

        # Validar emails
        regex = r'^[^@]+@[^@]+\.[^@]+$'

        for email in person.emails:
            if not re.match(regex, email.name):
                erros.append(f"Email inválido: {email.name}")

        return erros