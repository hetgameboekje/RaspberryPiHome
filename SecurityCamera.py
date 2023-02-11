import cv2
import time
import datetime

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Create background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# threshold for motion detection
threshold = 0.1

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use background subtractor to detect motion
    fgmask = fgbg.apply(frame)

    # Calculate the ratio of non-zero pixels to total pixels
    ratio = cv2.countNonZero(fgmask) / (frame.shape[0] * frame.shape[1])

    # Save the frame as an image file if motion is detected
    if ratio > threshold:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = "./captured_image_{}.jpg".format(current_time)
        cv2.imwrite(file_name, frame)
        print("Motion detected! Image saved as {}".format(file_name))
        time.sleep(0.5)
        
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the capture
cap.release()
