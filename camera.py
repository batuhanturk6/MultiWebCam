import cv2
import numpy as np
import time

image_path = 'IMAGE_PATH'
static_image = cv2.imread(image_path)
static_image_resized = cv2.resize(static_image, (320, 240))

def capture_frame(cam):
    ret, frame = cam.read()
    if ret:
        return cv2.resize(frame, (320, 240))
    else:
        return static_image_resized

cams = []
for i in range(3):
    cam = cv2.VideoCapture(i)
    if cam.isOpened():
        cams.append(cam)
    else:
        cams.append(None)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

start_time = time.time()
recording_duration = 10 * 60 

while True:
    frames = []

    for cam in cams:
        if cam is not None:
            frame = capture_frame(cam)
        else:
            frame = static_image_resized
        frames.append(frame)

    
    top_row = np.hstack((frames[0], frames[1]))
    bottom_row = np.hstack((frames[2], static_image_resized))
    combined_frame = np.vstack((top_row, bottom_row))

    cv2.imshow('Multi-Camera View', combined_frame)

    out.write(combined_frame)

    if time.time() - start_time > recording_duration:
        print("Recording complete.")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Recording stopped by user.")
        break

while time.time() - start_time < recording_duration:
    out.write(combined_frame)

for cam in cams:
    if cam is not None:
        cam.release()
out.release()

cv2.destroyAllWindows()