import cv2#import lib
img = cv2.imread("C:/Users/HCT/OneDrive/Pictures/Screenshots/Screenshot 2025-06-20 071415.png")#read the source image
cv2.imshow('show.jpg',img)#image is shown
cv2.imwrite('photo.jpg',img)#save image
cv2.waitKey(10000)#image shows for 10sec
cv2.destroyAllWindows()#after that it will disappear
