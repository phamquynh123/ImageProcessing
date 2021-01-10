import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy import ndimage
plt.rcParams['figure.figsize'] = (10,6)

def plot_gray(origin, median): 
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(origin, cmap=None)
    ax[0].set_title('Origin')
    ax[0].axis('off')
    # ax[1].imshow(noisy, cmap='gray')
    # ax[1].set_title('Noisy')
    # ax[1].axis('off')
    ax[1].imshow(median, cmap=None)
    ax[1].set_title('Median')
    ax[1].axis('off')
    plt.show()
def main(): 
    img = cv2.imread('./img/median.jpg')
    # grayscale image is used for equalization
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # noisy
    # noisy = gray + 4*gray.std()*np.random.random(gray.shape)
    # medians
    med_denoised = ndimage.median_filter(img, 3)
    med_denoised = ndimage.median_filter(med_denoised, 3)
    plot_gray(img, med_denoised)
if __name__ == '__main__': main()