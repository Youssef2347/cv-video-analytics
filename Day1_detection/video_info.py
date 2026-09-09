import cv2

VIDEO_PATH = "Day1_detection/Input/football.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Could not open video.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

duration = frame_count / fps

print("===== VIDEO INFORMATION =====")
print(f"Width:       {width}")
print(f"Height:      {height}")
print(f"Resolution:  {width}x{height}")
print(f"FPS:         {fps:.2f}")
print(f"Frames:      {frame_count}")
print(f"Duration:    {duration:.2f} seconds")

cap.release()