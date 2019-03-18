#Processo Seletivo Racoon
import pandas as pd 

class Produto:
	def __init__(self,p_id,name,quantity,price,category):
		self.p_id = p_id
		self.name = name
		self.quantity = quantity
		self.price = price
		self.category = category

#Para salvar no Banco de Dados
def salva_produtos(data):
	produtos = list()
	for i in range(0,len(data)):
		if "\"id" in data[i]:
			index = len("    \"id\": ")
			p_id = data[i][index:len(data[i])-1].replace(",","") 
		elif "\"name" in data[i]:
			index = len("    \"name\": ")
			name = data[i][index:len(data[i])-1].replace(",","")
			name = name.replace("\"","") 
		elif "\"quantity" in data[i]:
			index = len("    \"quantity\": ")
			quantity = data[i][index:len(data[i])-1].replace(",","")
			quantity = quantity.replace("\"","") 
		elif "\"price" in data[i]:
			index = len("    \"price\": ")
			price = data[i][index:len(data[i])-1].replace(",","")
			price = price.replace("\"","") 
		elif "\"category" in data[i]:
			index = len("    \"category\": ")
			category = data[i][index:len(data[i])-1].replace(",","")
			category = category.replace("\"","") 
			produtos.append(Produto(p_id,name,quantity,price,category))
	return produtos

#Substitui os caracteres corrompidos
def corrige_nomes(data):
	for i in range(0,len(data)):
		#Soh confere para nome de produtos
		if "\"name" in data[i]:
			data[i] = data[i].replace("æ","a")
			data[i] = data[i].replace("¢","c")
			data[i] = data[i].replace("ø","o")
			data[i] = data[i].replace("ß","b")

#Corrige os precos corrompidos
def corrige_precos(data):
	for i in range(0,len(data)):
		index = len("    \"price\":")
		#Soh confere para precos
		if "\"price" in data[i]:
			data[i] = data[i][:index]+data[i][index:].replace("\"","")

#Corrige as quantidades inexistentes
def corrige_quantidades(data):
	for i in range(0,len(data)):
		#Eh para ter "quantity" depois de cada "name"
		if "\"name" in data[i]:
			if "\"quantity" not in data[i+1]:
				data[i+1] = "    \"quantity\": 0,\n" + data[i+1]

#Imprime nomes ordenados
def imprime_nomes(produtos):
	size = len(produtos)
	name = [""]*size
	category = [""]*size
	p_id = [0]*size
	for i in range(0,size):
		name[i] = produtos[i].name
		category[i] = produtos[i].category
		p_id[i] = produtos[i].p_id
	d = {'name': name, 'category': category, 'p_id': p_id}
	df = pd.DataFrame(data = d)
	df = df.sort_values(['category','p_id'],ascending=[True,True])
	with open('imprimenomes.txt', 'w') as file:
		print(df, file=file)

#Imprime valor do estoque por categoria
def imprime_valor_estoque(produtos):
	size = len(produtos)
	category = [""]*size
	valor = [0]*size
	for i in range(0,size):
		category[i] = produtos[i].category
		valor[i] = int(produtos[i].quantity)*float(produtos[i].price)
	#Cria uma tabela com os dados
	d = {'category': category, 'valor': valor}
	df = pd.DataFrame(data = d)
	#Ordena
	df = df.groupby(['category']).sum()
	with open('imprimeestoque.txt', 'w') as file:
		print(df, file=file)

#Le bd
def le_bd(file_name):
	with open(file_name, 'r') as file:
		data = file.readlines()
	return data

#Escreve bd
def escreve_bd(file_name):
	with open(file_name, 'w') as file:
		for line in data:
			file.write(line)

#Funcao Principal
if __name__ == '__main__':
	#Le bd corrompido
	data = le_bd("broken-database.json")
	
	#Faz as correcoes
	corrige_nomes(data)
	corrige_precos(data)
	corrige_quantidades(data)
	
	#Escreve bd corrigido
	escreve_bd("corrected-database.json")
	
	#Verifica
	data = le_bd("corrected-database.json")
	produtos = salva_produtos(data)
	imprime_nomes(produtos)
	imprime_valor_estoque(produtos)
	


