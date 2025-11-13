import imageio.v3 as dv
from PIL import Image
import numpy as np   

filenames = ['1.png', '2.png', '3.png', '4.png']
images = []

base_img = Image.open(filenames[0])
width, height = base_img.size

for filename in filenames:
    img = Image.open(filename).resize((width, height))
    img = np.array(img)   
    images.append(img)

dv.imwrite('team.gif', images, duration=500, loop=0)
