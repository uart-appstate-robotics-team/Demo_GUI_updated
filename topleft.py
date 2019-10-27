import uart
import numpy as np
from PIL import Image


im =Image.open("allblack.jpeg")

lis = [True, True, False, False, False]

colors = {'red':[255,0,0]}

uart = uart.uart(np.array(im),colors,lis)

#uart.draw_line3([(0,0), (0,200), (200,200),(200,0),(0,0)])
#uart.draw_line3([(100,200), (100,275)])

uart.draw_line3([(100,100)])
