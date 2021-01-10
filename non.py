import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_cv_img(input_image, output_image):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    ax[0].set_title('Input Image')
    ax[0].axis('off')
    ax[1].imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
    ax[1].set_title('Gaussian Blurred')
    ax[1].axis('off')
    plt.show()
def main():
    img = cv2.imread('./img/1.png')
    kernel_size = (5,5)
    blur = cv2.GaussianBlur(img,(5,5),0)
    plot_cv_img(img, blur)
if __name__ == '__main__': main()