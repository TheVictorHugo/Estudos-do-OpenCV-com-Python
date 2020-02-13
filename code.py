#A cada salto é criado um quadrado amarelo de 5x5 pixels.
# import cv2
# imagem = cv2.imread('img/lenna.png')
# for y in range(0, imagem.shape[0], 10): #percorre linhas
#     for x in range(0, imagem.shape[1], 10): #percorre colunas
#         imagem[y:y+5, x: x+5] = (0,255,255)
# cv2.imshow("Imagem modificada", imagem)
# cv2.waitKey(0)

#########################################################

#O código abaixo abre uma imagem e cria vários retângulos coloridos sobre ela.
# import cv2
# image = cv2.imread('img/lenna.png')
# #Cria um retangulo azul por toda a largura da imagem
# image[30:50, :] = (255, 0, 0)
# #Cria um quadrado vermelho
# image[100:150, 50:100] = (0, 0, 255)
# #Cria um retangulo amarelo por toda a altura da imagem
# image[:, 200:220] = (0, 255, 255)
# #Cria um retangulo verde da linha 150 a 300 nas colunas 250 a
# 350
# image[150:300, 250:350] = (0, 255, 0)
# #Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a
# 350
# image[300:400, 50:150] = (255, 255, 0)
# #Cria um quadrado branco
# image[250:350, 300:400] = (255, 255, 255)
# #Cria um quadrado preto
# image[70:100, 300: 450] = (0, 0, 0)
# cv2.imshow("Imagem alterada", image)
# cv2.imwrite("img/lenna.png", image)
# cv2.waitKey(0)

#########################################################

#Com a técnica de slicing é possível criar quadrados e retângulos, contudo, para outras
# formas geométricas é possível utilizar as funções da OpenCV, isso é útil principalmente no
# caso de desenho de círculos e textos sobre a imagem
# import numpy as np
# import cv2
# imagem = cv2.imread('img/lenna.png')
# vermelho = (0, 0, 255)
# verde = (0, 255, 0)
# azul = (255, 0, 0)
# cv2.line(imagem, (0, 0), (100, 200), verde)
# cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)
# cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
# cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)
# (X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
# for raio in range(0, 175, 15):
#     cv2.circle(imagem, (X, Y), raio, vermelho)
# cv2.imshow("Desenhando sobre a imagem", imagem)
# cv2.waitKey(0)

#########################################################

#Escreve na imagem
# import numpy as np
# import cv2
# imagem = cv2.imread('img/lenna.png')
# fonte = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(imagem,'OpenCV',(15,65), fonte,
# 2,(255,255,255),2,cv2.LINE_AA)
# cv2.imshow("Ponte", imagem)
# cv2.waitKey(0)

#########################################################

#crop da imagem
# import cv2
# imagem = cv2.imread('img/lenna2.jpg')
# recorte = imagem[100:200, 100:200]
# cv2.imshow("Recorte da imagem", recorte)
# cv2.imwrite("recorte.jpg", recorte) #salva no disco

#########################################################

#Redimensionamento / Resize
# import numpy as np
# import cv2
# img = cv2.imread('img/lenna2.jpg')
# cv2.imshow("Original", img)
# largura = img.shape[1]
# altura = img.shape[0]
# proporcao = float(altura/largura)
# largura_nova = 320 #em pixels
# altura_nova = int(largura_nova*proporcao)
# tamanho_novo = (largura_nova, altura_nova)
# img_redimensionada = cv2.resize(img,
# tamanho_novo, interpolation = cv2.INTER_AREA)
# cv2.imshow('Resultado', img_redimensionada)
# cv2.waitKey(0)

#########################################################

#Redimensionamento / Resize
# import numpy as np
# import imutils
# import cv2
# img = cv2.imread('img/lenna2.jpg')
# cv2.imshow("Original", img)
# img_redimensionada = img[::2,::2]
# cv2.imshow("Imagem redimensionada", img_redimensionada)
# cv2.waitKey(0)

#########################################################

#Espelhando uma imagem / Flip
# import cv2
# img = cv2.imread('img/lenna2.jpg')
# cv2.imshow("Original", img)
# flip_horizontal = img[::-1,:] #comando equivalente abaixo
# #flip_horizontal = cv2.flip(img, 1)
# cv2.imshow("Flip Horizontal", flip_horizontal)
# flip_vertical = img[:,::-1] #comando equivalente abaixo
# #flip_vertical = cv2.flip(img, 0)
# cv2.imshow("Flip Vertical", flip_vertical)
# flip_hv = img[::-1,::-1] #comando equivalente abaixo
# #flip_hv = cv2.flip(img, -1)
# cv2.imshow("Flip Horizontal e Vertical", flip_hv)
# cv2.waitKey(0)

#########################################################

#Rotacionando uma imagem / Rotate
# import cv2
# img = cv2.imread('img/lenna2.jpg')
# (alt, lar) = img.shape[:2] #captura altura e largura
# centro = (lar // 2, alt // 2) #acha o centro
# M = cv2.getRotationMatrix2D(centro, 30, 1.0) #30 graus
# img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
# cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
# cv2.waitKey(0)