import imageio as i
import numpy as np

a = np.random.randint(0,255,(512,512))

i.imwrite('myfile.png', a)

