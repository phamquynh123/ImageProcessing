import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10,6)

def plot_gray(origin, min): 
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow(origin, cmap=None)
    ax[0].set_title('Origin')
    ax[0].axis('off')
    # ax[1].imshow(noisy, cmap='gray')
    # ax[1].set_title('Noisy')
    # ax[1].axis('off')
    ax[1].imshow(min, cmap=None)
    ax[1].set_title('Min filter')
    ax[1].axis('off')
    plt.show()

def minimumBoxFilter(noisy, n):
    # Creates the shape of the kernel
    size = (n,n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)

    # Applies the maximum filter with kernel NxN
    #một phần tử pixel là '1' nếu ít nhất một pixel trong nhân là '1'.
    #nó làm tăng vùng trắng trong hình ảnh hoặc kích thước của đối tượng tiền cảnh tăng lên.
    imgResult = cv2.erode(noisy, kernel, iterations=1)

    # Shows the result
    return imgResult

def main(): 
    img = cv2.imread('./img/j.jpg')
    # grayscale image is used for equalization
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # noisy
    # noisy = gray + 3*gray.std()*np.random.random(gray.shape)
    # minilter
    min_filter = minimumBoxFilter(img, 5)
    plot_gray(img, min_filter)
if __name__ == '__main__': main()

# Thay đổii ma trận
# Lọc  mã x bằng đa mức xám có gì khác min max => in mặt nạ ra
# ảnh nhị phân áp dụng lọc min, max ntn vs co dãn trên nhịn phân
# j lúc lọc min lại to ra lọc max lại thon đi  
# j ảnh đa mức xảm, ảnh xám hay nhị phân. 