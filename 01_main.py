# 7 Funções do Python que vao mudar a forma de como  programar

### Diego dos Santos -- develloper Goiânia Goiás

nomes = ["Diego", "Braynner", "Bento"]
cargos = ["Analista", "Gerente", "Coordenador"]
salarios = [5000, 1000, 3500]

dados_funcionarios = list(zip(nomes, cargos, salarios))

valores = zip(cargos,salarios)
dicionario_funcionarios = dict(zip(nomes, valores))
print(dados_funcionarios)
print(dicionario_funcionarios)

# lambda
salario_funcionario = 5000

def ajustar_salario1(salario):
    novo_salario = salario * 1.1
    return novo_salario

ajustar_salario2 = lambda x: x * 1.1
print(ajustar_salario1(salario_funcionario))
print(ajustar_salario2(salario_funcionario))

# map
novos_salarios = list(map(ajustar_salario2, salarios))
print(novos_salarios)

# map
novos_salarios = list(map(lambda x: x *1.1, salarios))
print(novos_salarios)

# filter
salarios_altos = list(filter(lambda x: x > 6000, salarios))
print(salarios_altos)

clientes = [
    {"nome": "Diego", "compras": 1500},
    {"nome": "Braynner", "compras": 7000},
    {"nome": "Diego", "compras": 900},

]

clientes_vip = list( filter(lambda x: x["compras"] > 5000, clientes))
print(clientes_vip)

# Any e a11
pagamentos = [True, True, True, False, True]
print("Todos os pagamentos foram feitos?", all(pagamentos))
print("Algum pagamento foi feito com sucesso?", any(pagamentos))


# sorted
funcionarios = [
    {"nome": "Ana", "salario": 5000},
    {"nome": "Diego", "salario": 12000},
    {"nome": "Rosimeire", "salario": 900},

]

funcionarios = sorted(funcionarios, key=lambda x: x["salario"])
print(funcionarios)


# f-string
nome_empresa = "Techforta"
mes= "Abril"
faturamento = 150000
mensagem = f"Relatorio do mês de {mes}: o faturamento da {nome_empresa} foi de R$ {faturamento}"
print(mensagem)