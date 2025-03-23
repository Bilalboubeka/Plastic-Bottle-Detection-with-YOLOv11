
import cv2
from ultralytics import YOLO

# Load your trained YOLO model
model = YOLO("best.pt")  # Path to your .pt file


# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 for default camera
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Main loop for object detection
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Run YOLO inference on the frame with confidence threshold 
    results = model(frame, conf=0.8)  # Set confidence threshold here

    # Visualize the results on the frame
    annotated_frame = results[0].plot()  # Get the annotated frame with bounding boxes

    # Display the annotated frame
    cv2.imshow("YOLO Object Detection", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
