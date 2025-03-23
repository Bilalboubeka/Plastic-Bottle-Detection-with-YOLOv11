# Plastic Bottle Detection with YOLOv11

This repository provides a real-time object detection system using the YOLOv11 model to identify and track plastic bottles.

## Overview
The system is designed to detect plastic bottles in real-time video feeds, providing a robust tool for various applications such as waste management and environmental monitoring.

## Features

- **Real-time Detection**: Utilizes a trained YOLOv11 model to detect plastic bottles in live video streams.
- **Visualization**: Displays detected objects with bounding boxes for clear visualization.
- **Adjustable Confidence Threshold**: Allows users to adjust the confidence level for detection to suit specific requirements.

## Requirements

To run this project, ensure you have the following dependencies installed:

- **Python**: Version 3.8 or higher.
- **OpenCV**: For video processing and visualization.
- **Ultralytics YOLO Library**: For object detection using YOLOv11.

You can install the required dependencies using pip:
```bash
pip install opencv-python ultralytics
```
## Usage

1. **Clone the Repository**:
git clone https://github.com/Bilalboubeka/Plastic-Bottle-Detection-with-YOLOv11.git
cd Plastic-Bottle-Detection-with-YOLOv11


2. **Place the Trained Model**:
Download the trained YOLOv11 model file (`best.pt`) from this link https://drive.google.com/drive/folders/1P-xoPzugjTcQlzx6liMn_Qp8dsE3oC9V?usp=sharing and place it in the root directory of the repository.

3. **Run the Detection Script**:
python detect_bottles.py

Press `q` to exit the detection window.

## File Structure

- **detect_bottles.py**: The main script for running the plastic bottle detection.
- **best.pt**: YOLO model weights (to be added by the user).

## Acknowledgments

This project relies on the Ultralytics YOLO library for efficient object detection.

## Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss what you would like to change.

## Contact

If you have any questions or feedback, feel free to contact me at [bilalboubeka@gmail.com](mailto:bilalboubeka@gmail.com).
