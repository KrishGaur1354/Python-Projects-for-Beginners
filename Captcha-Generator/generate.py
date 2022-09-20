from captcha.image import ImageCaptcha

image = ImageCaptcha(width = 300, height = 100)

captcha_text = input("Enter Captcha Text : ")
data = image.generate(captcha_text)

image.write(captcha_text, "D:\CS\generate1.png")

from PIL import Image
Image.open("D:\CS\generate1.png")
