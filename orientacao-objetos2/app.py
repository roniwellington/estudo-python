from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)
#restaurante_mexicano = Restaurante('Mexicano Food', 'Mexicana')
#restaurante_japones = Restaurante('Japa', 'Japonesa')

#restaurante_mexicano.alternar_estado()


def main ():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()