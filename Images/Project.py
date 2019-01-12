import matplotlib.pyplot as plt
import os.path
import PIL


'''Read the image data'''

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'pigeon.png')
img = plt.imread(filename)

'''Show the image data'''

fig, ax = plt.subplots(1, 3)

            
ax[0].imshow(img, interpolation='none')
ax[0].set_title('Haters be sayin otherwise')

img2=img
ax[2].imshow(img2, interpolation= 'none')
ax[2].plot(188,165,'ro')
ax[2].plot(232,165,'ro')
ax[2].set_title('Burn em up')

img3 = PIL.Image.open(filename)
grayImage = img3.convert('L')

ax[1].imshow(grayImage, cmap = plt.get_cmap('gray'))
ax[1].set_title('Proven since 18th century')

fig.show()

