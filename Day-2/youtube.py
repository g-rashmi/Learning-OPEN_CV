import pafy      # pip install pafy
import cv2
url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
data = pafy.new(url )
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture(0)   
cap.open(data.url)

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #read the frame
    
    if ret==True:
        
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
        #cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break
 
# Release everything if work is done
cap.release()
output.release()
cv2.destroyAllWindows()

#if any  error regarding youtube-dl occur thn
#pip3 install youtube-dl
