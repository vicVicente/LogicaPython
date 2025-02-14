import pandas as pd

#Aqui estou abrindo o arquivo CSV, criando uma "coluna virtual", onde eu adicono o faturamento por produto
tabela = pd.read_csv("Vendas.csv", sep=";")
tabela["faturamento"] = tabela["quantidade"] * tabela["preco_unitario"]
faturamentoProduto = tabela.set_index("produto")["faturamento"]

print("O faturamento por produto é:\n" + str(faturamentoProduto))

#Como na linha 7 eu adicionei o index "produto" para cada item, fica fácil buscar o maior e menor faturamenteo retornando apenas o index.
print("O produto com maior faturamento é " + str(faturamentoProduto.idxmax()))
print("O produto com menor faturamento é " + str(faturamentoProduto.idxmin()))