from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from skimage import io 
from skimage import filters
from skimage import img_as_float
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import random 

# IMPORT IMAGE FILE 
Tk().withdraw()
filename = askopenfilename()
imagem = io.imread(filename)

# FILTER

imagem = rgb2gray(imagem)

plt.imshow(imagem,cmap='gray')
plt.show()

imagem2 = img_as_float(imagem)


#SAVE FILE 

filename = asksaveasfilename()
file = open(filename, 'w')

file.write("Samples \n")
file.write("3 \n")
file.write("x \n")
file.write("y \n")
file.write("value \n")
for i in range(0, imagem2.shape[0]):
	for j in range (0, imagem2.shape[1]):
		aleatorio = random.random()
		if aleatorio <= 1:
			file.write(str(i)+" "+str(j)+" "+str(imagem2[i][j]) + "\n")

file.close()
