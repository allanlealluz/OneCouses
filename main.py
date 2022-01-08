from functools import reduce
produtos = [
    {'nome': 'P1', 'preco': 59.90, 'peso_kg': 1.312, 'variacoes': ['a', 'b']},
    {'nome': 'P2', 'preco': 19.55, 'peso_kg': 2.300, 'variacoes': ['c', 'd']},
    {'nome': 'P3', 'preco': 9.13, 'peso_kg': 0.150, 'variacoes': ['e', 'f']},
    {'nome': 'P4', 'preco': 3.49, 'peso_kg': 0.789, 'variacoes': ['g', 'h']},
    {'nome': 'P5', 'preco': 33.22, 'peso_kg': 3.578, 'variacoes': ['i', 'j']},
    {'nome': 'P6', 'preco': 67.79, 'peso_kg': 9.920, 'variacoes': ['k', 'l']},
    {'nome': 'P7', 'preco': 45.31, 'peso_kg': 1.123, 'variacoes': ['m', 'n']},
    {'nome': 'P8', 'preco': 93.27, 'peso_kg': 0.521, 'variacoes': ['o', 'p']},
    {'nome': 'P9', 'preco': 1.90, 'peso_kg': 1.300, 'variacoes': ['q', 'r']},
]
precos = list(map(lambda p: p['preco'],produtos))
precos_list_comprehencion = [produto['preco'] for produto in produtos]
precos_s = list(filter(lambda p: p['preco'] > 20,produtos))
produto_filter_list_comprehencion = [produto['preco'] for produto in produtos if produto['preco'] > 20]
preco_total = reduce(lambda soma,p: soma+p['preco'],produtos,0)
print(precos)
print(precos_s)
print(precos_list_comprehencion)
print(produto_filter_list_comprehencion)
print(preco_total)
