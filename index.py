import cv2  # opencv use as cv2 in python

# Ensure the file path is correct. Use an absolute path or ensure 'imgg.png' is in the same directory.
img1 = cv2.imread(r"C:\Users\rashm\OneDrive\Desktop\cp\Learning-OPEN_CV\imgg.png")  # Use absolute path if needed

# print(img1)

    # Resize the image
#img1 = cv2.resize(img1, (1280, 500))  # width=1280, height=500

    # Display the image
cv2.imshow("original", img1)  # image ko dekhne

    # Wait for a key press
# cv2.waitKey()  # Correct function call (capital K)

#     # Close all OpenCV windows
# cv2.destroyAllWindows() 

#image 3channel image and gray scale ; 
#imread accept two parameter one is location of parameter and other is number(integer decide image read in which way bydefault :1); 
img2 = cv2.imread(r"C:\Users\rashm\OneDrive\Desktop\cp\Learning-OPEN_CV\imgg.png",0) ;#by adding 0 here image converted to gray scale

cv2.imshow("grayscale image", img2) ;

cv2.waitKey()

cv2.destroyAllWindows() 