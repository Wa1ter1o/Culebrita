import pygame
import random
import pygame.time as tiempo
import sys
import pygame.locals as globales
import pygame.event as eventos

class celda():

    def __init__(self, pos):
        self.pos = pos

pygame.init()
pygame.font.init()

ancho, alto = 771, 771

fps = 60

reloj = tiempo.Clock()

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("CULEBRITA")

#variable del juego

culebrita = []

#definimos el tamaño del arreglo o tablero de juego
tamanoDeMatríz = (15, 15)
matriz = []
#tamaño de cada celda en tablero de juego
tamanoDeCelda = (50, 50)
#fijamos velocidad inicial y el aumento de velocidad por cada punto (pasos por segundo)
velocidadInicial = 5
incrementoVelocidad = 0.1
velocidad = velocidadInicial
espera = 1000 / velocidad
ultimoMovimiento = 0

direccion = ""

agregarCelda = False

#modos de pantalla
inicio = True
jugando = False
pausa = False
fin = False

#inicializamos matríz
for j in range (tamanoDeMatríz[1]):
    matriz.append([])
    for i in range (tamanoDeMatríz[0]):
        matriz[j].append(0)


def salir():
    pygame.font.quit()
    pygame.quit()
    sys.exit()

def dibujarFondo():

    for j, fila in enumerate(matriz):
        for i in range (len(fila)):
            pygame.draw.rect(ventana,(50, 50, 50), (10, 10, tamanoDeCelda[0]*(i+1), tamanoDeCelda[1]*(j+1)), 1)

    pygame.draw.rect(ventana, (255, 255, 255), (10, 10, tamanoDeMatríz[0] * tamanoDeCelda[0], tamanoDeMatríz[1] * tamanoDeCelda[1]), 1)



def dibujarTexto(estado):

    if inicio:
        altoFuente = 100
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'CULEBRITA'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0),
                         ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20 - altoFuente * 1.5,
                           centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2 - altoFuente * 1.5))

        altoFuente = 30
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'Juega con las flechas'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0), ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20 + altoFuente * 1,
                                               centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2 + altoFuente * 1))

        altoFuente = 25
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'Pausa el juego con "ESPACIO"'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0),
                         ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20 + altoFuente * 3.5,
                           centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2 + altoFuente * 3.5))

        altoFuente = 30
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'Pulsa "ESPACIO" para iniciar el juego'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0),
                         ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20 + altoFuente * 6,
                           centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2 + altoFuente * 6))

    if pausa:
        altoFuente = 50
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'PAUSA'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0), ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20,
                                               centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2))

    elif fin:
        altoFuente = 100
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'OUCH'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0), ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20 - 100,
                                               centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2 - 100))

        altoFuente = 30
        fuente = pygame.font.SysFont("OCR A Extended", altoFuente)
        texto = 'Pulsa "ESPACIO" para ir al inicio'
        img = fuente.render(texto, True, (255, 255, 255))
        centro = img.get_rect()[2] / 2
        pygame.draw.rect(ventana, (0, 0, 0),
                         ((ancho / 2 - centro - 20, alto / 2 - altoFuente / 2 - 20 + altoFuente * 6,
                           centro * 2 + 40, altoFuente + 40)))
        ventana.blit(img, (ancho / 2 - centro, alto / 2 - altoFuente / 2 + altoFuente * 6))


def dibujarMatriz():

    for j, fila in enumerate( matriz):
        for i, celda in enumerate(fila):
            if celda == 1:
                xCentro = 10 + ((i) * tamanoDeCelda[0]) + tamanoDeCelda[0] / 2
                yCentro = 10 + ((j) * tamanoDeCelda[1]) + tamanoDeCelda[1] / 2
                pygame.draw.circle(ventana,(250, 250, 250), (xCentro, yCentro),
                                   (tamanoDeCelda[0]/2)-(tamanoDeCelda[0] * 0.1), int(tamanoDeCelda[0] * 0.1))

            elif celda == 3:
                xCentro = 10 + ((i) * tamanoDeCelda[0]) + tamanoDeCelda[0] / 2
                yCentro = 10 + ((j) * tamanoDeCelda[1]) + tamanoDeCelda[1] / 2
                pygame.draw.circle(ventana,(250, 250, 250), (xCentro, yCentro), (tamanoDeCelda[0]/2)/2)

        xCentro = 10 + ((culebrita[0].pos[0]) * tamanoDeCelda[0]) + tamanoDeCelda[0] / 2
        yCentro = 10 + ((culebrita[0].pos[1]) * tamanoDeCelda[1]) + tamanoDeCelda[1] / 2
        pygame.draw.circle(ventana, (125, 125, 125), (xCentro,yCentro), tamanoDeCelda[0] * 0.1, int(tamanoDeCelda[0] * 0.05))

def agregarComida():
    global matriz

    celdasLibres = []
    for j, fila in enumerate(matriz):
        for i, celda  in enumerate(fila):
            if (matriz[j])[i] == 0:
                celdasLibres.append([i, j])
    if len(celdasLibres) > 0:
        comida = celdasLibres[random.randint(0, len(celdasLibres)-1)]
        (matriz[comida[1]])[comida[0]] = 3

def avanzar():
    global matriz, culebrita, agregarCelda, jugando, pausa, fin, velocidad

    comida = False

    posAnt = [culebrita[0].pos[0], culebrita[0].pos[1]]

    posCabeza = posAnt

    if direccion == "arriba" :
        if posCabeza[1] == 0 or matriz[posCabeza[1]-1][posCabeza[0]] == 1:
            fin = True
            jugando = False
        else:
            culebrita[0].pos[1] -= 1

    elif direccion == "abajo" :
        if posCabeza[1] == tamanoDeMatríz[1]-1 or matriz[posCabeza[1] + 1][posCabeza[0]] == 1:
            fin = True
            jugando = False
        else:
            culebrita[0].pos[1] += 1

    elif direccion == "izquierda":
        if posCabeza[0] == 0 or matriz[posCabeza[1]][posCabeza[0]-1] == 1:
            fin = True
            jugando = False
        else:
            culebrita[0].pos[0] -= 1

    elif direccion == "derecha":
        if posCabeza[0] == tamanoDeMatríz[0]-1 or matriz[posCabeza[1]][posCabeza[0]+1] == 1:
            fin = True
            jugando = False
        else:
            culebrita[0].pos[0] += 1


    if jugando and not pausa and not fin:

        #asignando datos a matríz
        matriz[posAnt[1]][posAnt[0]] = 0
        if matriz[culebrita[0].pos[1]][culebrita[0].pos[0]] == 3:
            agregarCelda = True
            velocidad = velocidad + incrementoVelocidad
            comida = True
        matriz[culebrita[0].pos[1]][culebrita[0].pos[0]] = 1


        cola = [culebrita[-1].pos[0], culebrita[-1].pos[1]]

        if len(culebrita) > 1:

            for i, parte in enumerate(culebrita):
                if i > 0:
                    posAnt2 = [parte.pos[0], parte.pos[1]]
                    parte.pos = [posAnt[0], posAnt[1]]
                    posAnt = [posAnt2[0], posAnt2[1]]

                    matriz[posAnt[1]][posAnt[0]] = 0
                    matriz[parte.pos[1]][parte.pos[0]] = 1

        if agregarCelda:
            culebrita.append(celda([cola[0], cola[1]]))
            matriz[cola[1]][cola[0]] = 1
            agregarCelda = False

    if comida:
        agregarComida()

def inicializar():
    global inicio, jugando, pausa, fin, matriz, culebrita, velocidad, espera

    inicio = True
    jugando = False
    pausa = False
    fin = False

    culebrita = []

    for j, fila in enumerate(matriz):
        for i, celda in enumerate(fila):
            matriz[j][i] = 0

    velocidad = velocidadInicial
    espera = 1000/velocidad


if __name__ == "__main__" :

    while True:

        micros = tiempo.get_ticks()
        ventana.fill((0,0,0))
        dibujarFondo()

        for evento in eventos.get():
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:

                    if jugando:
                        pausa = not pausa
                        fps = 15

                    if inicio:
                        jugando = True
                        inicio = False
                        culebrita.append(celda([int(tamanoDeMatríz[0]/2), int(tamanoDeMatríz[1]/2)]))
                        (matriz[(culebrita[0].pos)[1]])[culebrita[0].pos[0]] = 1
                        agregarComida()
                        fps = 60

                    if fin:
                        inicio = True
                        inicializar()


                if len(culebrita) == 1 :
                    if evento.key == pygame.K_UP:
                        direccion = "arriba"
                    if evento.key == pygame.K_DOWN:
                        direccion = "abajo"
                    if evento.key == pygame.K_LEFT:
                        direccion = "izquierda"
                    if evento.key == pygame.K_RIGHT:
                        direccion = "derecha"
                elif len(culebrita) > 1 :
                    if evento.key == pygame.K_UP:

                        if culebrita[1].pos[1] >=  culebrita[0].pos[1]:
                            direccion = "arriba"
                    if evento.key == pygame.K_DOWN:

                        if culebrita[1].pos[1] <= culebrita[0].pos[1]:
                            direccion = "abajo"
                    if evento.key == pygame.K_LEFT:

                        if culebrita[1].pos[0] >= culebrita[0].pos[0]:
                            direccion = "izquierda"
                    if evento.key == pygame.K_RIGHT:

                        if culebrita[1].pos[0] <= culebrita[0].pos[0]:
                            direccion = "derecha"
                else:
                    direccion = ""

                if evento.key == pygame.K_ESCAPE:
                    salir()

            if evento.type == globales.QUIT:
                salir()

        if inicio:
            dibujarTexto("inicio")

        if jugando:
            fps = 60
            espera = 1000 / velocidad
            dibujarMatriz()
            if not pausa:
                if micros > ultimoMovimiento + espera:
                    avanzar()
                    ultimoMovimiento = micros
            else:
                dibujarTexto("pausa")

        if fin:
            dibujarMatriz()
            dibujarTexto("fin")

            fps = 15

        reloj.tick(fps)
        pygame.display.update()