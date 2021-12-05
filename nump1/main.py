from PIL import Image
import numpy as np

file = ['l1.jpg', 'l2.jpg', 'l3.jpg']

for i in range(1, 4):
    img = Image.open('l%d.jpg' % i)
    data = np.array(img)
    min_ = np.min(data)
    max_ = np.max(data)
    LUT = np.zeros(256, dtype=np.uint8)
    LUT[min_:max_ + 1] = np.linspace(start=0, stop=255, num=(max_ - min_) + 1)
    Image.fromarray(LUT[data]).save('result%d.png' % i)

