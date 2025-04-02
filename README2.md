# 7 Funções do Python que vão mudar a forma de programar

### Diego dos Santos - Developer | Goiânia, Goiás

O Python é uma linguagem poderosa e versátil. Aqui estão sete funções que podem revolucionar a forma como você programa:

## 1. `zip()`
Permite combinar listas em pares de valores, criando listas de tuplas ou dicionários.

**Exemplo:**
```python
nomes = ["Diego", "Braynner", "Bento"]
cargos = ["Analista", "Gerente", "Coordenador"]
salarios = [5000, 1000, 3500]

dados_funcionarios = list(zip(nomes, cargos, salarios))
dicionario_funcionarios = dict(zip(nomes, zip(cargos, salarios)))
print(dados_funcionarios)
print(dicionario_funcionarios)
```

## 2. `lambda`
Cria funções anônimas de forma mais concisa.

**Exemplo:**
```python
ajustar_salario = lambda x: x * 1.1
print(ajustar_salario(5000))
```

## 3. `map()`
Aplica uma função a todos os itens de uma lista.

**Exemplo:**
```python
novos_salarios = list(map(lambda x: x * 1.1, salarios))
print(novos_salarios)
```

## 4. `filter()`
Filtra elementos de uma lista com base em uma condição.

**Exemplo:**
```python
salarios_altos = list(filter(lambda x: x > 6000, salarios))
print(salarios_altos)
```

## 5. `all()` e `any()`
Verifica se todos ou pelo menos um dos elementos de uma lista são verdadeiros.

**Exemplo:**
```python
pagamentos = [True, True, True, False, True]
print("Todos pagos?", all(pagamentos))
print("Algum pagamento feito?", any(pagamentos))
```

## 6. `sorted()`
Ordena listas de dicionários de acordo com uma chave específica.

**Exemplo:**
```python
funcionarios = [
    {"nome": "Ana", "salario": 5000},
    {"nome": "Diego", "salario": 12000},
    {"nome": "Rosimeire", "salario": 900},
]

funcionarios = sorted(funcionarios, key=lambda x: x["salario"])
print(funcionarios)
```

## 7. `f-string`
Facilita a formatação de strings de maneira intuitiva.

**Exemplo:**
```python
nome_empresa = "Techforta"
mes = "Abril"
faturamento = 150000
mensagem = f"Relatório do mês de {mes}: o faturamento da {nome_empresa} foi de R$ {faturamento}"
print(mensagem)
```

Essas funções vão ajudar a tornar seu código mais limpo, eficiente e Pythonic!

