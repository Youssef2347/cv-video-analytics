import cv2
import time

VIDEO_PATH = "Day1_detection/Input/football.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Could not open video.")
    exit()

frame_count = 0

start_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

end_time = time.time()

elapsed_time = end_time - start_time

processing_fps = frame_count / elapsed_time

print("Frames processed:", frame_count)
print("Time taken:", elapsed_time)
print("Processing FPS:", processing_fps)

cap.release()