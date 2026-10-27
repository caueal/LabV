# Exercício 1 - Triângulo (TDD)

## Aluno

Caue Gandini

## Repositório

https://github.com/caueal/LabV.git

---

# Estrutura do Projeto

.
├── Triangulo.py
├── TrianguloTest.py
└── README.md

---

# Ambiente

Python 3.10+

---

# Instalação

```bash
pip install -r requirements.txt
```

Conteúdo do requirements.txt:

```txt
pytest
pytest-cov
```

---

# Execução dos Testes

```bash
pytest
```

---

# Execução da Cobertura

```bash
pytest --cov=triangulo --cov-report=term-missing
```

ou

```bash
pytest --cov=triangulo --cov-report=html

CT	    Entrada	Resultado Esperado
CT01	(3,4,5)	Escaleno
CT02	(5,5,3)	Isósceles
CT03	(5,5,5)	Equilátero
CT04	(5,5,3)	Isósceles
CT05	(5,3,5)	Isósceles
CT06	(3,5,5)	Isósceles
CT07	(0,4,5)	Inválido
CT08	(-1,4,5)Inválido
CT09	(2,3,5)	Inválido
CT10	(2,3,5)	Inválido
CT11	(2,5,3)	Inválido
CT12	(5,2,3)	Inválido
CT13	(2,3,6)	Inválido
CT14	(2,3,6)	Inválido
CT15	(2,6,3)	Inválido
CT16	(6,2,3)	Inválido
CT17	(0,0,0)	Inválido

---

# Exercício 2 – Validação de Pessoa

| CT | Cenário | Resultado Esperado |
|-----|----------|-------------------|
| CT01 | Pessoa válida | Lista vazia |
| CT02 | Nome com apenas uma parte | Erro de nome |
| CT03 | Nome contendo números | Erro de nome |
| CT04 | Idade = 0 | Erro de idade |
| CT05 | Idade = 201 | Erro de idade |
| CT06 | Sem email cadastrado | Erro de email |
| CT07 | Email sem @ | Erro de email |
| CT08 | Email sem domínio | Erro de email |
| CT09 | Email sem usuário | Erro de email |

# Exercicio 03 

Name                       Stmts   Miss  Cover
------------------------------------------------
calculadora_salario.py        19      0   100%
------------------------------------------------
TOTAL                         19      0   100%

---

!! Todas as evidencias se encontram no README !!