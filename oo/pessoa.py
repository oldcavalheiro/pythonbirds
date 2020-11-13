class Pessoa:
    def __init__(self, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    p = Pessoa('luc')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'juca'  # atributo
    print(p.nome)