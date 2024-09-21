#IMAGE CONVERSION PROJECT COLORED IMAGE INTO GRAYSCALE ; 
import cv2
#path=input("enter the path of image");
#Now read image ; r->raw string
path=r"C:\Users\rashm\OneDrive\Desktop\cp\Learning-OPEN_CV\imgg.png"
img1= cv2.imread(path,0)
img1=cv2.flip(img1,0) #accept 3 parameters 0,-1,1;
cv2.imshow("converted image",img1)
k=cv2.waitKey(0);
if k==ord("s") :#now it will save whenever press s
    cv2.imwrite("C:\\Users\\rashm\\OneDrive\\Desktop\\cp\\Learning-OPEN_CV\\output.jpg",img1) ; 

    cv2.destroyAllWindows() ;