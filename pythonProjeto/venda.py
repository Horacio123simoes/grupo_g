produtos=[
{'nome':'feijão','preco':500,'estoque':50}, {'nome':'arroz','preco':600,'estoque':80}, {'nome':'massa','preco':200,'estoque':20}
]

def vender_produto():
	nome_produto=input('digita o nome do produto que deseja compra?: ')
	#for produto in produtos:
	if produtos[i]==nome_produto:
		if produtos[i]==0:
			 print('produto{nome_produto} sem estoque!')
		else:
			produtos[i]-=1
			print('produto{nome_produto} vendido com sucesso!')
			print(f'estoque restante:',{produtos[i]})
		return
		print('produto{nome_produto}não encontrado!')

def consultar_produto():
	nome_produto=input('digita o nome do produto que deseja consultar: ')
	for produto in produtos:
		if produto['nome']==nome_produto:
		   #print(f'nome:{produtos[produto]}preco: kz{produtos[produto]}estoque:{produtos[produto]})
			print()
	    return
			print(f'produto{nome_produto} não encontrado!')
while True:
	print('\n [1] vender produtos')
	print('\n [2] consultar produtos')
	print('\n [3] sair')
	opcao=input('digita a opcão desejada: ')
	if opcao=='1':
		vender_produto()
	if opcao=='2':
		consultar_produto()
	if opcão=='3':
		break
	else:
		print('opcão invalida!')