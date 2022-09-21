import cv2

image1 = cv2.imread("D:\skill.png")
window_name = "Original Image"

cv2.imshow(window_name , image1)

grey_img = cv2.cvtColor(image1 , cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussianBlur(invert , (21 , 21) , 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img , invertedblur , scale = 256.0)

cv2.imwrite("D:\sketch.png" , sketch)
image = cv2.imread("D:\sketch.png")

window_name = "Sketch Image"
cv2.imshow(window_name , image)
cv2.waitKey(0)
cv2.destoryAllWindows()
