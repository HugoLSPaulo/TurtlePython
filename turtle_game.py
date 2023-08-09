
from turtle import Turtle

#inicializar
t = Turtle()

#definir a velocidade
t.speed(1)

while True:
    direcao = input('Para qual direcao devemos ir ?  "f:frente" ou "t:tras" ')
    if direcao == "f" or direcao == "frente":
        distancia = int(input('Quantos pixels devemos movimentar para frente ?: '))
        movimentar_para_lado = input('Rotacionar para d:direita, e:esquerda n:nao rotacionar: ')
        
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar ?: '))
            t.right(angulo)

        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar ?: '))
            t.left(angulo)
        t.forward(distancia)
    
    if direcao == 't' or direcao == 'tras':
        distancia = int(input('Quantos pixels devemos movimentar para tras ?: '))
        movimentar_para_lado = input('Rotacionar para d:direita, e:esquerda n:nao rotacionar: ')
        
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar ?: '))
            t.right(angulo)

        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar ?: '))
            t.left(angulo)
        t.backward(distancia)

    resposta = input('Continuar andando? ')

    if resposta not in ('sim','s'):
        break 





