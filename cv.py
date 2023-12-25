from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n-seg.pt')  # load an official model

# Predict with the model
results = model('./IMG_8674.mov')
