#Nome string
#Categoria string
#Ativo bool

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_prass = Restaurante()
restaurante_prass.nome = 'Prass Restaurant'
restaurante_prass.categoria = 'Cafeteria Gourmet'
restaurante_peixuxa = Restaurante()

restaurantes = [restaurante_prass, restaurante_peixuxa]
print(vars(restaurante_prass))