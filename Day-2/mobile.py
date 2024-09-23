#in this we learn how to capture video using mobile 
#capturing video through different source like mobile cam
#in mobilee download ipwebcam
#click on start serveer then camera open 
#iss app ke through camera ko browser main access kr skte hai so path ko videowriter main pass kr skte hai 

#write the ip address on browser mention in the mobile after the camera open ;
# after click on js ,now u can see ur video is accessing in browser ; 
#ur mobile and laptop need to connect with same network ;



import cv2 ;
#connect ur laptop and android device with same network rither wifi 

camera="http://192.168.85.109:8080/video" #ip_address /video
cap=cv2.VideoCapture(0);

cap.open(camera)
fourcc=cv2.VideoWriter_fourcc(*"XVID")

output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0);

while (cap.isOpened()):
        ret,frame=cap.read();
        if ret==True:
              cv2.imshow("colorframe",frame);
              output.write(frame)
              if cv2.waitKey(1)&0xFF==ord('s'):
                  break;

cap.release() # release everything when work is done 
output.release()
cv2.destroyAllWindows()