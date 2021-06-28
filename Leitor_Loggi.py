'''Ordem das Trincas
1 Região de Origem
2 Região de Destino
3 Código da Loggi
4 Código do Vendedor do produto
5 Tipo do produto

Região Código
Centro-oeste 111
Nordeste 333
Norte 555
Sudeste 888
Sul 000

Tipo do Produto Código
Jóias 000
Livros 111
Eletrônicos 333
Bebidas 555
Brinquedos 888'''



regiao=["Centro-oeste", "Nordeste", "Norte", "Sudeste", "Sul"]
cod_reg=['111','333','555','888','000']
produto=['Jóias','Livros','Eletrônicos','Bebidas','Brinquedos']
cod_prod=['000','111','333','555','888']
loggi=['555']
vendedor_inativo=['584']
pacotes=['888555555123888',
        '333333555584333',
        '222333555124000',
        '000111555874555',
        '111888555654777',
        '111333555123333',
        '555555555123888',
        '888333555584333',
        '111333555124000',
        '333888555584333',
        '555888555123000',
        '111888555123555',
        '888000555845333',
        '000111555874000',
        '111333555123555']

print('\n{:^70}'.format('DESTINO DE CADA PACOTE'))

for i in pacotes:
    for j in range(len(pacotes)):
        if i[3:6] == cod_reg[j]:
            destino = regiao[j]
            print(f'Pacote {i} tem como Destino: {destino}')
            break

#-------------------------------------------------------------------------------------------------

print('\n','='*70)
print('{:^70}'.format('PACOTES VÁLIDOS E INVÁLIDOS'))

validos = []
invalidos = []
for a in pacotes:
    if a[:][0:3] not in cod_reg:
        invalidos.append(a)
for b in pacotes:
    if b[:][3:6] not in cod_reg:
        invalidos.append(b)
for c in pacotes:
    if (c[:][0:3] == '111'):
        if (c[:][12:15] == '000'):
            invalidos.append(c)
for d in pacotes:
    if (d[:][9:12] in vendedor_inativo):
        invalidos.append(d)
for e in pacotes:
    if (e[:][12:15] not in cod_prod):
        invalidos.append(e)

for f in pacotes:
    if f not in invalidos:
        validos.append(f)


for val in validos:
    pcts1 = "O pacote " + val + " é válido"
    print(pcts1)

print('\n','-'*30, '\n')
for inv in invalidos:
    pcts2 = "O pacote " + inv + " náo é válido"
    print(pcts2)


#-------------------------------------------------------------------------------------------------

print('\n','='*70)
print('{:^70}'.format('PACOTES COM A ORIGEM DE REGIÃO SUL, QUE TEM BRINQUEDOS EM SEU CONTEÚDO'))

brinq = []
for f in pacotes:
    if f[:][0:3] == '000':
        if (f[:][12:15] == '888'):
            brinq.append(f)
if len(brinq) == 0:
    print('Não há nenhum pacote com origem de região Sul, que contenha brinquedos em seu conteúdo.')
else:
    print(f'Há {len(brinq)} pacotes com origem de região Sul, que contém brinquedos em seu conteúdo.')
    print('\n',brinq)


#-------------------------------------------------------------------------------------------------

print('\n','='*70)
print('{:^70}'.format('PACOTES AGRUPADOS POR REGIÃO DE DESTINO'))

centro_oeste = []
nordeste = []
norte = []
sudeste = []
sul = []

for i in validos:
    if (i[3:6] == '111'):
        centro_oeste.append(i)
    elif (i[3:6] == '333'):
        nordeste.append(i)
    elif (i[3:6] == '555'):
        norte.append(i)
    elif (i[3:6] == '888'):
        sudeste.append(i)
    elif (i[3:6] == '000'):
        sul.append(i)

print('\n Pacotes com destino a Região Centro-Oeste',
      '\n',centro_oeste)
print('\n Pacotes com destino a Região Nordeste',
      '\n',nordeste)
print('\n Pacotes com destino a Região Norte',
      '\n',norte)
print('\n Pacotes com destino a Região Sudeste',
      '\n',sudeste)
print('\n Pacotes com destino a Região Sul',
      '\n',sul)


#-------------------------------------------------------------------------------------------------

print('\n','='*70)
print('{:^70}'.format('LISTA DO NÚMERO DE PACOTES ENVIADOS POR CADA VENDEDOR'))

vend_123=[]
vend_874=[]
vend_845=[]

for i in validos:
    if (i[9:12] == '123'):
        vend_123.append(i)
    elif(i[9:12] == '874'):
        vend_874.append(i)
    elif(i[9:12] == '845'):
        vend_845.append(i)

print('\nO vendedor 123, enviou: ',len(vend_123))
print('\nO vendedor 874, enviou: ',len(vend_874))
print('\nO vendedor 845, enviou: ',len(vend_845))


#-------------------------------------------------------------------------------------------------

print('\n','='*70)
print('{:^70}'.format('RELATÓRIO DE PACOTES POR DESTINO E POR TIPO'))

print(f'\nPara a região do Centro-oeste foram enviados {len(centro_oeste)} pacotes:')
for i in centro_oeste:
    for j in range(len(produto)):
        if i[12:15] == cod_prod[j]:
            prod=produto[j]
            print(f'Pacote {i} com o produto: "{prod}"')

print(f'\nPara a região do Nordeste foram enviados {len(nordeste)} pacotes:')
for i in nordeste:
    for j in range(len(produto)):
        if i[12:15] == cod_prod[j]:
            prod=produto[j]
            print(f'Pacote {i} com o produto: "{prod}"')

print(f'\nPara a região do Norte foram enviados {len(norte)} pacotes:')
for i in norte:
    for j in range(len(produto)):
        if i[12:15] == cod_prod[j]:
            prod=produto[j]
            print(f'Pacote {i} com o produto: "{prod}"')

print(f'\nPara a região do Sudeste foram enviados {len(sudeste)} pacotes:')
for i in sudeste:
    for j in range(len(produto)):
        if i[12:15] == cod_prod[j]:
            prod=produto[j]
            print(f'Pacote {i} com o produto: "{prod}"')

print(f'\nPara a região do Sul foram enviados {len(sul)} pacotes:')
for i in sul:
    for j in range(len(produto)):
        if i[12:15] == cod_prod[j]:
            prod=produto[j]
            print(f'Pacote {i} com o produto: "{prod}"')
