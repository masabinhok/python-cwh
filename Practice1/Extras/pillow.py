from PIL import Image 

im = Image.open("sabin.png") #opened the image file
print(im.format, im.size, im.mode) #prints the format, size and mode of the image file
im.show() #open the image file in the desktop

