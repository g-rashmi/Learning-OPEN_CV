import cv2  # opencv use as cv2 in python

# Ensure the file path is correct. Use an absolute path or ensure 'imgg.png' is in the same directory.
img1 = cv2.imread(r"C:\Users\rashm\OneDrive\Desktop\cp\Learning-OPEN_CV\imgg.png")  # Use absolute path if needed
# print(img1)
 # Resize the image
#img1 = cv2.resize(img1, (1280, 500))  # width=1280, height=500
 # Display the image
cv2.imshow("original", img1)  # image ko dekhne


#image 3channel image and gray scale ; 

#imread accept two parameter one is location of parameter and other is number(integer decide image read in which way bydefault :1);
 
#loads image in gray scale ; 
img2 = cv2.imread(r"C:\Users\rashm\OneDrive\Desktop\cp\Learning-OPEN_CV\imgg.png",0) ;#by adding 0 here image converted to gray scale
cv2.imshow("grayscale image", img2) ;


#loads image as such as original color saturation quite high(alpha channels); 
img3 = cv2.imread(r"C:\Users\rashm\OneDrive\Desktop\cp\Learning-OPEN_CV\imgg.png",-1) ;
cv2.imshow("highsaturation image", img3) ;
# Wait for a key press
# cv2.waitKey()  # Correct function call (capital K)  Close all OpenCV windows
# cv2.destroyAllWindows() 
cv2.waitKey() #visualization ko control krta hai (like image show ko), bydefult zero hota hai like statiscally image display hoti rhegii , (u can write timer like 3000ms->now 3sec image hold) ; 
cv2.destroyAllWindows() #jitni memory use kii like image load , to free all memory as when code terminate ; 