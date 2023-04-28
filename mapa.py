import math

mapa = [
    {
        'id': 'P1',
        'nome': 'Prefeitura Municipal de Nazaré',
        'latitude': -6974326217295570,
        'longitude': -426716956375021,
        'destinos': ['P2', 'P14'],
        'distancia': [79.73, 81.43]
    },
    {
        'id': 'P2',
        'nome': 'E. Euphoria MF',
        'latitude': -6974376866587700,
        'longitude': -42672428901739300,
        'destinos': ['P1', 'P3', 'P13'],
        'distancia': [79.73, 33.63, 99.86]
    },
    {
        'id': 'P3',
        'nome': 'Mercadinho Permissão',
        'latitude': -69742268115234500,
        'longitude': -4267269771744400,
        'destinos': ['P2', 'P4', 'P13'],
        'distancia': [33.63, 85.60, 88.05]
    },
    {
        'id': 'P4',
        'nome': 'Drogaria Pinheiro',
        'latitude': -69740623342748500,
        'longitude': -4267349040610860,
        'destinos': ['P3', 'P5', 'P12'],
        'distancia': [85.60, 67.82, 97.84]
    },
    {
        'id': 'P5',
        'nome': 'E. Reis Eletromóveis',
        'latitude': -697391822945540,
        'longitude': -4267411953301720,
        'destinos': ['P4', 'P6', 'P11'],
        'distancia': [67.82, 115.03, 99.48]
    },
    {
        'id': 'P6',
        'nome': 'Unidade Escolar João Leal',
        'latitude': -6973667967106020,
        'longitude': -4267512804359060,
        'destinos': ['P5', 'P7'],
        'distancia': [115.03, 105.64]
    },
    {
        'id': 'P7',
        'nome': 'E. R. Pedro Francisco',
        'latitude': -69727254885478900,
        'longitude': -4267492419570870,
        'destinos': ['P6', 'P8', 'P11'],
        'distancia': [105.64, 72.19, 115.62]
    },
    {
        'id': 'P8',
        'nome': 'E. Multmercado Central',
        'latitude': -6972109179581230,
        'longitude': -42674760539506000,
        'destinos': ['P7', 'P9'],
        'distancia': [72.19, 17.72]
    },
    {
        'id': 'P9',
        'nome': 'Multmercado Central',
        'latitude': -697217562638943,
        'longitude': -4267462675796990,
        'destinos': ['P8', 'P10'],
        'distancia': [17.72, 100.78]
    },
    {
        'id' : 'P11',
        'nome' : 'E. Salão do Reino T. Jeová',
        'latitude' : -6973044398994420,
        'longitude' : -426738901273818,
        'destinos' : ['P5', 'P7', 'P10', 'P12'],
        'distancia' : [99, 115, 71, 75]
    },
    {
        'id' : 'P12',
        'nome' : 'E. AV Mafrense',
        'latitude' : -6973212580128170,
        'longitude' : -42673266407271900,
        'destinos' : ['P4', 'P11', 'P13', 'P16'],
        'distancia' : [97, 75, 102, 106]
    },
    {
        'id' : 'P13',
        'nome' : 'Esquina Lucivaldo Bebidas',
        'latitude' : -6973528084171570,
        'longitude' : -4267232504772440,
        'destinos' : ['P2', 'P3', 'P12', 'PP14', 'P15'],
        'distancia' : [99, 88, 102, 56, 73]
    },
    {
        'id' : 'P14',
        'nome' : 'Secretaria M. de Educação',
        'latitude' : -6973714742306080,
        'longitude' : -426718684983636,
        'destinos' : ['P1', 'P13', 'P15'],
        'distancia' : [81, 56, 89]
    },
    {
        'id' : 'P15',
        'nome' : 'E. Brocados e Famintos',
        'latitude' : -6972951961913790,
        'longitude' : -4267213169100110,
        'destinos' : ['P13', 'P14', 'P16'],
        'distancia' : [73, 89, 119]
    },
    {
        'id' : 'P16',
        'nome' : 'Radio Liderança FM',
        'latitude' : -6972292384296360,
        'longitude' : -4267306987642810,
        'destinos' : ['P12', 'P15', 'P17'],
        'distancia' : [106, 119, 86]
    },
    {
        'id' : 'P17',
        'nome' : 'E. Rui Barbosa',
        'latitude' : -6971776792521840,
        'longitude' : -42673612919719100,
        'destinos' : ['P10', 'P16'],
        'distancia' : [76, 86]
    }
]

def ligar_pontos(pa,pb,dist):
    pa['destinos'].append(pb)
    pb['destinos'].append(pa)
    pa['distancia'].append(dist)
    pb['distancia'].append(dist)

ligar_pontos(mapa[0], mapa[1], 79.73)


def linha_reta(pa,pb):
    circTerra = 40075000
    dy = (pa['latitude'] - pb['latitude'])*circTerra/360

    fatorP1 = math.cos(math.radians(pa['latitude']))
    fatorP2 = math.cos(math.radians(pb['latitude']))
    dx = (pa['longitude'] * fatorP1 - pb['longitude'] * fatorP2) * circTerra/360

    dist = math.sqrt(dx ** 2 + dy ** 2)
    return dist

linha_reta(mapa[0],mapa[1])

print(mapa[0]['destinos'])