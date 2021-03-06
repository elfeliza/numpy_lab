import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 4):
    f, axs = plt.subplots(2, 2, figsize=(8, 8))
    data = np.genfromtxt('s%d.csv' % i)
    print(data)
    x = [i for i in range(0, len(data))]
    plt.subplot(2, 1, 1)
    plt.plot(x, data, color='pink')
    plt.title('Raw signals', color='purple')
    new_ = np.ones(data.shape[0])
    new_[0:9] = np.cumsum(data[0:9]) / np.arange(1, 10)
    new_[9:] = np.convolve(data, np.ones(10) / 10, mode='valid')
    x1 = [i for i in range(0, len(new_))]
    plt.subplot(2, 1, 2)
    plt.plot(x1, new, color='magenta')
    plt.title('Baked signal', color='purple')
    plt.savefig('s%d.png' % i)
