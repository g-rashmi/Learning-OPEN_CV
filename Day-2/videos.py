# import cv2;  
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
