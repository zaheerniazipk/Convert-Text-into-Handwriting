import pywhatkit as kit
import cv2


# Convert the given str into Handwriting and saved as a image file with color mode
text = input("Enter your Text: ")
kit.text_to_handwriting(text, save_to="handwriting.png")

# cv2.imread() method loads an image from the specified file
img = cv2.imread('./handwriting.png', 1)

# cv2.imshow() method display an image in a specified Window
cv2.imshow("Text to Handwriting", img)


# cv2.waitKey() allows us to wait for a specific time in milliseconds
# After pressing any key the window is automatically closed
cv2.waitKey(0)          # 0 is used for infinite time -->


# cv2.destroyAllWindows() simply destroys all the windows we created
cv2.destroyAllWindows()
