# Vaga para Estágio - TI - Projeto Classificatório

Minha solução para o problema proposto no Processo Seletivo da Racoon, Estágio TI, 2019 

## Task
Usando **Python** ou Javascript, fazer as correções e validações propostas em um conjunto de dados JSON corrompido, o qual pode ser baixado no nesse [link](https://github.com/bzamith/processo_seletivo-racoon/blob/master/broken-database.json)

Mais especificamente, criar três funções para percorrer o banco de dados corrompido e corrigir os três erros descritos:
1. Nos nomes;
2. Nos preços;
3. Nas quantidades.

Para validação, criar
1. Uma função que imprime a lista com todos os nomes dos produtos, ordenados primeiro por categoria em ordem alfabética, depois ordenados por id em ordem crescente;
2. Uma função que calcula qual é o valor total do estoque por categoria, ou seja, a soma do valor de todos os produtos em estoque de cada categoria, considerando a quantidade de cada produto.

## Implementação
* Python 3 (_não compatível com versões anteriores_)
* Pandas Dataframe
* Classe "Produto"

## Execução
No diretório onde se encontra o arquivo [broken-database.json](https://github.com/bzamith/processo_seletivo-racoon/blob/master/broken-database.json), executar:

```bash
> pip3 install -r requirements.txt
> python3 psRacoon.py
```

Output: [Diretório "Saídas"](https://github.com/bzamith/processo_seletivo-racoon/tree/master/Saidas)

## Lógica
A classe Produto é criada para poder armanezar os dados de cada produto afim de poder fazer as validações solicitadas. Para as correções, a classe não é utilizada, fazendo-se uso apenas de parsing do arquivo [broken-database.json](https://github.com/bzamith/processo_seletivo-racoon/blob/master/broken-database.json).

Depois de armazenadas as instâncias de Produto, as validações foram feitas a partir de uma tabela (dataframe) do [Pandas](https://pandas.pydata.org/). As funções "[sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html)" e "[groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)" auxiliam na ordenação e no agrupamento, respectivamente. 

A sequência de execução é:
1. Lê o arquivo corrompido
2. Faz a primeira correção solicitada
3. Faz a segunda correção solicitada
4. Faz a terceira correção solicitada
5. Salva o arquivo corrigido
6. Cria instâncias da classe Produto com base no arquivo corrigido
7. Faz a primeira validação solicitada
8. Faz a segunda validação solicitada

### Funções
- "salva_produtos": A partir do json corrigido, gera as instâncias da classe Produto e armazena.
- "corrige_nomes": Faz a primeira correção solicitada
- "corrige_precos": Faz a segunda correção solicitada
- "corrige_quantidades": Faz a terceira correção solicitada
- "imprime_nomes": Gera output da primeira validação solicitada
- "imprime_valor_estoque": Gera outuput da segunda validação solicitada

### Saídas
São gerados três arquivos de saída:
- [corrected-database.json](https://github.com/bzamith/processo_seletivo-racoon/blob/master/Saidas/corrected-database.json): Database corrigido
- [imprimenomes.txt](https://github.com/bzamith/processo_seletivo-racoon/blob/master/Saidas/imprimenomes.txt): Saída da primeira validação solicitada
- [imprimeestoque.txt](https://github.com/bzamith/processo_seletivo-racoon/blob/master/Saidas/imprimeestoque.txt): Saída da segunda validação solicitada
