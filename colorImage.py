# Taller 1 -- colorImage.py
# Leidy Carolina Pulido Feo
# Procesamiento de Imágenes y visión

import numpy as np
import cv2


class colorImage:   # Creación de la clase colorImage

    def __init__(self, ruta):    # Constructor -- Recibe, carga y almacena la imagen
        self.ruta = ruta
        self.Image = cv2.imread(self.ruta)  # Carga la imagen de la dirección ruta y la almacena en la valiable image

    def displayProperties(self):   # Método displayProperties
        self.altura, self.ancho, self.canales = self.Image.shape    # Tamaño de la imagen
        print('La altura de la imagen es:', self.altura)  # Muestra al usuario la altura de la imagen
        print('El ancho de la imagen es:', self.ancho)  # Muestra al usuario el ancho de la imagen

    def makeGray(self):     # Método makeGray
        self.Image_Gray = cv2.cvtColor(self.Image, cv2.COLOR_BGR2GRAY)   # Cambio de la imagen original a espacio de
        # grises
        cv2.imshow('Imagen en Grises', self.Image_Gray)  # Mostrar una imagen en una ventana; la ventana se ajusta
        # automáticamente al tamaño de la imagen.
        cv2.waitKey(0)  # Muestra la imagen con t=0 -> continuo

    def colorizeRGB(self, color):    # Método colorizeRGB, recibe string del color del canal deseado
        self.color = color

        if self.color == 'red':  # Imagen Rojiza
            self.Image_Red = np.copy(self.Image)    # Copia de la imagen original para no afectarla a "Image_Red"
            self.Image_Red[:, :, 0] = 0  # Elimina componente azul de la imagen
            self.Image_Red[:, :, 1] = 0  # Elimina componente verde de la imagen
            self.Image_Red[:, :, 2] = self.Image_Gray   # Asigna imagen en grises al canal rojo
            cv2.imshow('Imagen Rojiza', self.Image_Red)  # Mostrar una imagen en una ventana; la ventana se ajusta
            # automáticamente al tamaño de la imagen.
            cv2.waitKey(0)  # Muestra la imagen con t=0 -> continuo

        elif self.color == 'green':  # Imagen Verdosa
            self.Image_Green = np.copy(self.Image)  # Copia de la imagen original para no afectarla a "Image_Green"
            self.Image_Green[:, :, 0] = 0  # Elimina componente azul de la imagen
            self.Image_Green[:, :, 1] = self.Image_Gray   # Asigna imagen en grises al canal verde
            self.Image_Green[:, :, 2] = 0   # Elimina componente roja de la imagen
            cv2.imshow('Imagen Verdoza', self.Image_Green)  # Mostrar una imagen en una ventana; la ventana se ajusta
            # automáticamente al tamaño de la imagen.
            cv2.waitKey(0)  # Muestra la imagen con t=0 -> continuo

        elif self.color == 'bluel':  # Imagen Azulosa
            self.Image_Blue = np.copy(self.Image)   # Copia de la imagen original para no afectarla a "Image_Blue"
            self.Image_Blue[:, :, 0] = self.Image_Gray    # Asigna imagen en grises al canal azul
            self.Image_Blue[:, :, 1] = 0    # Elimina componente verde de la imagen
            self.Image_Blue[:, :, 2] = 0    # Elimina componente roja de la imagen
            cv2.imshow('Imagen azuloza', self.Image_Blue)  # Mostrar una imagen en una ventana; la ventana se ajusta
            # automáticamente al tamaño de la imagen.
            cv2.waitKey(0)  # Muestra la imagen con t=0 -> continuo

        else:  # En caso de error en la selección de color
            print('No determinó correctamente el color en el que desea ver la imagen. Las opciones son: ("red", "green", "bluel")')

    def makeHue(self):  # Método makeHue
        self.Image_HSV = cv2.cvtColor(self.Image, cv2.COLOR_BGR2HSV)    # Cambio de la imagen original a espacio de color HSV
        self.Image_HSV[:, :, 1] = 255   # Saturation = 255
        self.Image_HSV[:, :, 2] = 255   # Value = 255
        self.Image_RGB_Hue = cv2.cvtColor(self.Image_HSV, cv2.COLOR_HSV2BGR)  # Cambio de la imagen HSV a espacio de color RGB
        cv2.imshow('Imagen Hue', self.Image_RGB_Hue)  # Mostrar una imagen en una ventana; la ventana se ajusta
        # automáticamente al tamaño de la imagen.
        cv2.waitKey(0)  # Muestra la imagen con t=0 -> continuo
