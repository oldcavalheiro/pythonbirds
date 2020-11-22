"""Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1.Motor
2.Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1.Atributo de dado velocidade
2.Método acelerar, que deverá incremetar a velocidade de uma unidade
3.Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1.valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2.Método girar_a_direita
3.Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'oeste'
"""

NORTE = 'norte'  # convenção usa letras maiusculas para váriavel constante
SUL = 'sul'
LESTE = 'leste'
OESTE = 'oeste'


class Carro:

    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


class Direcao:
    rotacao_esquerda_dct = {NORTE: OESTE,
                            OESTE: SUL,
                            SUL: LESTE,
                            LESTE: NORTE}  # criando direção com dicionário

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):  # criando direção com if
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE

    def girar_a_esquerda(self):
        self.valor = self.rotacao_esquerda_dct[self.valor]


class Motor:  # criação de atributos no __init__
    def __init__(self):
        self.velocidade = 0  # atributo de dado

    def acelerar(self):
        self.velocidade = self.velocidade + 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)  # max retorna sempre o valor maior
