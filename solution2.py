import matplotlib.pyplot as plt
import numpy as np
from math import pi, exp

def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return


def filter(img, window_size=3):
    img2 = np.zeros_like(img)
    # kernel = get_kernel(window_size)
    sigma = 5
    window_size = 3 * sigma
    kernel = np.ones((window_size, window_size))
    p = window_size//2
    for i in range(window_size):
        for j in range(window_size):
            kernel[i][j] = (1 / ((2*pi)**(1/2)*sigma)) * exp(-((i - p)*(i - p) + (j - p)*(j - p)) / (2*sigma*sigma))
    kernel/=kernel.sum()
    
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2


def main():
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img)

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()