import numpy as np
import matplotlib.pyplot as plt
import cv2

def point_operation(img, K, L):
    img = np.asarray(img, dtype=np.float)
    img = img*K + L
    img[img > 255] = 255
    img[img < 0] = 0
    return np.asarray(img, dtype = np.int)
    
def main():
    img = cv2.imread('./img/1.png')
    print("img", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("3")
    # k = 0.5, l = 0
    out1 = point_operation(gray, 0.5, 0)
    # k = 1., l = 10
    out2 = point_operation(gray, 1., 10)
    # k = 0.8, l = 15
    out3 = point_operation(gray, 0.7, 2)
    res = np.hstack([gray,out1, out2, out3])
    plt.imshow(res, cmap='gray')
    print("jhfjff")
    plt.axis('off')
    plt.show()
if __name__ == '__main__': main()