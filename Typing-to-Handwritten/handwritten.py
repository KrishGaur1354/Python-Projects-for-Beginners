import pywhatkit as kit
import cv2
Handwritten=input("Enter your text to be Written as Handwriting: ")
kit.text_to_handwriting(Handwritten, save_to="hand.png")
img = cv2.imread("hand.png")
cv2.imshow("Python Coding", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
