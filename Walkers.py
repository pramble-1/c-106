import cv2


# Create our body classifier
body_classifier = cv2.CascadeClassifier('harrcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    for (x, y, w, h) in frame:
         cv2.rectangle(frame,(x,y), (x+w, y+h), (255, 0, 0), 2)

    # Pass frame to our body classifier
    cv2.iamshow('frame',frame)
    bodies=body_classifier.detechMultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
