import cv2
import time

face_cascade = cv2.CascadeClassifier('D:\\Google Vertex AI\\Eye-Blink-Counter-master\\Eye-Blink-Counter-master\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\\Google Vertex AI\\Eye-Blink-Counter-master\\Eye-Blink-Counter-master\\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
c = 0  # Total blink counter
blink_counter = 0  # Blink counter for 2 minutes
start_time = time.time()
duration = 120  # Duration of 2 minutes in seconds

while (time.time() - start_time) < duration:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        k = 1
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            k = 0
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        if k == 1:
            c += 1  # Increase the total blink counter
            blink_counter += 1  # Increase the blink counter for 2 minutes
            print("You've blinked your eyes", c, "times")
        else:
            print("Not blinking!")
    
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

print("Total number of blinks in 2 minutes:", blink_counter)
