# Taller 1 -- main.py
# Leidy Carolina Pulido Feo
# Procesamiento de Imágenes y visión

import numpy as np
from colorImage import * # Importa la clase "colorImage"
import cv2
import os

if __name__ == '__main__':

    ruta = input('Introducir la ruta de la imagen que desea trabajar:')     # Variable que almacena la ruta de la imagen a trabajar
    New_Image = colorImage(ruta)    # New_Image es la instancia de la clase colorImage
    #J:/Proc.Imagenes/Imagenlena/lena.png
    New_Image.displayProperties()   # Método de ancho y alto de la imagen
    New_Image.makeGray()    # Método de versión en gris de la imagen
    New_Image.colorizeRGB('red')    # Método de verisión colorizada de la imagen. Se debe escribir 'red', 'green' o 'bluel'
    New_Image.makeHue() # Método que resalta los tonos (Hue) de la imagen
