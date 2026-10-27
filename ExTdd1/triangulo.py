class Triangulo:

    def classificar(self, a: int, b: int, c: int) -> str:

        if a <= 0 or b <= 0 or c <= 0:
            return "Inválido"

        if a + b <= c or a + c <= b or b + c <= a:
            return "Inválido"

        if a == b and b == c:
            return "Equilátero"

        if a == b or a == c or b == c:
            return "Isósceles"

        return "Escaleno"