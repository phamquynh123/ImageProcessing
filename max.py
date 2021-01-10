import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10,6)

def plot_max(origin, max): 
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(origin)
    ax[0].set_title('Origin')
    ax[0].axis('off')
    # ax[1].imshow(noisy, cmap='gray')
    # ax[1].set_title('Noisy')
    # ax[1].axis('off')
    ax[1].imshow(max)
    ax[1].set_title('Max filter')
    ax[1].axis('off')
    plt.show()

def maximumBoxFilter(noisy, n):
    # Creates the shape of the kernel
    size = (n,n)
    shape = cv2.MORPH_RECT
   
    kernel = cv2.getStructuringElement(shape, size)
     print("kernel", kernel)

    # Applies the maximum filter with kernel NxN
    #một phần tử pixel là '1' nếu ít nhất một pixel trong nhân là '1'.
    #nó làm tăng vùng trắng trong hình ảnh hoặc kích thước của đối tượng tiền cảnh tăng lên.
    imgResult = cv2.dilate(noisy, kernel, iterations=1)

    # Shows the result
    return imgResult

def main(): 
    img = cv2.imread('./img/j.jpg')
    # grayscale image is used for equalization
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # noisy
    # noisy = gray + 3*gray.std()*np.random.random(gray.shape)
    # maxfilter
    max_filter = maximumBoxFilter(img, 11)
    plot_max(img, max_filter)
if __name__ == '__main__': main()