import cv2

VIDEO_PATH = "Day1_detection/Input/football.mp4"

# Open the video
cap = cv2.VideoCapture(VIDEO_PATH)

# Check if the video opened successfully
if not cap.isOpened():
    print("Could not open video.")
    exit()

# Read and display every frame
while True:

    ret, frame = cap.read()

    # Stop when there are no more frames
    if not ret:
        break

    # Display the current frame
    cv2.imshow("Football", frame)

    # Check if the user pressed q
    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):
        break

# Release the video
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()