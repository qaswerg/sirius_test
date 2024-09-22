from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    img = Image.open('memes/mem2adfs.jpg')

    plt.imshow(img)
    plt.axis('off')
    plt.show()