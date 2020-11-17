from PIL import Image

filename = "test.png"
img = Image.open(filename)
img.save("test.ico")