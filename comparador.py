from collections import Counter
import json
from time import sleep

with open('lista.json', 'r') as files:
    listas_data = json.load(files)

with open('livros.json', 'r') as files:
    livros = json.load(files)

listas = [pessoa["selecao"] for pessoa in listas_data["listas"]]

def top_n_frequentes(listas, n=12):
    contador = Counter()

    for lista in listas:
        contador.update(lista)

    mais_frequentes = contador.most_common(n)

    return [numero for numero, _ in mais_frequentes]

numeros_mais_frequentes = top_n_frequentes(listas)

livros_mais_frequentes = [(numero, livros.get(str(numero), "Desconhecido")) for numero in numeros_mais_frequentes]

print("Gerando Resultado...")
sleep(0.5)
print("Gerando Resultado...")
sleep(0.5)
print("Gerando Resultado...")
sleep(5)
print("O resultado é..............")
sleep(.8)

for numero, nome in livros_mais_frequentes:
    print(f"Número: {numero}, Livro: {nome}")