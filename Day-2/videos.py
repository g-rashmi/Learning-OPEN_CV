import cv2;  
# #videocapture takes path and u can access video ;
# # cap is videocapture object in which u read the video ;  
# cap=cv2.VideoCapture(r"C:\Users\rashm\Downloads\WhatsApp Video 2023-02-01 at 9.02.50 PM.mp4"); 
# #cap is object of video
# print(cap);
# #in this reading frames (img) one by one of whole video ;
# while True:
#     ret,frame=cap.read() ; #showing img;(this read return two value one is img and other is boolean )
#     frame=cv2.resize(frame,(700,300)); #to resize the frames ; 
#     #to convert to grayscale ;
#     #while in img we simply pass 0 in imread func but in video this is how convert to grayscale 
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame",frame); 
#     cv2.imshow("gray",gray);
#     # as we know video is collection of imges so image of video is showing ; 
#     # # jitni wait key kii value km hogi utni video playsppec fast as in this each frame duration  is pass like there pausing period  ; 
#     k= cv2.waitKey(23); # these like if any key is press ; video exit 
#     if k== ord():
#       break ;

# cap.release(); # as cap capture video so need to release;

# cv2.destroyAllWindows();  
#about we read video from memory and perform some operation


 # NOW WE'LL LEARN TO CAPTURE VIDEO FROM WEBCAM AND SAVE INTO MEMORY 

cap=cv2.VideoCapture(0) ;
#0 means internal webcam #1 for external webcam ; 
#this opened fn check whether webcam is open or not : it run untill web open cam and also throught ret it get whether we are getting frames or not if we are getting frames we are showing them 
# while cap.isOpened():
#    ret,frame=cap.read();
#    if ret==True: 
#        # frame = cv2.resize(frame, (300, 100))
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow("frame", frame)
#         cv2.imshow("gray", gray)
#         k = cv2.waitKey(23)
#         if k == ord("s"):
#             break
# cap.release();
# cv2.destroyAllWindows();  
#above one is for capture video through web cam but now how to save
#we use VideoWriter
#DIVX ,XVID,MJPG,X264,WMV1,WMV2;
fourcc=cv2.VideoWriter_fourcc(*"XVID") 

#IT contain 4 parameters name,codec,fps,resolution ; 
output=cv2.VideoWriter("OUTPUT.avi",fourcc,20.0,(660,490)); 
 #width,height pass 0 for gray frames
while cap.isOpened():
   ret,frame=cap.read();
   if ret==True: 
  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray) 
        output.write(frame)
        k = cv2.waitKey(23)
        if k == ord("s"):
            break
cap.release();
output.release();
cv2.destroyAllWindows(); 