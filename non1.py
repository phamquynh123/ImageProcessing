import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_gray(input_image, output_image):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(input_image, cmap='gray')
    ax[0].set_title('Input Image')
    ax[0].axis('off')
    ax[1].imshow(output_image, cmap='gray')
    ax[1].set_title('Histogram Equalized ')
    ax[1].axis('on')
    plt.savefig('./img/save.png')
    plt.show()
def main():
    # read an image
    img = cv2.imread('./img/1.png')
    # grayscale image is used for equalization
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # following function performs equalization on input image
    equ = cv2.equalizeHist(gray)
    # for visualizing input and output side by side
    plot_gray(gray, equ)
if __name__ == '__main__': main()